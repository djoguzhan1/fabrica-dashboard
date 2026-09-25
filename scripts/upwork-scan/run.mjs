#!/usr/bin/env node
/**
 * Score exported Upwork jobs (Ek E). No Upwork login on server — input from your main-session bookmarklet.
 *
 *   node scripts/upwork-scan/run.mjs path/to/export.json
 *   node scripts/upwork-scan/run.mjs --urls
 *   cat export.json | node scripts/upwork-scan/run.mjs
 */
import { readFileSync } from "node:fs";
import { scoreJob, normalizeTile } from "./lib/score-job.mjs";
import { parsePostedMinutes } from "./lib/parse-age.mjs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
const __dir = dirname(fileURLToPath(import.meta.url));
const searchUrls = JSON.parse(readFileSync(join(__dir, "search-urls.json"), "utf8"));

function loadInput(paths) {
  const byId = new Map();
  for (const p of paths) {
    const raw = readFileSync(p, "utf8");
    const data = JSON.parse(raw);
    const list = data.jobs || (Array.isArray(data) ? data : [data]);
    for (const j of list) {
      const id = j.id || j.url;
      if (!id) continue;
      const prev = byId.get(id) || {};
      byId.set(id, normalizeTile({ ...prev, ...j }));
    }
  }
  return [...byId.values()];
}

function readStdin() {
  return new Promise((resolve) => {
    let buf = "";
    process.stdin.setEncoding("utf8");
    process.stdin.on("data", (c) => (buf += c));
    process.stdin.on("end", () => resolve(buf));
    if (process.stdin.isTTY) resolve("");
  });
}

function printUrls() {
  console.log("# Upwork saved-search URLs (open in YOUR main session)\n");
  for (const row of searchUrls.queries) {
    const u = `${searchUrls.base}?q=${encodeURIComponent(row.q)}&sort=recency`;
    console.log(`## ${row.id} (Tier ${row.tier})\n${u}\n`);
  }
}

function formatRow(r) {
  const age = r.job.posted_minutes ?? parsePostedMinutes(r.job.posted_at);
  const ageStr = age == null ? "?" : `${age}m`;
  return [
    r.result.class.padEnd(4),
    String(r.result.score).padStart(2),
    r.result.template || "-",
    ageStr.padStart(4),
    (r.job.proposals_count || "?").slice(0, 14).padEnd(14),
    r.job.title.slice(0, 52),
    r.job.url,
  ].join(" | ");
}

async function main() {
  const args = process.argv.slice(2);
  if (args.includes("--urls") || args.includes("-u")) {
    printUrls();
    return;
  }

  let jobs = [];
  if (args.length) {
    jobs = loadInput(args.filter((a) => !a.startsWith("-")));
  } else {
    const stdin = await readStdin();
    if (stdin.trim()) {
      const data = JSON.parse(stdin);
      jobs = (data.jobs || []).map(normalizeTile);
    }
  }

  if (!jobs.length) {
    console.error("No jobs in input. Export from Upwork with bookmarklet, then:");
    console.error("  node scripts/upwork-scan/run.mjs ./export.json");
    console.error("  node scripts/upwork-scan/run.mjs --urls");
    process.exit(1);
  }

  const scored = jobs.map((job) => ({
    job,
    result: scoreJob(job),
  }));

  scored.sort((a, b) => {
    const order = { A: 0, B: 1, SKIP: 2 };
    const ca = order[a.result.class] ?? 9;
    const cb = order[b.result.class] ?? 9;
    if (ca !== cb) return ca - cb;
    return b.result.score - a.result.score;
  });

  const aList = scored.filter((s) => s.result.class === "A");
  const bList = scored.filter((s) => s.result.class === "B");
  const skip = scored.filter((s) => s.result.class === "SKIP");

  console.log(`\nScored ${jobs.length} jobs — A: ${aList.length} · B: ${bList.length} · SKIP: ${skip.length}\n`);
  console.log("CLASS | SC | TPL | AGE | PROPOSALS      | TITLE | URL");
  console.log("-".repeat(120));

  for (const s of [...aList, ...bList]) {
    console.log(formatRow(s));
    if (s.result.points?.length) console.log(`      points: ${s.result.points.join(", ")}`);
    if (s.result.verify?.length) console.log(`      VERIFY: ${s.result.verify.join("; ")}`);
    if (s.result.diagnosis) console.log(`      next: ${s.result.diagnosis}`);
  }

  if (skip.length && args.includes("--all")) {
    console.log("\n--- SKIP ---");
    for (const s of skip.slice(0, 30)) {
      console.log(formatRow(s));
      console.log(`      ${s.result.reasons.join("; ")}`);
    }
  }

  const lambda = [...aList, ...bList].reduce((sum, s) => sum + s.result.p, 0);
  console.log(`\nBatch λ (if you applied to all A+B): ${lambda.toFixed(2)}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
