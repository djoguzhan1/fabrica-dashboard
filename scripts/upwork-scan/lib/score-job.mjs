import { parseBudgetUsd, parsePostedMinutes, parseProposalsMax } from "./parse-age.mjs";

const BLACKLIST_RE =
  /\b(react|next\.?js|vue\.?js|angular|shopify\s+theme|mobile\s+app|ios\s+app|android\s+app|full[\s-]?stack\s+saas|woocommerce\s+(payment|checkout|store)|monthly\s+seo|seo\s+retainer|long[\s-]?term\s+team|full[\s-]?time\s+(developer|engineer)|ongoing\s+monthly|free\s+test|trial\s+task|pay\s+outside|whatsapp|telegram)\b/i;

const TIER1_RE =
  /\b(wordpress|elementor|pagespeed|page\s*speed|core\s+web\s+vitals|gtmetrix|lighthouse|white\s+screen|critical\s+error|plugin\s+conflict|contact\s+form|mobile\s+friendly|responsive|landing\s+page|one[\s-]?page|hvac|plumbing|plumber|roofing|electrician|contractor|home\s+services|small\s+business\s+website|speed\s+optim)/i;

const TIER2_RE =
  /\b(google\s+sheets|excel|spreadsheet|vlookup|xlookup|pivot|dashboard|figma|psd|html\s*\/\s*css|quick\s+fix|small\s+change|migrate|setup|install)\b/i;

const URL_RE = /https?:\/\/[^\s<>"']+/i;

export function detectTier(title, description) {
  const blob = `${title} ${description}`;
  const t1 = TIER1_RE.test(blob);
  const t2 = TIER2_RE.test(blob);
  if (t1) return 1;
  if (t2) return 2;
  return 0;
}

function scopeOneSentence(description) {
  if (!description) return false;
  const s = description.trim();
  if (s.length < 20) return false;
  if (s.length > 1200) return false;
  const sentences = s.split(/[.!?]\s+/).filter(Boolean);
  return sentences.length <= 8;
}

/**
 * @param {object} job - normalized job from bookmarklet or detail export
 * @returns scoring result
 */
export function scoreJob(job) {
  const title = job.title || "";
  const description = job.description || job.description_snippet || "";
  const blob = `${title} ${description}`;
  const tier = detectTier(title, description);
  const ageMin = job.posted_minutes ?? parsePostedMinutes(job.posted_at);
  const proposalsMax = job.proposals_max ?? parseProposalsMax(job.proposals_count || job.proposals);
  const budget = parseBudgetUsd(job.budget || job.job_type || "");
  const connects = job.connects_cost ?? job.connects ?? null;
  const paymentVerified = job.payment_verified !== false;
  const invites = job.invites_sent ?? job.invites ?? null;
  const interviewing = job.interviewing ?? null;
  const hireRate = job.client_hire_rate ?? null;
  const clientHires = job.client_hires ?? job.client_jobs_posted ?? null;
  const spent = job.client_spent_usd ?? null;
  const location = (job.client_location || "").toUpperCase();
  const experience = (job.experience_level || "").toLowerCase();
  const isFixed = /fixed/i.test(job.job_type || job.budget || "") || job.is_fixed === true;
  const hasUrl = URL_RE.test(blob) || Boolean(job.site_url);
  const hasScreening = Boolean(job.has_screening_questions) || (job.screening_questions?.length > 0);
  const lastViewedMin = job.client_last_viewed_minutes ?? null;

  const gates = [];
  const fail = (id, reason) => gates.push({ id, pass: false, reason });

  if (tier === 0) fail("G1", "Not Tier-1/2 whitelist");
  if (!paymentVerified) fail("G2", "Payment not verified");
  if (ageMin == null) gates.push({ id: "G3", pass: "verify", reason: "Posted time unknown — open job detail" });
  else {
    const tier1Fresh = tier === 1 && proposalsMax != null && proposalsMax < 5;
    const maxAge = tier1Fresh ? 45 : 15;
    if (ageMin > maxAge) fail("G3", `Job age ${ageMin}m > ${maxAge}m cap`);
  }
  if (proposalsMax != null && proposalsMax >= 10) fail("G4", `Proposals tier ≥10 (${job.proposals_count})`);
  if (invites != null && invites > 0) fail("G5", "Invites already sent");
  if (interviewing != null && interviewing > 0) fail("G5", "Interviewing in progress");
  if (BLACKLIST_RE.test(blob)) fail("G1b", "Blacklist keyword");
  if (!scopeOneSentence(description)) fail("G8", "Scope not clear in snippet — verify on detail");

  const introMax = tier === 1 ? 800 : 150;
  const introMin = tier === 1 ? 30 : 20;
  const budgetMax = budget.max ?? budget.min;
  if (budgetMax != null && budgetMax < introMin && !(clientHires === 0 && budgetMax < 20)) {
    fail("G6", `Budget below floor ($${budgetMax})`);
  }
  if (budgetMax != null && budgetMax > introMax) fail("G6", `Budget above sprint cap ($${budgetMax})`);

  if (connects != null && connects > 8) fail("G7", `Connects cost ${connects} > 8`);

  const hardFails = gates.filter((g) => g.pass === false);
  if (hardFails.length) {
    return {
      class: "SKIP",
      score: 0,
      tier,
      gates,
      reasons: hardFails.map((g) => `${g.id}: ${g.reason}`),
      template: null,
      p: 0,
    };
  }

  let score = 0;
  const points = [];

  if (ageMin != null && ageMin < 5) {
    score += 3;
    points.push("+3 <5m");
  }
  if (proposalsMax != null && proposalsMax < 5) {
    score += 2;
    points.push("+2 <5 proposals");
  }
  if (clientHires != null && clientHires >= 1 && hireRate != null && hireRate >= 50) {
    score += 2;
    points.push("+2 established client");
  } else if (clientHires != null && clientHires >= 1) {
    score += 1;
    points.push("+1 client has hires");
  }
  if (hasUrl) {
    score += 2;
    points.push("+2 site URL");
  }
  if (lastViewedMin != null && lastViewedMin <= 60) {
    score += 2;
    points.push("+2 client viewed ≤1h");
  }
  if (spent != null && spent >= 500) {
    score += 1;
    points.push("+1 spent ≥$500");
  }
  if (/^(US|UNITED STATES|UK|UNITED KINGDOM|CANADA|AUSTRALIA)/.test(location) || /\b(USA|U\.S\.)\b/.test(location)) {
    score += 1;
    points.push("+1 US/UK/CA/AU");
  }
  if (hasScreening) {
    score += 1;
    points.push("+1 screening Q");
  }
  if (/\b(urgent|asap|today|this week)\b/i.test(blob)) {
    score += 1;
    points.push("+1 urgent");
  }
  if (isFixed || /fixed/i.test(job.job_type || "")) {
    score += 1;
    points.push("+1 fixed price");
  }
  if (connects != null && connects <= 6) {
    score += 1;
    points.push("+1 connects ≤6");
  }
  if (experience.includes("expert")) {
    score -= 2;
    points.push("-2 expert");
  }
  if (clientHires != null && clientHires >= 10 && hireRate != null && hireRate < 30) {
    score -= 2;
    points.push("-2 low hire rate");
  }
  if (/\b(long[\s-]?term|ongoing|full[\s-]?time|team member)\b/i.test(blob)) {
    score -= 1;
    points.push("-1 long-term");
  }

  let klass = "C";
  let p = 0.02;
  if (score >= 10) {
    klass = "A";
    p = 0.055;
  } else if (score >= 6) {
    klass = "B";
    p = 0.035;
  }

  const template =
    tier === 1
      ? /\b(landing|one[\s-]?page|hvac|plumbing|contractor)\b/i.test(blob)
        ? /\b(3\s*page|three\s*page|redesign|multiple)\b/i.test(blob)
          ? "T3"
          : "T2"
        : "T1"
      : /\b(sheet|excel|spreadsheet|vlookup|xlookup)\b/i.test(blob)
        ? "S4"
        : "S5";

  const verify = gates.filter((g) => g.pass === "verify").map((g) => g.reason);

  return {
    class: klass === "C" ? "SKIP" : klass,
    score,
    tier,
    points,
    gates,
    verify,
    reasons: klass === "C" ? [`Score ${score} < 6 (B threshold)`] : [],
    template,
    p,
    diagnosis: hasUrl ? "PSI + mobile check before send" : "Micro-plan opener",
  };
}

export function normalizeTile(raw) {
  return {
    id: raw.id,
    title: raw.title,
    url: raw.url,
    budget: raw.budget,
    job_type: raw.job_type,
    experience_level: raw.experience_level,
    posted_at: raw.posted_at,
    posted_minutes: raw.posted_minutes,
    description_snippet: raw.description_snippet || raw.description,
    proposals_count: raw.proposals_count,
    client_location: raw.client_location,
    payment_verified: raw.payment_verified,
    connects_cost: raw.connects_cost,
    source_query: raw.source_query,
    scraped_at: raw.scraped_at || new Date().toISOString(),
  };
}
