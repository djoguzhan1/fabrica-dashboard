# Proof projects

Three small, complete tools that back up the "small technical tasks" side of the Upwork
profile. Each folder is a standalone repository: its own README, tests, CI, licence and
`.gitignore`. They are developed here and published as separate public repos under
`github.com/djoguzhan1/`, which is what the profile and portfolio link to.

| Folder | What it is | Stack | Checks |
| --- | --- | --- | --- |
| `tidycsv/` | Clean a messy CSV, write a three-sheet Excel report | Python, pandas, openpyxl | 27 pytest, ruff, CI 3.10–3.12 |
| `docbrief/` | Page-referenced briefs of PDFs/URLs via OpenAI or Anthropic | Python, pypdf, httpx, selectolax | 19 pytest (offline), ruff, CI |
| `sheet-notify/` | Email + Slack alert for new Google Sheet rows | Google Apps Script | 7 node:test on pure helpers, CI |

## Publishing each project as its own repo

These need to be run from your own machine (or anywhere `gh` is logged in to your account),
once per project. Repo names must match the URLs used in the READMEs and in
`docs/upwork-portfolio/README.md`.

```bash
gh auth status                     # must show djoguzhan1

publish () {                       # usage: publish <name> "<description>"
  rm -rf "/tmp/$1" && cp -r "proof-projects/$1" "/tmp/$1" && cd "/tmp/$1" &&
  git init -b main && git add -A && git commit -qm "Initial release" &&
  gh repo create "djoguzhan1/$1" --public --source=. --push --description "$2" && cd -
}

publish tidycsv      "Clean a messy CSV and turn it into an Excel report in one command."
publish docbrief     "Structured, page-referenced briefs of PDFs and web pages (OpenAI / Anthropic)."
publish sheet-notify "Email and Slack alerts for new rows in a Google Sheet (Apps Script)."
```

Publishing from a copy in `/tmp` keeps this repository free of nested `.git` folders. For
later updates, clone the public repo, copy the changed files over it, commit and push — or
just develop in the public repo from then on and treat this folder as the archive.

After each push:

1. Check the **Actions** tab: the CI badge should go green within a minute or two.
2. Add topics on the repo page (Settings gear next to About): e.g. `python`, `csv`, `excel`, `pandas` /
   `llm`, `summarization`, `openai`, `anthropic` / `google-apps-script`, `google-sheets`, `slack`.
3. On your GitHub profile, **Customize your pins** and pin all three plus `web-dev-portfolio`.
4. For `docbrief`, run one real brief locally and read it against the source before you
   mention the tool in a proposal:

   ```bash
   pip install -e "proof-projects/docbrief[openai]"
   export OPENAI_API_KEY=...
   docbrief proof-projects/docbrief/examples/meeting-notes.md -o /tmp/brief.md
   ```

## Working on them here

```bash
pip install -e "proof-projects/tidycsv[dev]" -e "proof-projects/docbrief[dev]"
(cd proof-projects/tidycsv && ruff check . && pytest -q)
(cd proof-projects/docbrief && ruff check . && pytest -q)
(cd proof-projects/sheet-notify && node --test)
```
