// Runs the pure helper functions from Code.gs in Node (node --test).
// Apps Script globals are stubbed just enough for these functions.
const { test } = require('node:test');
const assert = require('node:assert/strict');
// Objects created inside the vm context have their own prototypes, so compare structurally.
const same = (actual, expected) => assert.deepEqual(JSON.parse(JSON.stringify(actual)), expected);
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const context = {
  SpreadsheetApp: { getActiveSpreadsheet: () => ({ getName: () => 'Leads' }) },
  Utilities: { formatDate: (d) => d.toISOString().slice(0, 16).replace('T', ' ') },
  Session: { getScriptTimeZone: () => 'UTC' },
};
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(__dirname, '..', 'Code.gs'), 'utf8'), context);

const record = [
  { name: 'Name', value: 'Ada Lovelace' },
  { name: 'Email', value: 'ada@example.com' },
  { name: 'Message', value: 'Hello <world> & friends' },
];

test('fillTemplate_ replaces headers, row and sheet placeholders', () => {
  const out = context.fillTemplate_('New: {{ Name }} <{{Email}}> row {{row}} in {{sheet}} {{Missing}}', record, 7);
  assert.equal(out, 'New: Ada Lovelace <ada@example.com> row 7 in Leads ');
});

test('splitList_ trims and drops empties', () => {
  same(context.splitList_(' a@x.com, b@y.com ,, '), ['a@x.com', 'b@y.com']);
  same(context.splitList_(''), []);
});

test('isEmptyRow_ ignores the Notified column', () => {
  assert.equal(context.isEmptyRow_(['', '', 'ERROR: x'], 3), true);
  assert.equal(context.isEmptyRow_(['', 'x', ''], 3), false);
});

test('buildRecord_ skips Notified, blank headers and non-included columns', () => {
  const headers = ['Name', '', 'Email', 'Notified'];
  const row = ['Ada', 'ignored', 'ada@example.com', ''];
  same(context.buildRecord_(headers, row, { includeColumns: [] }, 4), [
    { name: 'Name', value: 'Ada' },
    { name: 'Email', value: 'ada@example.com' },
  ]);
  same(context.buildRecord_(headers, row, { includeColumns: ['Email'] }, 4), [
    { name: 'Email', value: 'ada@example.com' },
  ]);
});

test('formatValue_ renders dates and nulls', () => {
  const date = vm.runInContext("new Date('2026-03-14T09:30:00Z')", context);
  assert.equal(context.formatValue_(date), '2026-03-14 09:30');
  assert.equal(context.formatValue_(null), '');
  assert.equal(context.formatValue_(42), '42');
});

test('emailHtml_ escapes user content', () => {
  const html = context.emailHtml_('Subject <b>', record, 'https://docs.google.com/x');
  assert.ok(html.includes('Subject &lt;b&gt;'));
  assert.ok(html.includes('Hello &lt;world&gt; &amp; friends'));
  assert.ok(!html.includes('<world>'));
});

test('slackPayload_ keeps fields within block limits', () => {
  const many = Array.from({ length: 23 }, (_, i) => ({ name: 'F' + i, value: String(i) }));
  const payload = context.slackPayload_('S', many, 'https://x');
  const sections = payload.blocks.filter((b) => b.type === 'section');
  assert.equal(sections.length, 1); // record is capped at 10 fields
  assert.equal(sections[0].fields.length, 10);
  assert.equal(payload.blocks[0].type, 'header');
  assert.equal(payload.text, 'S');
});
