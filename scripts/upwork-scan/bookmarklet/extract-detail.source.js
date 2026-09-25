/**
 * Run on an open Upwork job detail panel or /jobs/~ page (logged-in main session).
 * Fills G5/G7 and screening fields missing from search tiles.
 */
(function extractUpworkJobDetail() {
  const root = document.querySelector('[data-test="job-details"], main, article') || document.body;
  const text = root.innerText || "";
  const title =
    document.querySelector('[data-test="job-title"], h1')?.textContent?.trim() ||
    document.title.replace(/ - Upwork.*$/i, "").trim();
  const href = location.href;
  const idMatch = href.match(/~([0-9a-f]+)/i);
  const id = idMatch?.[1] || "";
  const activity = text.match(/Interviewing:\s*(\d+)/i);
  const invites = text.match(/Invites sent:\s*(\d+)/i);
  const lastViewed = text.match(/Last viewed by client:\s*([^\n]+)/i);
  const connectsMatch = text.match(/(\d+)\s*Connects?\s*(?:required|to submit|to apply)/i);
  const screening = Array.from(document.querySelectorAll('[data-test="screening-question"], .fe-job-details-screening li'))
    .map((el) => el.innerText?.trim())
    .filter(Boolean);
  const desc =
    document.querySelector('[data-test="job-description-text"], [data-test="Description"]')?.innerText?.trim() || "";
  const job = {
    id,
    title,
    url: href,
    description: desc.slice(0, 8000),
    interviewing: activity ? Number(activity[1]) : null,
    invites_sent: invites ? Number(invites[1]) : null,
    client_last_viewed_raw: lastViewed?.[1]?.trim() || null,
    connects_cost: connectsMatch ? Number(connectsMatch[1]) : null,
    has_screening_questions: screening.length > 0,
    screening_questions: screening,
    payment_verified: /payment verified/i.test(text),
    scraped_at: new Date().toISOString(),
    kind: "upwork-detail",
  };
  const payload = { version: 1, kind: "upwork-detail", jobs: [job] };
  const json = JSON.stringify(payload, null, 2);
  if (typeof copy === "function") copy(json);
  console.log("Detail JSON copied to clipboard.");
  console.log(json);
  return payload;
})();
