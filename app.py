"""
Student App Starter
===================
A small but complete web app (accounts + a database + create/edit/delete)
that any group can grow into their own project.

Run it on your computer:
    python app.py
Then open http://127.0.0.1:5000 in your browser.

Run it on a server (AWS, Render, etc.):
    gunicorn app:app

Everything lives in this one file on purpose, so it is easy to read.
HTML pages are in templates/, styling is in static/style.css.
"""
import os
import secrets
import sqlite3
from datetime import datetime
from functools import wraps

from flask import (
    Flask,
    abort,
    current_app,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.security import check_password_hash, generate_password_hash

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# The allowed values for an item's "status" column.
STATUSES = ["todo", "doing", "done"]

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    username      TEXT    NOT NULL UNIQUE,
    password_hash TEXT    NOT NULL,
    created_at    TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS items (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title       TEXT    NOT NULL,
    description TEXT    NOT NULL DEFAULT '',
    status      TEXT    NOT NULL DEFAULT 'todo',
    created_at  TEXT    NOT NULL
);
"""


# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------
def get_db():
    """Return one database connection per request (reused inside the request)."""
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row  # lets us write row["title"]
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(_error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Create the tables if they do not exist yet. Safe to run many times."""
    db = get_db()
    db.executescript(SCHEMA)
    db.commit()


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


# ---------------------------------------------------------------------------
# Login + security helpers
# ---------------------------------------------------------------------------
def login_required(view):
    """Put @login_required under a route to make it members-only."""

    @wraps(view)
    def wrapped(*args, **kwargs):
        if g.user is None:
            flash("Please log in first.", "warning")
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)

    return wrapped


def csrf_token():
    """A secret per-session token that every form sends back (stops CSRF attacks)."""
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)
    return session["csrf_token"]


def get_own_item(item_id):
    """Load an item that belongs to the logged-in user, or show a 404 page."""
    item = get_db().execute(
        "SELECT * FROM items WHERE id = ? AND user_id = ?", (item_id, g.user["id"])
    ).fetchone()
    if item is None:
        abort(404)
    return item


def read_item_form():
    """Read and check the item form. Returns (data, error_message_or_None)."""
    data = {
        "title": request.form.get("title", "").strip(),
        "description": request.form.get("description", "").strip(),
        "status": request.form.get("status", "todo"),
    }
    if not data["title"]:
        return data, "Title is required."
    if len(data["title"]) > 120:
        return data, "Title must be 120 characters or less."
    if len(data["description"]) > 2000:
        return data, "Description must be 2000 characters or less."
    if data["status"] not in STATUSES:
        return data, "Pick a valid status."
    return data, None


# ---------------------------------------------------------------------------
# The app
# ---------------------------------------------------------------------------
def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-only-change-me"),
        DATABASE=os.environ.get("DATABASE", os.path.join(BASE_DIR, "app.db")),
        APP_NAME=os.environ.get("APP_NAME", "Student App"),
        CSRF_ENABLED=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )
    if test_config:
        app.config.update(test_config)

    # When running behind a web server like nginx (AWS) or a host like Render,
    # trust its headers so links and redirects use the right https:// address.
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

    db_folder = os.path.dirname(app.config["DATABASE"])
    if db_folder:
        os.makedirs(db_folder, exist_ok=True)

    app.teardown_appcontext(close_db)
    with app.app_context():
        init_db()

    @app.context_processor
    def template_globals():
        # These names can be used inside every HTML template.
        return {
            "app_name": app.config["APP_NAME"],
            "csrf_token": csrf_token,
            "statuses": STATUSES,
        }

    @app.before_request
    def load_user_and_check_csrf():
        user_id = session.get("user_id")
        g.user = None
        if user_id is not None:
            g.user = get_db().execute(
                "SELECT id, username FROM users WHERE id = ?", (user_id,)
            ).fetchone()

        if request.method == "POST" and app.config["CSRF_ENABLED"]:
            sent = request.form.get("csrf_token", "")
            if not sent or sent != session.get("csrf_token"):
                abort(400)

    # ---------------- Pages ----------------
    @app.route("/")
    def index():
        if g.user:
            return redirect(url_for("dashboard"))
        return render_template("index.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")
            error = None
            if not 3 <= len(username) <= 30:
                error = "Username must be 3-30 characters."
            elif len(password) < 6:
                error = "Password must be at least 6 characters."
            else:
                db = get_db()
                try:
                    db.execute(
                        "INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)",
                        # pbkdf2 works on every Python install (scrypt does not on macOS).
                        (username, generate_password_hash(password, method="pbkdf2:sha256"), now()),
                    )
                    db.commit()
                except sqlite3.IntegrityError:
                    error = "That username is already taken."
            if error:
                flash(error, "danger")
            else:
                flash("Account created! Please log in.", "success")
                return redirect(url_for("login"))
        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")
            user = get_db().execute(
                "SELECT * FROM users WHERE username = ?", (username,)
            ).fetchone()
            if user is None or not check_password_hash(user["password_hash"], password):
                flash("Wrong username or password.", "danger")
            else:
                session.clear()
                session["user_id"] = user["id"]
                flash(f"Welcome back, {user['username']}!", "success")
                next_url = request.args.get("next", "")
                # Only follow links inside this site (never to other websites).
                if next_url.startswith("/") and not next_url.startswith("//"):
                    return redirect(next_url)
                return redirect(url_for("dashboard"))
        return render_template("login.html")

    @app.route("/logout", methods=["POST"])
    def logout():
        session.clear()
        flash("You have been logged out.", "info")
        return redirect(url_for("index"))

    @app.route("/dashboard")
    @login_required
    def dashboard():
        search = request.args.get("q", "").strip()
        status = request.args.get("status", "")

        sql = "SELECT * FROM items WHERE user_id = ?"
        params = [g.user["id"]]
        if search:
            sql += " AND (title LIKE ? OR description LIKE ?)"
            params += [f"%{search}%", f"%{search}%"]
        if status in STATUSES:
            sql += " AND status = ?"
            params.append(status)
        sql += " ORDER BY id DESC"

        db = get_db()
        items = db.execute(sql, params).fetchall()
        counts = {s: 0 for s in STATUSES}
        for row in db.execute(
            "SELECT status, COUNT(*) AS n FROM items WHERE user_id = ? GROUP BY status",
            (g.user["id"],),
        ):
            counts[row["status"]] = row["n"]
        return render_template(
            "dashboard.html", items=items, counts=counts, search=search, status=status
        )

    @app.route("/items/new", methods=["GET", "POST"])
    @login_required
    def item_new():
        item = {"title": "", "description": "", "status": "todo"}
        if request.method == "POST":
            item, error = read_item_form()
            if error:
                flash(error, "danger")
            else:
                db = get_db()
                db.execute(
                    "INSERT INTO items (user_id, title, description, status, created_at)"
                    " VALUES (?, ?, ?, ?, ?)",
                    (g.user["id"], item["title"], item["description"], item["status"], now()),
                )
                db.commit()
                flash("Item added.", "success")
                return redirect(url_for("dashboard"))
        return render_template("item_form.html", item=item, is_new=True)

    @app.route("/items/<int:item_id>/edit", methods=["GET", "POST"])
    @login_required
    def item_edit(item_id):
        item = get_own_item(item_id)
        if request.method == "POST":
            data, error = read_item_form()
            if error:
                flash(error, "danger")
                item = data
            else:
                db = get_db()
                db.execute(
                    "UPDATE items SET title = ?, description = ?, status = ? WHERE id = ?",
                    (data["title"], data["description"], data["status"], item_id),
                )
                db.commit()
                flash("Item updated.", "success")
                return redirect(url_for("dashboard"))
        return render_template("item_form.html", item=item, item_id=item_id, is_new=False)

    @app.route("/items/<int:item_id>/delete", methods=["POST"])
    @login_required
    def item_delete(item_id):
        get_own_item(item_id)  # makes sure it is yours (404 otherwise)
        db = get_db()
        db.execute("DELETE FROM items WHERE id = ?", (item_id,))
        db.commit()
        flash("Item deleted.", "info")
        return redirect(url_for("dashboard"))

    @app.route("/health")
    def health():
        """Servers ping this to check the app is alive."""
        return {"status": "ok"}

    @app.errorhandler(400)
    def bad_request(_e):
        message = "That form expired. Go back, refresh the page and try again."
        return render_template("error.html", code=400, message=message), 400

    @app.errorhandler(404)
    def not_found(_e):
        return render_template("error.html", code=404, message="We couldn't find that page."), 404

    return app


# Servers (gunicorn, PythonAnywhere) look for this name: app
app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=True)
