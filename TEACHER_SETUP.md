# 👩‍🏫 Teacher setup (5 minutes, once)

1. Create a GitHub repository, e.g. `student-app-kit` (Public).
2. Upload everything in this folder, **including hidden files** (`.gitignore`, `.env.example`, `.dockerignore`).
   Or use the terminal from inside this folder:
   ```bash
   git init && git add . && git commit -m "Student app kit" && git branch -M main
   ```
   ```bash
   git remote add origin https://github.com/YOUR-USER/student-app-kit.git && git push -u origin main
   ```
3. On GitHub, go to **Settings → General** and tick **Template repository**.
4. Share the repo link with your class. Each group clicks **Use this template**, opens `START_HERE.md`, then follows `README.md` from step A.

**Suggested schedule**

| Session | Goal | README sections |
|---|---|---|
| 1 | Install the tools, run the starter, form groups | A → J |
| 2 | Fill in `PROJECT_IDEA.md`, generate the plan and code with AI | K → M |
| 3 | Test, fix, split the work with Git | N → P |
| 4 | Deploy online | Q → V |
| 5 | Polish and present | W → Y |

**Tips**
- Check each group's `PROJECT_IDEA.md` before they start using AI. A good idea sheet leads to good AI output.
- Ask every student to explain one route and one template they own. The AI prompt asks the AI to write likely teacher questions with answers, which is good practice for this.
- **No paid AI needed:** `FREE_AI_GUIDE.md` sets students up with **Google Antigravity** (a free AI coding app; students sign in with a Google account, so check your school's rules on accounts). Free ChatGPT/Gemini/Claude plus Copilot Free are the backup when its weekly limit runs out. No Student Pack required.
- **No installs allowed on school computers?** Groups can use GitHub Codespaces (see "No laptop setup?" in the README). The `.devcontainer` folder makes it set itself up. (Firebase Studio is closed to new users.)
- Render and PythonAnywhere free plans usually don't ask for a card. AWS does, unless you use **AWS Academy** or **AWS Educate** classroom accounts.
