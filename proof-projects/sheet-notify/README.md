# sheet-notify

Google Apps Script that sends an email and/or a Slack message when a new row appears in a Google Sheet — form responses, rows pushed by Zapier/Make, or rows typed in by hand. Every row is notified exactly once and stamped in a `Notified` column, so retries, bulk pastes and overlapping triggers do not cause duplicates.

No add-ons, no third-party service, no monthly fee. It runs inside the spreadsheet on the owner's Google account.

## What the notification looks like

Email (HTML with a plain-text fallback):

```
New entry: Ada Lovelace (ada@example.com)

Timestamp   2026-03-14 09:30
Name        Ada Lovelace
Email       ada@example.com
Service     Boiler service
Message     Water pressure keeps dropping.

Open the row in Google Sheets →
```

Slack uses Block Kit: a header, one field per column (up to 10), and a link to the exact row.

## Setup (about five minutes)

1. Open the spreadsheet → **Extensions → Apps Script**.
2. Replace the contents of `Code.gs` with the file from this repo. Open **Project Settings**, tick *Show "appsscript.json"*, and replace that file too (it declares the minimal permissions).
3. Save, reload the spreadsheet. A **Notify** menu appears.
4. **Notify → Set up**. This creates a `Settings` sheet, adds a `Notified` column to the watched sheet and installs the trigger. Google will ask you to authorise the script once.
5. Fill in the `Settings` sheet:

   | Setting | Example |
   | --- | --- |
   | Email recipients | `ops@example.com, sales@example.com` |
   | Watched sheet | `Form Responses 1` |
   | Slack webhook URL | `https://hooks.slack.com/services/...` (optional) |
   | Subject template | `New lead: {{Name}} ({{Service}})` |
   | Columns to include | `Name, Email, Service, Message` (empty = all) |
   | Max rows per run | `20` |

6. **Notify → Send test notification**. Check your inbox / channel.

From then on every new row is delivered within a few seconds. Existing rows are left alone until their `Notified` cell is cleared.

Slack: create an *Incoming Webhook* in your Slack app settings and paste the URL. The script refuses URLs that are not on `hooks.slack.com`.

## How it works

- An installable **onChange** trigger fires on edits, form submissions and API writes. It waits 1.5 s so partially written rows are complete, then scans for rows whose `Notified` cell is empty.
- A **script lock** prevents two overlapping runs from sending the same row twice.
- Each processed row gets a timestamp, or `ERROR: …` with the reason. Clear the cell to resend.
- **Max rows per run** caps a single run so a bulk paste of 500 rows does not send 500 emails at once; the rest go out on the next change (or via **Notify → Process pending rows now**).
- Google's free quota is 100 emails per day for consumer accounts and 1,500 for Workspace; Slack has no such limit.

## Customising

- Subject placeholders: any column header as `{{Header}}`, plus `{{row}}` and `{{sheet}}`.
- Email layout: `emailHtml_()`; Slack layout: `slackPayload_()`.
- To notify only on certain rows (e.g. `Status = Urgent`), add a condition at the top of the loop in `processPendingRows()`.

## Development

The Apps Script services (`SpreadsheetApp`, `MailApp`, …) only exist inside Google, but the pure helpers — templates, escaping, record building, Slack payload — are tested in Node:

```
node --test
```

To deploy from the command line instead of pasting, install [clasp](https://github.com/google/clasp), copy `.clasp.json.example` to `.clasp.json`, put your script ID in it and run `clasp push`.

## License

MIT © 2026 Oğuzhan Salatan
