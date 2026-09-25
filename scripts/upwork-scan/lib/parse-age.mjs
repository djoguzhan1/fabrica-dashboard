/**
 * Parse Upwork "posted" strings to minutes since publish.
 * Examples: "5 minutes ago", "1 hour ago", "Yesterday", "2 days ago"
 */
export function parsePostedMinutes(text) {
  if (!text) return null;
  const t = text.toLowerCase().trim();
  const m = t.match(/(\d+)\s*minute/);
  if (m) return Number(m[1]);
  const h = t.match(/(\d+)\s*hour/);
  if (h) return Number(h[1]) * 60;
  if (t.includes("just now") || t === "now") return 0;
  if (t.includes("yesterday")) return 24 * 60;
  const d = t.match(/(\d+)\s*day/);
  if (d) return Number(d[1]) * 24 * 60;
  const w = t.match(/(\d+)\s*week/);
  if (w) return Number(w[1]) * 7 * 24 * 60;
  return null;
}

export function parseProposalsMax(text) {
  if (!text) return null;
  const t = text.toLowerCase();
  if (t.includes("less than 5") || t.includes("< 5")) return 4;
  if (t.includes("5 to 10")) return 10;
  if (t.includes("10 to 15")) return 15;
  if (t.includes("15 to 20")) return 20;
  if (t.includes("20 to 50")) return 50;
  const n = t.match(/(\d+)\s*proposals?/);
  if (n) return Number(n[1]);
  return null;
}

export function parseBudgetUsd(text) {
  if (!text) return { min: null, max: null, hourly: false };
  const raw = text.replace(/,/g, "");
  const hourly = /\/hr|hourly/i.test(raw);
  const range = raw.match(/\$?\s*(\d+(?:\.\d+)?)\s*[-–]\s*\$?\s*(\d+(?:\.\d+)?)/);
  if (range) return { min: Number(range[1]), max: Number(range[2]), hourly };
  const single = raw.match(/\$?\s*(\d+(?:\.\d+)?)/);
  if (single) {
    const v = Number(single[1]);
    return { min: v, max: v, hourly };
  }
  return { min: null, max: null, hourly };
}
