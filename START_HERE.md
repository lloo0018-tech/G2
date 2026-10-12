# 👋 START HERE — how to find your way around this kit

You're in the right place. This page tells you **what each file is for** and **what to open next**.

---

## 1. Open the kit the right way

The easiest way is in **VS Code** (free: https://code.visualstudio.com). It shows every file in a sidebar.

1. In VS Code, go to **File → Open Folder** and choose the `student-app-kit` folder.
2. If VS Code asks *"Do you trust the authors?"*, click **Yes**.
3. To read a guide **nicely formatted**, right-click a `.md` file and choose **Open Preview**. You can also press **Cmd + Shift + V** (Mac) or **Ctrl + Shift + V** (Windows).

> 💡 Some files start with a dot (`.gitignore`, `.devcontainer`). Finder hides them on a Mac. To see them, press **Cmd + Shift + .** in Finder. VS Code always shows them.

---

## 2. What each file is for

### 📖 Guides (just reading, no code)

| File | For | What it's for |
|---|---|---|
| `START_HERE.md` | Everyone | This page: a map of the kit |
| `TEACHER_SETUP.md` | Teacher | How to share the kit with the class, plus a 5-session plan |
| `README.md` | Students | **The main A–Z guide**, from installing the tools to presenting |
| `PROJECT_IDEA.md` | Students | A form each group fills in about their app idea |
| `AI_PROMPT.md` | Students | The text you copy into ChatGPT, Claude, Gemini or Copilot to build your app |
| `FREE_AI_GUIDE.md` | Students | How to build with **Google Antigravity** (free AI that edits your files), plus backup free AIs and the relay method |

### 🧩 The app itself

| File / folder | What it is | Who usually edits it |
|---|---|---|
| `app.py` | The main program: pages, database and security, all in one file | Backend (or the AI) |
| `templates/` | The pages people see (home, login, dashboard, forms) | Frontend |
| `static/style.css` | Colours and styling. Change `--brand` for your main colour. | Design |
| `tests/test_app.py` | 12 automatic checks that the app still works | Tester |
| `requirements.txt` | The Python packages the app needs | Rarely edited |
| `requirements-dev.txt` | The same, plus the testing package | Rarely edited |

### ⚙️ Setup and deployment (leave these alone unless the guide says otherwise)

| File / folder | What it's for |
|---|---|
| `deploy/aws/` | Scripts that set up, update and back up the app on an AWS server |
| `render.yaml` | Lets Render put the app online in one click |
| `Dockerfile`, `.dockerignore` | Run the app on any host that supports Docker |
| `.devcontainer/` | Makes the kit open ready-to-use in GitHub Codespaces (in the browser) |
| `.env.example` | Example server settings |
| `.gitignore` | Stops passwords and data from being uploaded to GitHub. **Don't delete it.** |

---

## 3. What to do, in order

### 👩‍🏫 If you're the teacher
1. Read `TEACHER_SETUP.md`.
2. Skim `README.md`, so you know the steps your students will follow.
3. *(Recommended)* Try it yourself: follow README steps **B → I** (about 15 min). The starter app will run at http://127.0.0.1:5000.
4. Put the kit on GitHub as a template (`TEACHER_SETUP.md`, steps 1–4) and share the link.

### 🧑‍🎓 If you're a student
1. **README A → J:** set up the tools and run the starter app.
   *Can't install anything?* Use **"No laptop setup? Code in your browser"** near the top of the README.
2. **Fill in `PROJECT_IDEA.md`** together as a group, and read **`FREE_AI_GUIDE.md`**.
3. **README K → P:** paste `AI_PROMPT.md` into an AI to turn the starter into your app, and work as a team with Git.
4. **README Q → V:** put your app online for free.
5. **README W → Z:** fix problems, check the final list, and present.

---

## 4. Where to find answers in the README

The README sections are lettered **A to Z**. Use **Cmd + F** (Mac) or **Ctrl + F** (Windows) and search for the letter's heading, e.g. `## R.`.

| If you want to… | Go to |
|---|---|
| Install the tools | **B, C, D** |
| Get the code from GitHub | **E** |
| Run the app | **I** |
| Run the automatic tests | **J** |
| Use AI to build your group's idea | **K, L, M** + `FREE_AI_GUIDE.md` |
| Fix errors the AI's code causes | **N** |
| Work as a team without overwriting each other | **O** |
| Know what must never go on GitHub | **P** |
| Choose where to host the app | **Q** |
| Put it on AWS | **R** |
| Put it online the easiest way | **S** (Render) or **T** (PythonAnywhere) |
| Code in the browser with nothing installed | **"No laptop setup?"** (just before Part 1) |
| Fix a specific error | **W** |
| Check everything before presenting | **X** |
| Plan your presentation | **Y** |
| Understand a technical word | **Z** |

---

## 5. Stuck?

1. Look in **README section W** (Troubleshooting).
2. Ask your AI: *"I'm building a Flask app. I ran `<command>` and got this error: `<full error>`. Here is my file: `<file>`. What's wrong?"*
3. Ask your teacher. Show them the **full** error message.

**Next step:** open `README.md` and start at **A**. 🚀
