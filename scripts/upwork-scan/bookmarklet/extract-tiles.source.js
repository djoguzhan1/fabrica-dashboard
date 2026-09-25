/**
 * Run in the browser console on YOUR logged-in Upwork job search page.
 * Same session only — no second account, no automation login.
 *
 * Usage: paste full file, or use the one-liner from docs/upwork-live-scan-workflow.md
 */
(function extractUpworkJobTiles() {
  const cards = document.querySelectorAll('article[data-test="JobTile"]');
  const scrapedAt = new Date().toISOString();
  const jobs = Array.from(cards).map((card) => {
    const titleEl = card.querySelector(
      '[data-test="job-tile-title-link"], [data-test="job-tile-title-link UpLink"], h2 a, h3 a'
    );
    const title = titleEl?.textContent?.trim() ?? "";
    const href = titleEl?.getAttribute("href") ?? "";
    const url = href.startsWith("http") ? href : `https://www.upwork.com${href}`;
    const idMatch = href.match(/~([0-9a-f]+)/i);
    const id = idMatch?.[1] ?? "";
    const descEl = card.querySelector(
      '[data-test="UpCLineClamp JobDescription"], [data-test="job-description-text"], p'
    );
    const paymentText = card.innerText || "";
    const payment_verified = /payment verified/i.test(paymentText);
    return {
      id,
      title,
      url,
      budget:
        card.querySelector('[data-test="budget"]')?.innerText?.trim() ||
        card.querySelector('[data-test="job-type-label"]')?.innerText?.trim() ||
        "",
      job_type: card.querySelector('[data-test="job-type-label"]')?.innerText?.trim() || "",
      experience_level: card.querySelector('[data-test="experience-level"]')?.innerText?.trim() || "",
      posted_at: card.querySelector('[data-test="job-pubilshed-date"], [data-test="posted-on"]')?.innerText?.trim() || "",
      description_snippet: (descEl?.innerText?.trim() || "").slice(0, 500),
      proposals_count: card.querySelector('[data-test="proposals-tier"]')?.innerText?.trim() || "",
      client_location: card.querySelector('[data-test="location"]')?.innerText?.trim() || "",
      payment_verified,
      scraped_at: scrapedAt,
      source_query: new URLSearchParams(location.search).get("q") || document.title,
    };
  });
  const payload = { version: 1, kind: "upwork-tiles", scraped_at: scrapedAt, jobs };
  const json = JSON.stringify(payload, null, 2);
  if (typeof copy === "function") copy(json);
  console.log(`Extracted ${jobs.length} jobs. JSON copied to clipboard.`);
  console.log(json);
  return payload;
})();
