#!/usr/bin/env node
// Usage: node scripts/site_audit.mjs <url> [outDir]
// Needs playwright (npm i playwright) and Chrome; CHROME_PATH overrides the binary.
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';

const url = process.argv[2];
if (!url) { console.error('usage: site_audit.mjs <url> [outDir]'); process.exit(2); }
const outDir = process.argv[3] || 'audit-out';
fs.mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch({
  executablePath: process.env.CHROME_PATH || '/usr/local/bin/google-chrome',
  args: ['--no-sandbox'],
});
const report = { url, viewports: [] };

for (const width of [390, 768, 1366]) {
  const page = await browser.newPage({ viewport: { width, height: 900 } });
  const consoleErrors = [];
  const failedRequests = [];
  page.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text().slice(0, 200)); });
  page.on('requestfailed', r => failedRequests.push(r.url().slice(0, 200)));
  await page.addInitScript(() => {
    window.__lcp = 0;
    new PerformanceObserver(l => { for (const e of l.getEntries()) window.__lcp = e.startTime; })
      .observe({ type: 'largest-contentful-paint', buffered: true });
  });
  const t0 = Date.now();
  try { await page.goto(url, { waitUntil: 'load', timeout: 45000 }); }
  catch (e) { report.viewports.push({ width, error: e.message }); await page.close(); continue; }
  const loadMs = Date.now() - t0;
  await page.waitForTimeout(1500);
  const dom = await page.evaluate(() => {
    const vw = document.documentElement.clientWidth;
    const overflow = [];
    for (const el of document.querySelectorAll('body *')) {
      const r = el.getBoundingClientRect();
      if (r.width && r.right > vw + 2 && getComputedStyle(el).position !== 'fixed') {
        overflow.push(`${el.tagName.toLowerCase()}${el.id ? '#' + el.id : ''}${el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/)[0] : ''} (+${Math.round(r.right - vw)}px)`);
        if (overflow.length >= 10) break;
      }
    }
    const brokenImages = [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.src.slice(0, 200));
    const smallTap = [...document.querySelectorAll('a,button')].filter(e => {
      const r = e.getBoundingClientRect(); return r.width && r.height && (r.height < 24 || r.width < 24);
    }).length;
    return {
      scrollWidth: document.documentElement.scrollWidth, vw, overflow, brokenImages, smallTap,
      lcpMs: Math.round(window.__lcp), title: document.title,
    };
  });
  const shot = path.join(outDir, `shot-${width}.png`);
  await page.screenshot({ path: shot, fullPage: false });
  report.viewports.push({ width, loadMs, ...dom, consoleErrors: consoleErrors.slice(0, 10), failedRequests: failedRequests.slice(0, 10), shot });
  await page.close();
}
await browser.close();

fs.writeFileSync(path.join(outDir, 'report.json'), JSON.stringify(report, null, 2));
for (const v of report.viewports) {
  if (v.error) { console.log(`[${v.width}px] ERROR ${v.error}`); continue; }
  const issues = [];
  if (v.scrollWidth > v.vw + 2) issues.push(`yatay taşma ${v.scrollWidth - v.vw}px: ${v.overflow.slice(0, 3).join(', ')}`);
  if (v.brokenImages.length) issues.push(`${v.brokenImages.length} kırık görsel`);
  if (v.consoleErrors.length) issues.push(`${v.consoleErrors.length} konsol hatası`);
  if (v.failedRequests.length) issues.push(`${v.failedRequests.length} başarısız istek`);
  if (v.lcpMs > 2500) issues.push(`LCP ${v.lcpMs}ms (>2500)`);
  if (v.width === 390 && v.smallTap > 5) issues.push(`${v.smallTap} küçük dokunma hedefi`);
  console.log(`[${v.width}px] load ${v.loadMs}ms, LCP ${v.lcpMs}ms -> ${issues.length ? issues.join(' | ') : 'temiz'}`);
}
console.log(`rapor: ${path.join(outDir, 'report.json')}`);
