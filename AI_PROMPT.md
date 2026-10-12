# 🤖 AI Prompt — copy everything below the line into your AI

> **How to use this file**
> 1. Fill in `PROJECT_IDEA.md` first. On free AI plans, read `FREE_AI_GUIDE.md` too (the relay method).
> 2. Open a free AI (ChatGPT, Claude, Gemini, or Copilot in VS Code).
> 3. Upload these files, or paste them (Copilot in VS Code or Codespaces can read them itself): `app.py`, everything in `templates/`, `static/style.css`, `tests/test_app.py`, and your filled-in `PROJECT_IDEA.md`.
> 4. Copy **everything below the line** and send it.
> 5. Follow the AI's steps. When it stops, type **`next`**. If something breaks, paste the **full error** and type **`fix this`**.

---

You are a senior Python web developer and a patient teacher. Our student group is building a web app for a school project. We have a **working starter app** and a **project idea**. Turn the starter into our app, step by step.

## The starter app (what we already have)
- **Python + Flask 3**, one main file `app.py` using the `create_app()` pattern.
- **SQLite** through Python's built-in `sqlite3` (no ORM). Tables are made in the `SCHEMA` string by `init_db()`.
- **Jinja2 templates** in `templates/` that extend `base.html`. **Bootstrap 5** comes from a CDN. Our own CSS is in `static/style.css`.
- It already has sign up, log in and log out, a members-only dashboard, and create/edit/delete for "items" with search and a status filter.
- It has pytest tests in `tests/test_app.py`.
- It is deployed with **gunicorn** (`gunicorn app:app`) on AWS EC2, Render or PythonAnywhere. Settings come from the environment variables `SECRET_KEY`, `DATABASE` and `APP_NAME`.

## Our project idea
(See the `PROJECT_IDEA.md` we attached or pasted. If anything is unclear, choose the simplest sensible option and list your assumptions. Do not stop to ask.)

## Rules you MUST follow
1. **Keep the stack:** Flask, sqlite3, Jinja2 and Bootstrap 5. Only add a new pip package if it is truly needed. If you add one, also add it to `requirements.txt`.
2. **Keep everything that already works:** accounts, `login_required`, the `/health` route, `create_app()`, the module-level `app = create_app()`, the env-var config, and `ProxyFix`.
3. **Keep the security features:**
   - Every `<form method="post">` must include `<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">`.
   - Always use `?` placeholders in SQL. Never build SQL with f-strings or `+` from user input.
   - Users may only see and change their **own** data, unless the idea says data is shared. Check ownership the same way `get_own_item()` does.
   - Hash passwords with `generate_password_hash(password, method="pbkdf2:sha256")`.
   - Changing data (create, update, delete, logout) uses POST only, never GET.
   - Check every form field on the server (required fields, max length, allowed values).
4. **The database:** rename or replace the `items` table to fit our idea. Add tables if needed, with `REFERENCES ... ON DELETE CASCADE` where it fits. Keep `CREATE TABLE IF NOT EXISTS`.
5. **Write beginner-friendly code:** clear names, short comments that explain *why*, and no clever tricks. Students must be able to explain every line.
6. **Make it look good on phones and laptops.** Use Bootstrap classes, and set our brand colour in `--brand` in `style.css`.
7. **Update the tests** in `tests/test_app.py` so they cover our new features. All tests must pass with `python -m pytest`.
8. **Python 3.9+ compatible.** Don't use `match` statements or `X | None` type hints.
9. **Do not change** `Dockerfile`, `render.yaml` or the `deploy/` folder, unless a new package or env var really requires it. If you do, explain why.

## How to answer (very important)
- **Step 1 — Plan.** Reply first with a short plan:
  - app name and a one-line pitch
  - features (must-have vs nice-to-have)
  - database tables, with columns and types
  - a list of pages/routes (`URL — method — what it does — login needed?`)
  - which files you will create or change
  - your assumptions

  End the plan with: "📌 Save this plan in a file called PLAN.md." Then **stop and wait** until we type `next`.
- **If we attach a `PLAN.md`:** the plan is already approved. Skip Step 1, follow `PLAN.md` exactly, and continue from the files we say are done.
- **Step 2 onward — Code, a few files at a time.** For every file:
  - Put the path as a heading, e.g. `### app.py`.
  - Give the **COMPLETE file** in one code block. Never write "...", "rest stays the same" or "add your code here". We will copy and paste whole files.
  - End each reply with: "**Files done so far:** … / **Still to come:** …". Then stop and wait for `next`.
- **Last step — Finish.** Give:
  1. The exact commands to run it on Windows and on Mac (use `.venv\Scripts\python` / `.venv/bin/python`).
  2. A **manual test checklist** (click-by-click steps to try every feature).
  3. A ready-to-paste section `## About our app` for our README (features, screenshot placeholders, who did what).
  4. 5 questions a teacher might ask about our code, each with a short model answer.
- **If we paste an error:** explain the cause in one or two sentences, then give the full corrected file(s).

Start with Step 1 now.
