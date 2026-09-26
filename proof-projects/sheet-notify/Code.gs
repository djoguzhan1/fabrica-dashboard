/**
 * sheet-notify
 *
 * Sends an email and/or a Slack message when a new row lands in a Google Sheet
 * (form responses, Zapier/Make pushes, manual entry). Each row is notified once;
 * the script marks it in a "Notified" column so re-runs and retries are safe.
 *
 * Setup: see README.md. Everything you configure lives in the "Settings" sheet,
 * not in this file.
 */

var SETTINGS_SHEET = 'Settings';
var NOTIFIED_HEADER = 'Notified';

/* ------------------------------------------------------------------------ */
/* Menu and one-time setup                                                  */
/* ------------------------------------------------------------------------ */

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Notify')
    .addItem('Set up (create Settings + trigger)', 'setup')
    .addItem('Send test notification', 'testNotify')
    .addItem('Process pending rows now', 'processPendingRows')
    .addSeparator()
    .addItem('Remove trigger', 'removeTriggers')
    .addToUi();
}

/**
 * Creates the Settings sheet (if missing), the Notified column on the watched
 * sheet, and an installable onChange trigger. Safe to run more than once.
 */
function setup() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var settings = ss.getSheetByName(SETTINGS_SHEET) || createSettingsSheet_(ss);
  var config = readSettings_(settings);

  var watched = ss.getSheetByName(config.watchedSheet);
  if (!watched) {
    throw new Error('Watched sheet "' + config.watchedSheet + '" not found. Fix the name in Settings!B3.');
  }
  ensureNotifiedColumn_(watched);

  removeTriggers();
  ScriptApp.newTrigger('onSheetChange').forSpreadsheet(ss).onChange().create();

  SpreadsheetApp.getUi().alert(
    'sheet-notify is set up.\n\n' +
      'Watching: ' + config.watchedSheet + '\n' +
      'Email to: ' + (config.recipients.join(', ') || '(none)') + '\n' +
      'Slack: ' + (config.slackWebhook ? 'yes' : 'no') + '\n\n' +
      'Use Notify > Send test notification to check delivery.'
  );
}

function removeTriggers() {
  ScriptApp.getProjectTriggers().forEach(function (trigger) {
    if (trigger.getHandlerFunction() === 'onSheetChange') {
      ScriptApp.deleteTrigger(trigger);
    }
  });
}

/* ------------------------------------------------------------------------ */
/* Trigger entry points                                                     */
/* ------------------------------------------------------------------------ */

/** Installable onChange trigger. Fires for edits, form submissions and API writes. */
function onSheetChange(e) {
  if (e && e.changeType && ['INSERT_ROW', 'EDIT', 'OTHER'].indexOf(e.changeType) === -1) {
    return;
  }
  // Writes from forms and integrations can arrive before all cells are filled;
  // a short wait avoids sending half a row.
  Utilities.sleep(1500);
  processPendingRows();
}

/**
 * Finds rows on the watched sheet whose Notified cell is empty, sends one
 * notification per row, then stamps the time. Uses a lock so overlapping
 * triggers cannot double-send.
 */
function processPendingRows() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(20000)) {
    return; // another run is already working; it will pick up the same rows
  }
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var config = readSettings_(ss.getSheetByName(SETTINGS_SHEET));
    var sheet = ss.getSheetByName(config.watchedSheet);
    if (!sheet) return;

    var notifiedCol = ensureNotifiedColumn_(sheet);
    var lastRow = sheet.getLastRow();
    if (lastRow < 2) return;

    var headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
    var rows = sheet.getRange(2, 1, lastRow - 1, sheet.getLastColumn()).getValues();
    var sent = 0;

    for (var i = 0; i < rows.length; i++) {
      var row = rows[i];
      if (row[notifiedCol - 1] !== '') continue;
      if (isEmptyRow_(row, notifiedCol)) continue;

      var record = buildRecord_(headers, row, config, notifiedCol);
      var rowNumber = i + 2;
      var result = notify_(record, rowNumber, config);

      sheet.getRange(rowNumber, notifiedCol).setValue(result.ok ? new Date() : 'ERROR: ' + result.error);
      sent++;
      if (sent >= config.maxPerRun) break;
    }
  } finally {
    lock.releaseLock();
  }
}

/** Sends a sample notification using the first data row (or placeholder values). */
function testNotify() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var config = readSettings_(ss.getSheetByName(SETTINGS_SHEET));
  var sheet = ss.getSheetByName(config.watchedSheet);
  var headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
  var row = sheet.getLastRow() >= 2
    ? sheet.getRange(2, 1, 1, sheet.getLastColumn()).getValues()[0]
    : headers.map(function (h) { return h ? 'sample ' + h : ''; });

  var record = buildRecord_(headers, row, config, ensureNotifiedColumn_(sheet));
  var result = notify_(record, 2, config, '[TEST] ');
  SpreadsheetApp.getUi().alert(result.ok ? 'Test sent.' : 'Test failed: ' + result.error);
}

/* ------------------------------------------------------------------------ */
/* Notification                                                             */
/* ------------------------------------------------------------------------ */

function notify_(record, rowNumber, config, subjectPrefix) {
  var subject = (subjectPrefix || '') + fillTemplate_(config.subjectTemplate, record, rowNumber);
  var link = SpreadsheetApp.getActiveSpreadsheet().getUrl() + '#gid=' +
    SpreadsheetApp.getActiveSpreadsheet().getSheetByName(config.watchedSheet).getSheetId() +
    '&range=A' + rowNumber;
  var errors = [];

  if (config.recipients.length) {
    try {
      MailApp.sendEmail({
        to: config.recipients.join(','),
        subject: subject,
        htmlBody: emailHtml_(subject, record, link),
        body: emailText_(subject, record, link),
      });
    } catch (err) {
      errors.push('email: ' + err.message);
    }
  }

  if (config.slackWebhook) {
    try {
      var response = UrlFetchApp.fetch(config.slackWebhook, {
        method: 'post',
        contentType: 'application/json',
        payload: JSON.stringify(slackPayload_(subject, record, link)),
        muteHttpExceptions: true,
      });
      if (response.getResponseCode() >= 300) {
        errors.push('slack: HTTP ' + response.getResponseCode());
      }
    } catch (err) {
      errors.push('slack: ' + err.message);
    }
  }

  return errors.length ? { ok: false, error: errors.join('; ') } : { ok: true };
}

function emailText_(subject, record, link) {
  var lines = [subject, ''];
  record.forEach(function (field) { lines.push(field.name + ': ' + field.value); });
  lines.push('', 'Open row: ' + link);
  return lines.join('\n');
}

function emailHtml_(subject, record, link) {
  var rows = record.map(function (field) {
    return '<tr><td style="padding:6px 12px 6px 0;color:#555;white-space:nowrap;vertical-align:top">' +
      escapeHtml_(field.name) + '</td><td style="padding:6px 0">' + escapeHtml_(field.value) + '</td></tr>';
  }).join('');
  return '<div style="font:14px/1.5 -apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#111;max-width:640px">' +
    '<h2 style="margin:0 0 12px;font-size:18px">' + escapeHtml_(subject) + '</h2>' +
    '<table style="border-collapse:collapse">' + rows + '</table>' +
    '<p style="margin-top:16px"><a href="' + link + '">Open the row in Google Sheets</a></p></div>';
}

function slackPayload_(subject, record, link) {
  var fields = record.slice(0, 10).map(function (field) {
    return { type: 'mrkdwn', text: '*' + field.name + '*\n' + (field.value || '—') };
  });
  var blocks = [
    { type: 'header', text: { type: 'plain_text', text: subject.substring(0, 150) } },
  ];
  // Slack allows at most 10 fields per section block.
  for (var i = 0; i < fields.length; i += 10) {
    blocks.push({ type: 'section', fields: fields.slice(i, i + 10) });
  }
  blocks.push({ type: 'context', elements: [{ type: 'mrkdwn', text: '<' + link + '|Open the row in Google Sheets>' }] });
  return { text: subject, blocks: blocks };
}

/* ------------------------------------------------------------------------ */
/* Settings                                                                 */
/* ------------------------------------------------------------------------ */

var SETTINGS_ROWS = [
  ['Setting', 'Value', 'Notes'],
  ['Email recipients', '', 'Comma-separated. Leave empty to skip email.'],
  ['Watched sheet', 'Form Responses 1', 'Exact tab name to watch for new rows.'],
  ['Slack webhook URL', '', 'Incoming Webhook URL. Leave empty to skip Slack.'],
  ['Subject template', 'New entry: {{Name}} ({{Email}})', 'Use {{Column header}} placeholders, or {{row}}.'],
  ['Columns to include', '', 'Comma-separated headers. Empty = all columns.'],
  ['Max rows per run', '20', 'Safety cap so a bulk paste cannot send hundreds of emails.'],
];

function createSettingsSheet_(ss) {
  var sheet = ss.insertSheet(SETTINGS_SHEET);
  sheet.getRange(1, 1, SETTINGS_ROWS.length, 3).setValues(SETTINGS_ROWS);
  sheet.getRange(1, 1, 1, 3).setFontWeight('bold').setBackground('#1F3A5F').setFontColor('#FFFFFF');
  sheet.getRange(2, 2, SETTINGS_ROWS.length - 1, 1).setBackground('#FFF8E1');
  sheet.setColumnWidth(1, 180);
  sheet.setColumnWidth(2, 360);
  sheet.setColumnWidth(3, 380);
  sheet.setFrozenRows(1);
  return sheet;
}

function readSettings_(sheet) {
  if (!sheet) {
    throw new Error('No "' + SETTINGS_SHEET + '" sheet. Run Notify > Set up first.');
  }
  var values = sheet.getRange(2, 1, SETTINGS_ROWS.length - 1, 2).getValues();
  var map = {};
  values.forEach(function (pair) { map[String(pair[0]).trim()] = String(pair[1]).trim(); });

  var recipients = splitList_(map['Email recipients']);
  var webhook = map['Slack webhook URL'];
  if (webhook && webhook.indexOf('https://hooks.slack.com/') !== 0) {
    throw new Error('Slack webhook URL should start with https://hooks.slack.com/');
  }
  if (!recipients.length && !webhook) {
    throw new Error('Add at least one email recipient or a Slack webhook in Settings.');
  }
  return {
    recipients: recipients,
    watchedSheet: map['Watched sheet'] || 'Form Responses 1',
    slackWebhook: webhook,
    subjectTemplate: map['Subject template'] || 'New entry in {{sheet}} (row {{row}})',
    includeColumns: splitList_(map['Columns to include']),
    maxPerRun: Math.max(1, parseInt(map['Max rows per run'], 10) || 20),
  };
}

/* ------------------------------------------------------------------------ */
/* Helpers                                                                  */
/* ------------------------------------------------------------------------ */

/** Returns the 1-based index of the Notified column, adding it after the last header if needed. */
function ensureNotifiedColumn_(sheet) {
  var lastCol = Math.max(1, sheet.getLastColumn());
  var headers = sheet.getRange(1, 1, 1, lastCol).getValues()[0];
  var index = headers.indexOf(NOTIFIED_HEADER);
  if (index !== -1) return index + 1;

  var col = lastCol + 1;
  sheet.getRange(1, col).setValue(NOTIFIED_HEADER).setFontWeight('bold');
  sheet.getRange(2, col, Math.max(1, sheet.getMaxRows() - 1), 1).setNumberFormat('yyyy-mm-dd hh:mm');
  return col;
}

function buildRecord_(headers, row, config, notifiedCol) {
  var record = [];
  headers.forEach(function (header, i) {
    if (i === notifiedCol - 1 || header === '') return;
    if (config.includeColumns.length && config.includeColumns.indexOf(String(header)) === -1) return;
    record.push({ name: String(header), value: formatValue_(row[i]) });
  });
  return record;
}

function fillTemplate_(template, record, rowNumber) {
  var byName = {};
  record.forEach(function (field) { byName[field.name] = field.value; });
  return template.replace(/\{\{\s*([^}]+?)\s*\}\}/g, function (_, key) {
    if (key === 'row') return String(rowNumber);
    if (key === 'sheet') return SpreadsheetApp.getActiveSpreadsheet().getName();
    return byName.hasOwnProperty(key) ? byName[key] : '';
  });
}

function formatValue_(value) {
  if (value instanceof Date) {
    return Utilities.formatDate(value, Session.getScriptTimeZone(), 'yyyy-MM-dd HH:mm');
  }
  return value === null || value === undefined ? '' : String(value);
}

function isEmptyRow_(row, notifiedCol) {
  return row.every(function (cell, i) { return i === notifiedCol - 1 || cell === ''; });
}

function splitList_(text) {
  return String(text || '')
    .split(',')
    .map(function (s) { return s.trim(); })
    .filter(Boolean);
}

function escapeHtml_(text) {
  return String(text)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
