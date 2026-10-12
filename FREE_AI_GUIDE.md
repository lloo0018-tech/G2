# 🤖 Free AI Guide — build your whole app with AI for $0

You **don't need** a paid plan or the GitHub Student Developer Pack. Every free AI has limits, so the trick is to **combine a few free tools** and **share the work across your group**.

> ℹ️ Free AI plans change often. This guide was written in October 2026. If a tool's limits look different, the plan below still works with any free AI chat.

---

## 1. Which AI to use for what (everyone has a laptop)

| Job | Tool | Why |
|---|---|---|
| 🚀 **Build the app** (main tool) | **Google Antigravity** (free plan) | An AI coding app on your laptop. You describe what you want and it **edits the files and runs the app for you**. No copy-pasting. |
| 🏗️ **Backup builder** (when Antigravity's limit runs out) | **ChatGPT**, **Gemini** or **Claude** (free plans) | Works with `AI_PROMPT.md`: it plans your app, then gives you complete files to paste in |
| 🔧 **Quick fixes** | **GitHub Copilot Free** in VS Code | Can see your files. Good for "fix this error" or "explain this line". |

**❌ Skip these:**
- **Firebase Studio:** closed to new users.
- **Gemini Code Assist:** its free plan ended in June 2026.

**About the limits:**
- **Antigravity's free plan** has weekly limits. Google doesn't publish the exact numbers and has lowered them several times. When it says you've reached your limit, switch to the backup builder (the relay method in section 3) until it resets.
- **Copilot Free** comes with every GitHub account, with no Student Pack needed. It only gives a small number of chat messages each month (about 50), so **save it for small fixes.**

---

## 2. Set up (each group member, once)

### A. Get the project on your laptop
Follow README steps **A → J**. You need Python and Git installed, your group's project downloaded, and the starter app running.

### B. Install Google Antigravity
1. Go to **https://antigravity.google** and download it for your computer (Mac or Windows).
2. Install it and open it. Sign in with a **Google account**.
   *If your school Google account doesn't work, use a personal Gmail account. Check with your teacher first.*
3. Go to **File → Open Folder** and choose your group's project folder (the one you downloaded with `git clone`).
4. If it asks whether you trust the folder, click **Yes**. If it suggests installing the **Python** extension, click **Install**.

> 💡 Antigravity looks and works like VS Code, so every step in the README works the same way inside it (the terminal, Git, opening files).

### C. Build your app with the Antigravity agent
1. Fill in `PROJECT_IDEA.md` with your group and save it.
2. Open the **Agent** panel and start a new conversation.
3. Copy **everything below the line** in `AI_PROMPT.md`, paste it, and add at the end:
   ```
   Read PROJECT_IDEA.md and all the project files yourself.
   Make the file changes directly in the project.
   ```
4. The agent shows you **a plan first**. Read it as a group. Ask for changes, or approve it. Ask it to save the plan as **`PLAN.md`**.
5. The agent edits the files. **Review each change before you accept it.** If it wants to run a terminal command, read the command first. Only allow commands you understand, like `python app.py` or `python -m pytest`.
6. Run the app (README step I) and the tests (step J). Then try every feature in the browser.
7. Save your work to Git after every working step (README step O).

**Safety rules for the agent:**
- ❌ Never let it delete folders, change files outside your project, or run commands you don't understand.
- ❌ Never give it passwords, and never paste the `.env` file.
- ✅ If it gets confused or keeps making the same mistake, start a **new conversation** and attach `PLAN.md`.

### D. Set up the backups (2 min)
1. Make a free account on **at least one** chat AI:
   - ChatGPT: https://chatgpt.com
   - Gemini: https://gemini.google.com
   - Claude: https://claude.ai
2. *(Optional)* Turn on **Copilot Free** in VS Code or Antigravity by signing in with your GitHub account.
3. **Agree as a group which AI you'll all use** as the backup. Using the same one keeps the code style consistent.

---

## 3. The "relay" method: never get stuck on limits

Use this when **Antigravity's limit runs out**, or if it doesn't work for someone. Free AIs stop answering after a number of messages, then reset later (Antigravity resets weekly, chat AIs usually daily). Every member has **their own** limit, so a group of 4 gets **4× the messages**. You pass the work along like a relay race.

> If you already made `PLAN.md` with Antigravity, skip Leg 1 and go straight to "Next legs".

### 🏁 Leg 1: make the plan (the team lead)
1. Open a chat AI → **new chat**.
2. Attach or paste `app.py`, the `templates/` files, `static/style.css`, `tests/test_app.py` and your filled-in `PROJECT_IDEA.md`.
3. Paste the prompt from `AI_PROMPT.md` and send it.
4. The AI replies with a **plan**. Discuss it as a group, ask for changes, then approve it.
5. ⭐ **Important:** make a new file in your project called **`PLAN.md`** and paste the whole plan into it. Save it and push it to GitHub. **The plan is your relay baton.**

### 🏃 Next legs: build (anyone in the group)
Type **`next`** to get files. Paste each file into your project, test it, and save it to Git (README step O).

**When the AI says you've hit your limit,** the next teammate opens **their own** AI and starts a new chat with:
1. The same files as before (they're now updated), **plus `PLAN.md`**.
2. The prompt from `AI_PROMPT.md`.
3. Then, **before sending**, add this at the bottom:

```
We already finished Step 1. Our approved plan is in PLAN.md - follow it exactly.
These files are already done: <list them, e.g. app.py, templates/base.html>
Continue with the remaining files. Do not redo the plan.
```

The new AI picks up exactly where the last one stopped. 🎉

### 💡 Even better: give each member one part
Each person builds **their own part** with **their own** AI account (with `PLAN.md` attached):

| Member | Asks their AI for |
|---|---|
| Backend | `app.py`: routes and database |
| Frontend | the files in `templates/` |
| Design | `static/style.css`: colours and polish |
| Tester | `tests/test_app.py` + the manual checklist |

Tell the AI: *"Only give me `<your files>`. The others are being made by teammates. Follow PLAN.md exactly so the names match."*

---

## 4. Get more from every message

1. ✍️ **Fill in `PROJECT_IDEA.md` well.** A clear idea gives good code the first time, with fewer repeats.
2. 📋 **Paste the full error** the first time. *"It doesn't work"* wastes a message. The whole red error text fixes it in one.
3. 🎯 **Ask for one thing at a time.** *"Add a rating from 1 to 5 to books"* works better than a list of ten changes.
4. 💾 **Save to Git after every success** (`git add .` → `git commit -m "..."` → `git push`). If the next change breaks everything, you can go back for free.
5. 🔁 **The same mistake twice?** Start a **new chat** with the current files. Long chats confuse the AI.
6. 🧠 **Ask the AI to explain** anything you don't understand. You'll be asked about your code when you present.

---

## 5. Ready-to-copy messages

**Fix an error:**
```
When I run the app I get this error:
<paste the full error>
Here is the file it mentions:
<paste the file>
Explain the cause in 2 sentences, then give me the complete fixed file.
```

**Add a small feature:**
```
Following PLAN.md, add this feature: <describe it>.
Keep all the security rules from AI_PROMPT.md.
Give me every changed file in full, plus a test for it in tests/test_app.py.
```

**Understand the code:**
```
Explain what this code does, line by line, in simple words,
as if I'll have to explain it to my teacher:
<paste the code>
```

**Change the look:**
```
Make the design look more <modern / playful / professional>.
Only change static/style.css and templates/base.html.
Our main colour is <colour>. Give me the complete files.
```

---

## 6. Rules for using AI

- ✅ Use AI to **write, fix and explain** code. That's the point of this project.
- ✅ **Read and test** everything the AI gives you. AI makes mistakes.
- ✅ Every member must be able to **explain** the part they own.
- ❌ Never paste **passwords, secret keys or the `.env` file** into an AI.
- ❌ Don't let the AI remove the security features (the `csrf_token` in forms, login checks). `AI_PROMPT.md` already tells it not to.

**Next step:** go back to `README.md`, section **K**. 🚀
