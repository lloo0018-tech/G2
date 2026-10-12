"""Automatic checks for the app. Run them with:  python -m pytest
If every test passes, the main features still work."""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app  # noqa: E402


@pytest.fixture
def app(tmp_path):
    return create_app({
        "TESTING": True,
        "DATABASE": str(tmp_path / "test.db"),
        "CSRF_ENABLED": False,
    })


@pytest.fixture
def client(app):
    return app.test_client()


def register(client, username="alice", password="secret123"):
    return client.post("/register", data={"username": username, "password": password},
                       follow_redirects=True)


def login(client, username="alice", password="secret123"):
    return client.post("/login", data={"username": username, "password": password},
                       follow_redirects=True)


def logged_in(client, username="alice"):
    register(client, username)
    login(client, username)
    return client


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Get started" in response.data


def test_health_check(client):
    assert client.get("/health").get_json() == {"status": "ok"}


def test_register_and_login(client):
    assert b"Account created" in register(client).data
    response = login(client)
    assert b"Welcome back, alice" in response.data
    assert b"My items" in response.data


def test_duplicate_username_rejected(client):
    register(client)
    assert b"already taken" in register(client).data


def test_short_password_rejected(client):
    assert b"at least 6" in register(client, password="123").data


def test_wrong_password_rejected(client):
    register(client)
    assert b"Wrong username or password" in login(client, password="nope-nope").data


def test_dashboard_requires_login(client):
    response = client.get("/dashboard")
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_create_edit_delete_item(client):
    logged_in(client)
    response = client.post("/items/new", data={"title": "Buy milk", "description": "2 litres",
                                                "status": "todo"}, follow_redirects=True)
    assert b"Buy milk" in response.data

    response = client.post("/items/1/edit", data={"title": "Buy oat milk", "description": "",
                                                  "status": "done"}, follow_redirects=True)
    assert b"Buy oat milk" in response.data

    response = client.post("/items/1/delete", follow_redirects=True)
    assert b"Buy oat milk" not in response.data
    assert b"No items yet" in response.data


def test_empty_title_rejected(client):
    logged_in(client)
    response = client.post("/items/new", data={"title": "  ", "status": "todo"},
                           follow_redirects=True)
    assert b"Title is required" in response.data


def test_search_and_filter(client):
    logged_in(client)
    client.post("/items/new", data={"title": "Math homework", "status": "todo"})
    client.post("/items/new", data={"title": "Science project", "status": "done"})

    response = client.get("/dashboard?q=math")
    assert b"Math homework" in response.data and b"Science project" not in response.data

    response = client.get("/dashboard?status=done")
    assert b"Science project" in response.data and b"Math homework" not in response.data


def test_users_cannot_see_each_others_items(client):
    logged_in(client, "alice")
    client.post("/items/new", data={"title": "Alice secret", "status": "todo"})
    client.post("/logout")

    logged_in(client, "bob")
    assert b"Alice secret" not in client.get("/dashboard").data
    assert client.get("/items/1/edit").status_code == 404
    assert client.post("/items/1/delete").status_code == 404


def test_forms_without_csrf_token_are_blocked(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "csrf.db")})
    response = app.test_client().post("/register", data={"username": "eve", "password": "secret123"})
    assert response.status_code == 400
