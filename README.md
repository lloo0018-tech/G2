# 🚀 Student App Kit — build and launch a real web app, A to Z, for free

This kit gives your group:

- ✅ **A working web app** (Python + Flask). It has accounts, a database, add/edit/delete, search, a mobile-friendly design, security built in, and 12 automatic tests.
- ✅ **An AI prompt** (`AI_PROMPT.md`) that turns this starter into **your own app idea**.
- ✅ **Free deployment** to **AWS**, **Render** or **PythonAnywhere**, with a one-command setup script for AWS.
- ✅ This **A–Z guide**. Follow the letters in order and you can't get lost.

> ⏱️ Time needed: about 30 min to run it, 1–3 sessions to build your idea, and about 30 min to put it online.
> 💸 Cost: $0. You never need to pay for anything in this guide.

---

## 📁 What's in the box

```
student-app-kit/
├── START_HERE.md        ← 👋 map of the kit: open this first
├── app.py               ← the whole app (routes, database, security)
├── templates/           ← the HTML pages
│   ├── base.html        ← shared layout (navbar, messages, footer)
│   ├── index.html       ← home page
│   ├── register.html    ← sign up
│   ├── login.html       ← log in
│   ├── dashboard.html   ← list + search + filter
│   ├── item_form.html   ← add / edit form
│   └── error.html       ← 400 / 404 pages
├── static/style.css     ← your colours and styles
├── tests/test_app.py    ← automatic tests
├── requirements.txt     ← Python packages the app needs
├── requirements-dev.txt ← + packages for testing
├── AI_PROMPT.md         ← 🤖 paste into AI to build YOUR app
├── FREE_AI_GUIDE.md     ← 💸 build it all with free AI (no paid plans)
├── PROJECT_IDEA.md      ← ✏️ fill this in first
├── TEACHER_SETUP.md     ← for the teacher (share the kit)
├── .env.example         ← example server settings
├── Dockerfile           ← run anywhere with Docker
├── render.yaml          ← one-click Render deploy
├── .devcontainer/       ← makes it open in GitHub Codespaces (browser)
└── deploy/aws/          ← AWS scripts: setup, update, backup
```

**How it works, in one picture:**

```
Browser ──► Flask (app.py) ──► SQLite database (app.db)
   ▲              │
   └── HTML page ◄┘  (made from templates/ + Bootstrap)
```

---

## 💻 No laptop setup? Code in your browser with GitHub Codespaces
Use this on a school computer or a Chromebook, or if you can't install anything. It's free (about 60 hours a month on a free GitHub account, and more with the Student Pack).

1. Make a GitHub account (step **A**), and get your group's repo (step **E**).
2. On your repo's GitHub page, click the green **Code** button → **Codespaces** tab → **Create codespace on main**.
3. Wait 1–2 minutes. VS Code opens **in your browser**, with Python and all packages already installed.
4. In the terminal at the bottom, type `python app.py`. A browser tab opens with your app. If it doesn't, open the **Ports** tab and click the 🌐 next to port 5000.
5. Run the tests with `python -m pytest`.
6. **AI help:** click the **Copilot chat** icon and use the prompt from Part 2. Copilot can read and edit your files directly.
7. **Save your work** with Git (step **O**). In Codespaces, you can also use the **Source Control** icon on the left: type a message → **Commit** → **Sync**.

So: skip steps **B, C, D, G and H**. Everything else in this guide is the same. Use `python` instead of `.venv\Scripts\python` / `.venv/bin/python`.

> 🛑 **Stop your codespace when you're done** (**github.com/codespaces** → **⋯** → **Stop codespace**), so you don't use up your free hours. It also stops by itself after 30 minutes with no activity.
>
> ℹ️ **Firebase Studio?** Google is shutting it down. New sign-ups and new workspaces are closed, so use Codespaces instead.

---

# PART 1 — Run it on your computer (A → J)

## A. Make your free accounts
Every group member needs:
1. **GitHub**: https://github.com/signup. This is where your code lives. Students can also apply for the free **GitHub Student Developer Pack**.
2. **AI tools (all free):** **Google Antigravity** is the main tool. It's an AI coding app that edits your files for you. Make a **ChatGPT, Gemini or Claude** account too, as a backup. `FREE_AI_GUIDE.md` shows how to set them up and how your group can share the free limits.

The **team lead** will also need a hosting account later, in Part 3.

## B. Install Python (3.9 or newer)
- **Windows:** download it from https://www.python.org/downloads/. ⚠️ On the first screen of the installer, **tick "Add python.exe to PATH"**, then click Install.
- **Mac:** download it from https://www.python.org/downloads/ (recommended), or use the Python that comes with the Mac.

Check that it worked. Open **Terminal** (Mac) or **PowerShell** (Windows) and type:
```bash
python --version
```
On a Mac, use `python3 --version`. You should see `Python 3.x.x`.

## C. Install VS Code
Download it from https://code.visualstudio.com. Open it, click the **Extensions** icon on the left (four squares), search for **Python** and install the one by Microsoft.

## D. Install Git
- **Windows:** download from https://git-scm.com/download/win and keep clicking Next.
- **Mac:** type `git --version` in Terminal. If it asks to install the developer tools, click **Install**.

Then tell Git who you are, once per computer:
```bash
git config --global user.name "Your Name"
```
```bash
git config --global user.email "you@example.com"
```

## E. Get the code (team lead does this once)
1. Open your teacher's kit page on GitHub and click the green **Use this template → Create a new repository** button. Name it (e.g. `readtrack`), choose **Public**, and click **Create repository**.
   *No template link? Create a new repository and click **"uploading an existing file"**. Drag in **all** files and folders from the kit, including the hidden ones (`.gitignore`, `.env.example`, `.dockerignore`). On a Mac, press **Cmd + Shift + .** in Finder to show hidden files.*
2. Add teammates: go to **Settings → Collaborators → Add people**.

**Everyone** then downloads the repo:
```bash
git clone https://github.com/YOUR-USER/YOUR-REPO.git
```
Then open the folder in VS Code (**File → Open Folder**).

## F. Open the terminal in VS Code
Go to **Terminal → New Terminal**. All commands below go there. The terminal should be in your project folder.

## G. Create a virtual environment (a private box for this project's packages)
**Windows:**
```bash
py -m venv .venv
```
**Mac:**
```bash
python3 -m venv .venv
```
If VS Code asks *"Use this environment for the workspace?"*, click **Yes**.

## H. Install the packages
**Windows:**
```bash
.venv\Scripts\python -m pip install -r requirements-dev.txt
```
**Mac:**
```bash
.venv/bin/python -m pip install -r requirements-dev.txt
```

## I. Run the app 🎉
**Windows:**
```bash
.venv\Scripts\python app.py
```
**Mac:**
```bash
.venv/bin/python app.py
```
Open **http://127.0.0.1:5000** in your browser. Sign up, log in and add a few items.
To stop the app, click the terminal and press **Ctrl + C**.

> 💡 The database file `app.db` is created automatically. Delete it any time to start fresh. The app recreates it.

## J. Run the automatic tests
**Windows:**
```bash
.venv\Scripts\python -m pytest
```
**Mac:**
```bash
.venv/bin/python -m pytest
```
You should see **`12 passed`**. Run the tests after every big change. If something turns red, you broke something; see section W.

---

# PART 2 — Turn it into YOUR app with AI (K → P)

## K. Fill in `PROJECT_IDEA.md`
Do this together as a group. Be specific: list your features, the data you save and the pages you want. A finished example is at the bottom of the file.

## L. Give the AI your project
> 💸 **Main tool: Google Antigravity** (free AI that edits your files, set up in `FREE_AI_GUIDE.md`, section 2). **When its limit runs out,** follow the **relay method** in `FREE_AI_GUIDE.md`. Save the AI's plan as `PLAN.md`, so any teammate can continue when one person hits their limit.

1. Open your AI assistant and start a **new chat**.
2. **Attach** (📎) or paste these files: `app.py`, all files in `templates/`, `static/style.css`, `tests/test_app.py`, and `PROJECT_IDEA.md`.
3. Open `AI_PROMPT.md`, copy **everything below the line** and send it.
4. The AI replies with a **plan**. Read it as a group. Want changes? Say so (for example, "remove the leaderboard, add a calendar page"). Happy with it? Type **`next`**.

> 🛠️ **Using Google Antigravity (recommended), Copilot or Cursor?** See `FREE_AI_GUIDE.md`, section 2C, for Antigravity. Switch the chat to **Agent** mode and paste the prompt. It can read and edit the files itself. Still check each change.

## M. Put the AI's code into your project
For each file the AI gives you:
1. Open that file in VS Code. If it's a new file, right-click the folder and choose **New File** with the exact same name.
2. Select all (**Ctrl/Cmd + A**), delete, and paste the AI's **complete** file.
3. Save (**Ctrl/Cmd + S**).
4. Type **`next`** in the AI chat until it says it's finished.

⚠️ If you changed the database tables, **delete `app.db`** before running again, so the new tables are created.

## N. Test → fix → repeat
1. Run the app (section I) and the tests (section J).
2. Something broke? Copy the **full red error text** from the terminal or browser into the AI and type **`fix this`**.
3. Repeat until everything works. Then go through the AI's **manual test checklist**.

> 💡 **Golden rule:** change one thing at a time, test it, then save it to Git (section O). Small steps are easy to fix.

## O. Teamwork with Git (so you don't overwrite each other)
**The daily routine for each member:**
```bash
git pull
```
*(Get your teammates' latest work. Do this BEFORE you start.)*

…do your work, test it…
```bash
git add .
```
```bash
git commit -m "Add rating stars to book page"
```
```bash
git push
```

**Split the work by files**, so two people don't edit the same file at the same time:

| Role | Owns |
|------|------|
| Backend | `app.py` (routes + database) |
| Frontend / Design | `templates/` + `static/style.css` |
| Tester | `tests/test_app.py` + the manual checklist |
| Lead / Docs | `README.md`, deployment, final demo |

Got a **merge conflict** (`<<<<<<<` lines in a file)? Paste the whole file into the AI with "resolve this merge conflict, keep both changes". Then add, commit and push.

## P. Rules: what must NEVER go on GitHub
- ❌ `.env` (passwords and secret keys)
- ❌ `app.db` or `data/` (your users' data)
- ❌ `.venv/` (huge, and each computer makes its own)

The included `.gitignore` already blocks all of these. Don't delete it.

---

# PART 3 — Put it online for free (Q → V)

## Q. Pick where to host

| Option | Best for | Cost | Data kept? | Difficulty |
|---|---|---|---|---|
| **R. AWS EC2** ⭐ | Real cloud experience, full control | Free with AWS free-tier credits* | ✅ Yes | ★★★ |
| **S. Render** | Fastest: one click from GitHub | Free plan | ⚠️ **Resets on every redeploy/restart** (fine for demos) | ★ |
| **T. PythonAnywhere** | Easiest *permanent* free hosting | Free "Beginner" plan | ✅ Yes | ★★ |
| **U. Docker** | Any other cloud (Railway, Fly.io, Google Cloud Run, AWS App Runner) | Depends on host | Depends on host | ★★★ |

\* AWS needs a credit/debit card to sign up, and it gives new accounts free-tier usage or credits. **Free-tier rules change, so read the current terms at https://aws.amazon.com/free and set a budget alert (step R2).** If your school uses **AWS Academy** or **AWS Educate**, use that account instead. It needs no card.

## R. Deploy on AWS EC2 (step by step)

**R1. Create an account.** Go to https://aws.amazon.com/free → **Create a free account**. Choose the **free plan** if you're asked.

**R2. Set a $0 safety alarm (do this first!).** Search the top bar for **Budgets** → **Create budget** → **Use a template** → **Zero spend budget** → enter your email → **Create**. AWS now emails you if anything ever costs money.

**R3. Choose a region.** In the top-right corner, pick a region close to you (e.g. *Europe (Frankfurt)* or *US East (N. Virginia)*). Use the same one every time.

**R4. Launch the server.** Search for **EC2** → **Launch instance**, then fill in:
| Field | What to choose |
|---|---|
| Name | `student-app` |
| Application and OS Images | **Ubuntu Server 24.04 LTS**. It must say **"Free tier eligible"**. |
| Instance type | the one marked **"Free tier eligible"** (`t3.micro` or `t2.micro`) |
| Key pair | **Create new key pair** → name it `student-app` → **Create**. Keep the downloaded file safe. |
| Network settings | ✅ Allow SSH traffic from **Anywhere** · ✅ **Allow HTTP traffic from the internet** · ✅ **Allow HTTPS traffic from the internet** |
| Storage | 8–30 GB **gp3** (the free tier covers up to 30 GB) |

Click **Launch instance**, then **View all instances**. Wait until the *Instance state* shows **Running** and *Status check* shows **2/2 checks passed** (about 2 min).

**R5. Connect to the server in your browser.** Select your instance → **Connect** → the **EC2 Instance Connect** tab → **Connect**. A black terminal opens. You are now inside your cloud server.

**R6. Install the app with the setup script.** Paste these lines one at a time, replacing the URL with **your** GitHub repo:
```bash
sudo apt-get update -y && sudo apt-get install -y git
```
```bash
git clone https://github.com/YOUR-USER/YOUR-REPO.git ~/app
```
```bash
bash ~/app/deploy/aws/setup_ec2.sh
```
After about 2 minutes you'll see:
```
SUCCESS! Your app is live at:  http://12.34.56.78
```
Open that address in any browser, on any device. **Your app is on the internet! 🎉**

> The script installs Python and nginx, creates a random `SECRET_KEY`, runs the app with gunicorn, and makes it restart automatically after a reboot or crash. Your database is saved at `~/app/data/app.db`.

**R7. Update the live app after you push new code.** Connect again (R5) and run:
```bash
bash ~/app/deploy/aws/update.sh
```

**R8. Back up the database (before demos and big updates):**
```bash
bash ~/app/deploy/aws/backup.sh
```

**R9. Useful server commands:**
| What | Command |
|---|---|
| Is the app running? | `sudo systemctl status studentapp` |
| Show the last 50 log lines | `sudo journalctl -u studentapp -n 50 --no-pager` |
| Restart the app | `sudo systemctl restart studentapp` |
| Change the app name or settings | `nano ~/app/.env`, then restart the app |

**R10. When the project is over:** go to **EC2 → Instances**, select yours, and choose **Instance state → Terminate**. This makes sure you're never charged later.

> ⚠️ **Private repo?** `git clone` will ask for a password. The easiest fix is to make the repo **Public** (**Settings → General → Danger Zone → Change visibility**). Secrets are safe, because `.env` is never uploaded.

## S. Deploy on Render (fastest, ~5 min)
1. Sign up at https://render.com with your **GitHub** account.
2. Click **New → Blueprint**, pick your repo, then click **Apply**. Render reads `render.yaml` and sets everything up, including a random `SECRET_KEY`.
3. Wait for **"Live"**, then open the `https://your-app.onrender.com` link.

**Know these limits:**
- The free plan **sleeps after about 15 minutes with no visitors**. The first visit after that takes 30–60 seconds. Open the site 2 minutes before your demo.
- **The database resets** whenever the app redeploys or restarts. That's fine for a demo. For data that stays, use AWS or PythonAnywhere.
- Every `git push` redeploys the app automatically.

## T. Deploy on PythonAnywhere (free, keeps your data)
1. Sign up for a **Beginner** (free) account at https://www.pythonanywhere.com.
2. Go to **Consoles → Bash** and run the commands below, using your own repo URL:
   ```bash
   git clone https://github.com/YOUR-USER/YOUR-REPO.git ~/app
   ```
   ```bash
   cd ~/app && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt && mkdir -p data
   ```
   ```bash
   python3 -c "import secrets; print(secrets.token_hex(32))"
   ```
   Copy the long random text this prints. That is your secret key.
3. Go to the **Web** tab → **Add a new web app** → **Next** → **Manual configuration** → pick the newest **Python** → **Next**.
4. On the Web tab, fill in:
   - **Source code:** `/home/YOURUSERNAME/app`
   - **Virtualenv:** `/home/YOURUSERNAME/app/.venv`
5. Click the **WSGI configuration file** link. **Delete everything in it** and paste this, with your username and secret key filled in:
   ```python
   import os, sys
   path = "/home/YOURUSERNAME/app"
   if path not in sys.path:
       sys.path.insert(0, path)
   os.environ["SECRET_KEY"] = "PASTE-YOUR-LONG-RANDOM-TEXT-HERE"
   os.environ["DATABASE"] = "/home/YOURUSERNAME/app/data/app.db"
   os.environ["APP_NAME"] = "Student App"
   from app import app as application
   ```
   Click **Save**, go back to the **Web** tab and click the green **Reload** button.
6. Open `https://YOURUSERNAME.pythonanywhere.com` 🎉
7. **To update:** in a Bash console, run `cd ~/app && git pull`, then click **Reload** on the Web tab.
8. Free sites are paused unless you log in and click **"Run until 3 months from today"** on the Web tab. Do it before your demo.

## U. Deploy anywhere with Docker (advanced)
The included `Dockerfile` runs the app on port **8000** with gunicorn. You can test it locally:
```bash
docker build -t student-app .
```
```bash
docker run -p 8000:8000 -e SECRET_KEY=change-me -v "$(pwd)/data:/app/data" student-app
```
Then open http://localhost:8000. Any host that accepts a Dockerfile can run it, such as Railway, Fly.io, Google Cloud Run or AWS App Runner. Always set a `SECRET_KEY` environment variable. To keep data, mount storage at `/app/data`.

## V. Optional: your own domain and HTTPS
- **Render** and **PythonAnywhere** give you `https://` automatically.
- **AWS:** you need a domain name first. Point a DNS **A record** at your server's IP, then run the commands below on the server. Certbot is free.
  ```bash
  sudo apt-get install -y certbot python3-certbot-nginx
  ```
  ```bash
  sudo certbot --nginx -d yourdomain.com
  ```

---

# PART 4 — Finish strong (W → Z)

## W. Troubleshooting

| Problem | Fix |
|---|---|
| `python` is not recognized (Windows) | Reinstall Python and **tick "Add to PATH"**, or use `py` instead of `python`. |
| `No module named flask` | You skipped step H, or you're not using `.venv`. Run step H again. |
| `Address already in use` / port 5000 busy | Another copy of the app is still running, so close the other terminal. On a Mac, AirPlay Receiver uses port 5000. Run `PORT=5001 .venv/bin/python app.py` and open port 5001. |
| `sqlite3.OperationalError: no such column/table` | You changed the tables. Delete `app.db` and run again. |
| "That form expired" (error 400) | Refresh the page and submit again. If **every** form fails, a template is missing the `csrf_token` hidden input. |
| `TemplateNotFound` | The file name or folder is wrong. Templates must be inside `templates/`. |
| `jinja2...UndefinedError` | A template uses a variable the route didn't send. Paste the error into the AI. |
| The page looks unstyled | Check your internet connection (Bootstrap loads from a CDN), then hard-refresh with Ctrl/Cmd + Shift + R. |
| AWS: the site doesn't load | Check that the security group allows **HTTP (port 80)**. Use `http://`, not `https://`. Check the logs (R9). |
| AWS: `git clone` asks for a password | Your repo is private. See the note under R10. |
| Render: the first load is slow | The free plan was asleep. Wait 60 seconds. |
| PythonAnywhere: "Something went wrong" | Go to the **Web** tab and open the **Error log**. Usually it's the WSGI file path or the username. |
| `git push` is rejected | Run `git pull` first, fix any conflicts (section O), then push again. |

**Still stuck?** Ask the AI: *"I'm building a Flask app. I ran `<command>` and got this error: `<full error>`. Here is my file: `<file>`. What's wrong?"*

## X. Final checklist before you present
- [ ] `python -m pytest` shows all tests passed
- [ ] Every must-have feature from `PROJECT_IDEA.md` works
- [ ] Tried on a phone screen (in browser dev tools: F12 → phone icon)
- [ ] The app name and colours are changed (`APP_NAME`, `--brand`)
- [ ] The live link works from a different device
- [ ] A demo account exists with realistic example data
- [ ] The README has an "About our app" section, screenshots and who did what
- [ ] No `.env` or `.db` file is on GitHub
- [ ] Every member can explain at least one part of the code

## Y. Presentation tips (5 minutes)
1. **The problem** (30 sec): who has it, and why it matters.
2. **Live demo** (2 min): sign up → main feature → the "wow" feature.
3. **How it works** (1 min): show the picture at the top of this README. Browser → Flask → SQLite.
4. **What we learned / what was hard** (1 min).
5. **What's next** (30 sec): features you'd add with more time.

Have **screenshots ready** in case the internet fails during your demo.

## Z. Glossary
| Word | Meaning |
|---|---|
| **Flask** | A Python library for making websites. |
| **Route** | A URL like `/dashboard` and the Python function that answers it. |
| **Template** | An HTML file with `{{ placeholders }}` that Flask fills in. |
| **SQLite** | A database stored in one file (`app.db`). |
| **SQL** | The language for reading and saving data: `SELECT`, `INSERT`, `UPDATE`, `DELETE`. |
| **Session** | How the site remembers you're logged in (a signed cookie). |
| **Hash** | A one-way scramble. We store password *hashes*, never the passwords themselves. |
| **CSRF token** | A hidden secret in every form, so other websites can't submit forms as you. |
| **Virtual environment (`.venv`)** | A private folder of packages just for this project. |
| **Git / GitHub** | Git saves versions of your code. GitHub stores them online for your team. |
| **gunicorn** | A production web server that runs Flask on a real server. |
| **nginx** | A web server that sits in front of gunicorn on AWS and handles visitors. |
| **EC2** | A virtual computer you rent in Amazon's cloud. |
| **Deploy** | Put your app on a server so anyone can use it. |
| **Environment variable** | A setting given to the app from outside the code, such as `SECRET_KEY`. |

---

## About our app
_(Replace this section with the one your AI writes for you in the last step.)_
