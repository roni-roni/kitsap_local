# Primer: why GitHub is useful here

You do not need to be a Git expert. You need six habits, and you need to
understand why each one earns its place on a project like this.

## What GitHub gives this project

| Feature | Why it matters for Kitsap Local |
| --- | --- |
| **History** | Every change is saved and reversible. "It worked last week" becomes "let's see what changed". |
| **Issues** | The backlog: one issue per unit of work, grouped by class milestone. It is also where tester feedback and data-source checks live. |
| **Milestones** | Class 1 through Class 10, plus "Later". Progress bars for free. |
| **Pull requests** | A place to review your own work before it lands, and (later) check that tests pass. |
| **Projects board** | Optional kanban view over the issues. |
| **Actions (CI)** | Runs `flutter analyze` and `flutter test` on every push (Class 9). |
| **Releases and tags** | Tag `v1.0.0` and `v1.1.0` so a store build maps back to exact code. |
| **Pages** | Free hosting for the **privacy policy** the Play Store requires (Class 7). |
| **Secret scanning** | Warns you if a key slips into a commit. Prevention is the `.gitignore`. |

## Six habits

1. **Small commits, clear messages.** `Add Ferry terminal list on mock data`, not `stuff`.
2. **Branch per issue.** `git switch -c 23-ferry-terminal-list`.
3. **Link work to issues.** Write `Closes #23` in the PR. Merging closes the issue.
4. **Pull requests, even solo.** The diff view catches accidental debug code and secrets.
5. **Never commit secrets.** Keys, keystores, `google-services.json`, `.env`. The
   repo's `.gitignore` covers the usual ones; see below.
6. **Tag every release.** `git tag v1.0.0 && git push --tags`.

## First-time setup

```
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
gh auth login                       # GitHub CLI; optional but handy

git init
git add .
git commit -m "Boilerplate: six-tab shell"
gh repo create kitsap-local --private --source=. --push
```

Start **private**. Make it public later if you want, after checking history for
anything sensitive.

## Seeding the backlog

```
DRY_RUN=1 tools/backlog/seed_issues.sh    # preview
tools/backlog/seed_issues.sh              # create milestones, labels, issues
```

Edit `tools/backlog/backlog.json` first if you want to change the plan. Run it
once; running it twice creates duplicate issues.

## Protect `main`

In **Settings > Branches**, add a rule for `main`: require a pull request, and (once
CI exists in Class 9) require checks to pass. It feels like ceremony until the
day it saves you from a broken release.

## Keys and secrets: the rules

- Anything in git history is public forever once pushed, even if deleted later.
  If a key leaks, **rotate it** (get a new one); do not just delete the commit.
- Files that stay out of git (see `.gitignore`): `env/*.json` (real config),
  `android/key.properties` and `*.jks` (release signing), Firebase service
  files, `functions/.env`.
- Files that are committed on purpose: `env/dev.example.json`,
  `functions/.env.example` (empty templates).
- Server-side secrets (the OneBusAway key) live in Firebase Secret Manager,
  never in the app. Anything shipped in the APK can be extracted.

## When you get stuck

- `git status` first. It tells you what state you are in.
- `git restore <file>` throws away uncommitted edits to one file.
- `git log --oneline -10` shows recent history.
- Committed something you should not have, and not yet pushed? Ask before you
  reach for `--force`.
