# CLAUDE.md — AIToolGrade.com
> Read this file before every task.

## Project Location
`~/Desktop/ClaudeWork/aitoolgrade/`

## Hosting & Deploy
- **Domain:** AIToolGrade.com (registered on Namecheap)
- **Host:** Hostinger
- **Nameservers:** `nova.dns-parking.com` / `cosmos.dns-parking.com`
- **GitHub repo:** github.com/richn33-sys/aitoolgrade
- **SSH:** `ssh -p 65002 u877849432@145.79.4.163`
- **Deploy command (run on server after push):**
  ```bash
  cd ~/domains/aitoolgrade.com/public_html && git fetch origin && git reset --hard origin/main
  ```
- **Full deploy workflow:**
  1. Make changes locally
  2. `git add . && git commit -m "message" && git push`
  3. SSH in and run deploy command above
- **Note:** Hostinger auto-deploy via webhook is unreliable — always use SSH force pull

## What This Project Does
An AI tools review and affiliate website. Independent reviews, ratings, category pages, comparisons, and a blog. Monetized via affiliate links (not yet live — waiting for traffic). No CMS — pure HTML/CSS files.

## File Structure
```
/                        ← root
├── index.html           ← homepage
├── reviews.html         ← reviews index
├── compare.html         ← comparison page with working JS category filters
├── favicon.svg / .png   ← favicon on all pages
├── robots.txt
├── sitemap.xml          ← submitted to Google Search Console
├── nav.js               ← shared nav (single source of truth — see Site Architecture)
├── review/              ← 30 individual tool review pages
│   ├── jasper.html              (AI Writing, 8.2)
│   ├── copyai.html              (AI Writing, 7.3)
│   ├── writesonic.html          (AI Writing, 8.0)
│   ├── grammarly.html           (AI Writing, 8.5)
│   ├── cursor.html              (AI Coding, 9.4)
│   ├── github-copilot.html      (AI Coding, 8.9)
│   ├── windsurf.html            (AI Coding, 8.2)
│   ├── bolt.html                (AI Coding, 8.3)
│   ├── replit.html              (AI Coding, 8.3)
│   ├── lovable.html             (AI Coding, 8.1)
│   ├── google-antigravity.html  (AI Coding, 7.5)
│   ├── deepseek-v4.html         (AI Coding, 8.1)
│   ├── claude-code.html         (AI Coding, 8.0)
│   ├── kimi-code.html           (AI Coding, 7.8)
│   ├── grok-build.html          (AI Coding, 6.7)
│   ├── midjourney.html          (AI Image, 7.8)
│   ├── adobe-firefly.html       (AI Image, 8.7)
│   ├── leonardo-ai.html         (AI Image, 8.7)
│   ├── zapier.html              (Automation, 8.1)
│   ├── n8n.html                 (Automation, 8.3)
│   ├── microsoft-agent-365.html (Automation, 7.1)
│   ├── runway.html              (AI Video, 8.9)
│   ├── synthesia.html           (AI Video, 8.0)
│   ├── heygen.html              (AI Video, 8.1)
│   ├── descript.html            (AI Video, 7.9)
│   ├── chatgpt.html             (Productivity, 9.0)
│   ├── notion-ai.html           (Productivity, 8.6)
│   ├── perplexity.html          (Productivity, 8.8)
│   ├── claude-cowork.html       (Productivity, 8.2)
│   ├── perplexity-computer.html (Productivity, 7.4)
│   └── notebooklm.html          (Productivity, 8.7)
├── category/            ← 6 category listing pages
│   ├── writing.html
│   ├── coding.html
│   ├── image.html
│   ├── automation.html
│   ├── video.html
│   └── productivity.html
└── blog/              ← 12 blog posts + index
    ├── index.html
    ├── cursor-vs-windsurf-vs-github-copilot.html
    ├── best-free-ai-tools-2026.html
    ├── best-ai-tools-for-seo-2026.html
    ├── chatgpt-vs-claude-vs-perplexity.html
    ├── how-to-automate-business-with-n8n.html
    ├── cursor-pricing-2026.html
    ├── notion-ai-pricing-2026.html
    ├── best-ai-agents-non-developers-2026.html
    ├── best-ai-app-builders-2026.html
    ├── best-ai-coding-agents-2026.html
    ├── chatgpt-go-vs-plus-2026.html
    └── chatgpt-pro-100-vs-200-2026.html
```
> Root also has: about.html, resources.html, how-we-review.html, contribute.html, contact.html,
> advertise.html, and legal pages (see "Missing File Structure Details"). author/ holds
> marcus-veil.html and priya-nolan.html. Full HTML page count: 67.

## Category Review Counts (homepage displays these — keep in sync)
- AI Writing: 4 (Jasper, Copy.ai, Writesonic, Grammarly)
- AI Coding: 11 (Cursor, GitHub Copilot, Windsurf, Bolt.new, Replit, Lovable, Google Antigravity, DeepSeek V4, Claude Code, Kimi Code, Grok Build)
- AI Image: 3 (Midjourney, Adobe Firefly, Leonardo AI)
- Automation: 3 (Zapier, n8n, Microsoft Agent 365)
- AI Video: 4 (Runway, Synthesia, HeyGen, Descript)
- Productivity: 6 (ChatGPT, Notion AI, Perplexity, Claude Cowork, Perplexity Computer, NotebookLM)

Total: 31 reviews. Homepage `cat-count` values in index.html match these (AI Coding is 11 as of
June 7, 2026 after adding Grok Build; Productivity is 6 after NotebookLM; Automation is 3).

When adding a new review, update the count in `index.html` using this script pattern:
```bash
python3 << 'EOF'
content = open('index.html').read()
content = content.replace('<div class="cat-count">3 tools reviewed</div>', '<div class="cat-count">4 tools reviewed</div>')
open('index.html','w').write(content)
EOF
```

## Design System (CSS Variables)
All pages share these variables — never hardcode colors:
```css
--bg: #fafaf8          /* page background */
--bg2: #f3f2ee         /* section/card background */
--bg3: #eceae3         /* deeper background */
--text: #1a1a18        /* primary text */
--text2: #4a4a45       /* secondary text */
--text3: #8a8a82       /* muted/meta text */
--accent: #e85d26      /* brand orange — CTAs, links, scores */
--accent2: #f07d4a     /* accent hover state */
--accent-dim: rgba(232,93,38,0.08)
--border: #e2e0d8      /* borders */
--white: #ffffff
```

## Typography
```css
--display: 'Playfair Display', serif   /* headings, logo, scores */
--sans: 'DM Sans', sans-serif          /* body text */
--mono: 'DM Mono', monospace           /* labels, badges, ratings */
```
Google Fonts link (include in every page head):
```html
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
```

## Site Positioning
The site is positioned as a research-based resource, NOT a hands-on testing site. Never claim personal hands-on testing, 30-day trials, or first-person use. Instead frame everything as: verified pricing, documented features, primary source research, community sentiment analysis, and structured scoring. The methodology page at how-we-review.html explains this fully — all content must be consistent with it.

## Tone Rules — Prohibited Language
Never use the following hyperbolic or promotional language anywhere on the site:
- "game changer" / "game-changer"
- "must-try" / "must try"
- "no-brainer"
- "fundamentally changes"
- "genuinely transformative" / "genuinely exceptional" / "genuinely impressive"
- "changes everything"
- "revolutionary"
- "unmatched" (unless a specific, verifiable claim)
- "outstanding" as a verdict label

Use instead: measured, specific, comparative language grounded in documented capabilities. Strong evaluative claims are fine — promotional phrasing is not. The goal is authoritative, not enthusiastic.

## Writing Style
All content (reviews, blog posts, any copy) must be humanized — not AI-sounding. Vary sentence lengths, use natural phrasing, improve transitions, make it feel organic and authentic. No fluff, no generic AI sentence structures. Short punchy sentences mixed with longer ones. Write like a knowledgeable person, not a content generator.

As a final step in any writing task, humanize the text so it does not feel AI-generated. Vary sentence length, add natural phrasing, improve transitions, and make it feel organic and authentic — without adding fluff or changing the message.

## Key UI Patterns
- **Scores:** displayed as `★ 9.4 / 10` using `var(--mono)` font, `var(--accent)` color
- **Free badge:** `<span class="free-badge">FREE</span>` — green pill badge
- **Nav:** sticky, frosted glass (`backdrop-filter: blur(12px)`), dropdown menus on hover
- **Cards:** white bg, `var(--border)` border, 14px border-radius, lift on hover (`translateY(-2px)` + box-shadow)
- **Section label:** small all-caps mono text in accent color above headings
- **Footer:** 4-column grid (brand desc + 3 link columns) + bottom bar with copyright + affiliate disclosure

## Nav Structure (current — defined once in nav.js; see Site Architecture)
> As of May 30, 2026 the nav is rendered from `nav.js` (single source of truth). Do NOT
> edit nav markup per-page — edit `nav.js` only and it updates all 61 pages. The structure
> below documents what nav.js renders.
```
Categories ▾         Reviews ▾            Compare    Blog    Get Updates
  AI Writing           Jasper AI
  AI Coding            Copy.ai
  AI Image             Cursor
  Automation           ChatGPT
  AI Video             Writesonic
  Productivity         GitHub Copilot
                       Windsurf
                       Bolt.new
                       Claude Code
                       DeepSeek V4
                       Kimi Code
                       Zapier
                       n8n
                       Midjourney
                       Adobe Firefly
                       Leonardo AI
                       Runway
                       Synthesia
                       HeyGen
                       Notion AI
                       Perplexity AI
                       Perplexity Computer
                       NotebookLM
                       Grammarly
                       Replit
                       Claude Cowork
```

### Nav & logo href patterns by file location
Nav and logo links are now generated by `nav.js` via server-relative depth detection — you no
longer hand-write these per page. The patterns below still apply to **non-nav links** authored
directly in page content (breadcrumbs, in-body links, footer links):
- Root files (`index.html`, `reviews.html`, etc): `href="review/jasper.html"`, `href="compare.html"`, `href="blog/index.html"`
- Sub files (`review/`, `category/`): `href="../review/jasper.html"`, `href="../compare.html"`, `href="../blog/index.html"`
- Blog posts (`blog/`): `href="../../review/jasper.html"`, `href="../../compare.html"`
- Logo link resolves to the homepage at the correct depth (`index.html` / `../index.html` / `../../index.html`) — handled automatically by nav.js.
- Reminder: nav.js depth detection is server-relative — test via an HTTP server, not `file://`.

## Coding Conventions
- **No JavaScript frameworks** — vanilla HTML/CSS only
- **No external CSS files** — all styles are inline `<style>` blocks in each HTML file
- **No separate JS files** — any JS is inline `<script>` at bottom of body. **Exception:** `nav.js` (project root) is a shared external script that renders the nav on all pages (see Site Architecture, implemented May 30, 2026).
- **Self-contained pages** — each page has its own styles and footer. **Exception:** the nav is no longer hardcoded per page — it is injected by `nav.js`.
- Mobile breakpoint at `768px` — always include responsive styles
- Breadcrumbs on all non-homepage pages: `Home › Category › Page Name`

## Do NOT Touch Without Asking
- CSS variable names — changing them breaks all pages
- Nav link structure — edit `nav.js` only (single source of truth); never hand-edit nav markup per page
- Footer affiliate disclosure link — legally required on every page
- Score ratings — don't change published scores without a reason
- Google Search Console verification meta tag in `index.html`: `l6ZuoKnWQSEezpQ3liP8-QwvV045Q2LQLML-ryisN0o`

## Adding a New Review Page
1. Use an existing review page as template (e.g. `review/cursor.html`)
2. Update: title, meta description, tool name, score, pros/cons, affiliate link
3. Add to nav dropdown — edit `nav.js` only (one line; updates all 61 pages)
4. Add a card to the relevant `category/` page
5. Add a card to `reviews.html`
6. Add a row to `compare.html`
7. Update homepage category count in `index.html`
8. Add URL to `sitemap.xml`
9. Run prohibited language check — grep the full list (zero results before deploy)
10. Push and SSH deploy
- [ ] Editorial sanity check — paste this into Perplexity after deploy:
  "Review [LIVE URL] for promotional language, unsupported claims, and anything that reads more like marketing than research-based analysis. Flag specific phrases that should be qualified or removed."
  Fix any flagged issues with a quick Claude Code prompt before promoting on social.

## Editorial Quality Control

### Perplexity editorial review (implemented June 3, 2026)
After publishing any review, paste the URL into Perplexity and ask:
"What promotional language or unsupported claims appear in this review?"

Issues found and fixed June 3, 2026:
- HeyGen review: "hard to tell you're not watching filmed video" → sourced G2 attribution
- HeyGen review: "most convincing AI avatar widely available" → "highest-rated on G2 among platforms we reviewed"
- NotebookLM review: "no hallucination" → "dramatically reduces hallucination risk" (3 instances)

Pattern to watch: superlative claims without source attribution, absolute statements about AI capabilities (especially "eliminates" or "no" anything)

The Perplexity editorial check is now a standard step on all new reviews per the checklist.
Reviews checked this session (June 5-6, 2026): Kimi Code (fixes applied), Bolt.new (pending check), Adobe Firefly (pending check).

### Prohibited language grep (existing)
Run before every deploy: grep for full prohibited language list per CLAUDE.md

## Updating Nav (nav.js — single source of truth)
> Superseded May 30, 2026. The old per-page Python find-and-replace pattern is no longer used —
> all 61 pages now load nav markup from `nav.js`, so there is no per-page nav HTML to rewrite.

To change the nav:
1. Edit `nav.js` (project root) only — add/remove a review or category entry (one line).
2. The change propagates to all 61 pages automatically; no per-page edits.
3. Test via an HTTP server (depth detection is server-relative — `file://` will not resolve paths correctly).
4. Commit, push, and SSH deploy as usual.

## SEO Conventions
- Title format: `[Tool Name] Review 2026 — [Hook] | AIToolGrade`
- Category title format: `Best [Category] Tools 2026 | AIToolGrade`
- Blog title format: `[Topic] — [Hook] | AIToolGrade`
- Always include `<meta name="description">` — keep under 160 chars
- Google Search Console verified — sitemap submitted and fetching successfully
- Several pages already indexed by Google as of April 2026

## Monetization Status
- Affiliate links: NOT YET ADDED — waiting for traffic to build first
- When adding: use `target="_blank" rel="noopener"` on all affiliate links
- Affiliate disclosure in footer on every page (legally required)
- Display ads: planned but not implemented
- Company name for legal pages: NashMart, LLC

## What to Build Next
- More review pages (priority: AI coding tools, more productivity)
- More blog posts (comparisons and best-of lists perform best for SEO)
- Affiliate links once traffic starts coming in
- Email newsletter backend (signup form exists on homepage)
- Display ad slots

## Long-Term SEO Strategy

### Google Ranking Systems That Matter Most for This Site
1. **Helpful Content System** — every content decision should ask: does this genuinely help someone decide whether to use this tool? Not just rank for a keyword.
2. **Reviews System** — rewards insightful analysis, original research, and evidence of expertise. Screenshots, specific observations, and methodology transparency directly feed this system.
3. **Link Analysis / PageRank** — quality inbound links from relevant sources are required to break through on competitive queries. Content quality alone is not enough.

### Near-Term Priorities (Content and Credibility)
- ~~Add screenshots to Tier 1 review pages: Cursor, Grammarly, Perplexity, Jasper~~ ✅ done (May 31, 2026) — all Tier 1 reviews now embed their pricing screenshot. Jasper now references `img/reviews/jasper-pricing.jpg` (replaced a non-standard `images/reviews/jasper/pricing.png` path; orphaned file removed)
- Add a methodology callout box at the top of each review page linking to how-we-review.html
- Keep adding reviews and blog posts to build topical depth

### Medium-Term Priorities (Authority Building)
- Contributor bylines from people with existing web presence = author entity signals
- Outreach for mentions and links from AI tools communities, newsletters, and roundups
- Guest posts or contributions on other sites under Rich's name pointing back to AIToolGrade
- Rich's 20 years of SEO experience = relationships to leverage for link building

### Longer-Term Priorities (Topical Authority)
- Build topic clusters: each category needs a pillar page, multiple reviews, and supporting blog content all interlinked
- Deep blog posts (2,000+ words) on comparison and best-of topics earn the most backlinks
- Quality links over quantity — one link from a respected AI newsletter beats ten from directories
- Brand signals matter: direct traffic, branded searches, and return visits all feed ranking confidence

### Content Quality Standard
Every piece of content should be good enough that a reader would share it or link to it naturally. That is what creates the content quality gap that earns links over time.

## Social Media Accounts

### Brand Account
- **X/Twitter:** @aitoolgrade
- **Email:** aitoolgrade@proton.me
- **Bio:** "The most thorough AI tools research on the web. Verified pricing · Documented features · Honest ratings"

### Marcus Veil
- **X/Twitter:** @marcusveil_
- **Email:** marcusveil33@proton.me
- **Author page:** aitoolgrade.com/author/marcus-veil.html
- **Content focus:** Trend analysis, industry shifts, tool comparisons
- **Voice:** Direct, analytical, skeptical-but-fair, no padding

### Priya Nolan
- **X/Twitter:** @priyanolan
- **Email:** priyanolan@proton.me
- **Author page:** aitoolgrade.com/author/priya-nolan.html
- **Content focus:** AI for everyday professionals, how-to guides, accessible explainers
- **Voice:** Warm, approachable, encouraging, plain-language

### Social Strategy
- Post 1x per day per account during establishment phase — do NOT automate yet
- Marcus and Priya cross-tag @aitoolgrade in posts
- Brand account cross-posts every new article
- Space posts out — do not post all at once
- Automation via n8n + Claude Code Chrome DevTools MCP planned once accounts are established

### Article Attribution
- Marcus writes: trend analysis, comparisons, industry takes, coding/automation tools
- Priya writes: how-to guides, beginner-friendly content, writing/productivity tools
- Rich Nashawaty: listed as Founder & Editor on About page only — does not write articles

## X/Twitter Content Strategy

### Accounts
- @AIToolGrade — brand account, 3-4x per week
- @marcusveil_ — Marcus persona, 2-3x per week
- @priyanolan — Priya persona, 2-3x per week

### Post Types by Account

**@AIToolGrade** (brand voice — authoritative, data-driven)
- Score highlights — share a score with the specific reasoning behind it
- Community sentiment — what Reddit/G2 users actually say about a tool
- Pricing alerts — changes, comparisons, value callouts
- Stat callouts — surprising numbers from reviews
- Month wrap — end of month roundup

**@marcusveil_** (analytical, direct, skeptical)
- Industry takes — competitive dynamics, company behavior, market shifts
- Head-to-head comparisons — clear winner with specific reasoning
- Pricing alerts — value analysis for developers and power users

**@priyanolan** (warm, accessible, encouraging)
- How-to posts — practical starting points and tool stacks
- Myth busts — challenge fear and misinformation around AI tools
- Beginner guides — entry-point recommendations with free tiers first
- Personal takes — first-person voice, counterintuitive results

### Content Rules
- Every post must link back to a specific review or aitoolgrade.com
- No prohibited language (game changer, revolutionary, unmatched, etc.)
- Posts are single tweets under 280 characters — not threads
- 1-2 hashtags max: #AITools #Productivity (use sparingly)
- Rest days: Day 6, 13, 20, 27 of each 30-day cycle

### 30-Day Calendar
A full 30-day content calendar exists at:
~/Desktop/ClaudeWork/aitoolgrade/x-calendar-30day.md

After Day 30, rotate back to Day 1 — posts are evergreen.
Update stats and community sentiment pulls using the Sunday research brief.

### Generating New Posts
When new content is published, generate posts for all three accounts:
1. @AIToolGrade: score + one specific insight + link
2. @marcusveil_ (if tech/coding/automation tool): analytical angle + link
3. @priyanolan (if writing/productivity tool): practical angle + link
Both personas post on every review — just from different angles.

## Schema Markup
All schema is implemented as JSON-LD in the <head> of each page. Do not add duplicate schema when updating pages.

### Implemented
- **Organization schema** — index.html (entity signal for Google)
- **Review schema** — all 26 review pages (eligible for star ratings in SERPs)
  - Includes: reviewRating, author, itemReviewed with applicationCategory + operatingSystem + offers
- **Article schema** — all 12 blog posts (eligible for article rich results)
  - Includes: headline, author (Person), publisher (Organization), datePublished, dateModified
- **BreadcrumbList schema** — all review and blog pages

### When adding a new review page
Add Review schema with these required fields:
- reviewRating (ratingValue, bestRating: 10, worstRating: 0)
- author (Organization — AIToolGrade)
- itemReviewed (SoftwareApplication with applicationCategory + operatingSystem + offers)
- datePublished and dateModified

### When adding a new blog post
Add Article schema with these required fields:
- headline
- author (Person — Marcus Veil or Priya Nolan with url to their author page)
- publisher (Organization — AIToolGrade)
- datePublished and dateModified

### Validation
Test any page at search.google.com/test/rich-results to confirm schema is valid.

## New Review Page Template Prompt
Use this prompt in Claude Code to build and deploy a new review page end-to-end.
Replace [TOOL NAME], [CATEGORY], [AUTHOR], and [SCORE] with the correct values.

Categories: AI Writing / AI Coding / AI Image / Automation / AI Video / Productivity
Authors: Marcus Veil (trend/technical tools) / Priya Nolan (writing/productivity tools)

PROMPT TEMPLATE (copy from here):

[TOOL NAME] review page fully built and deployed on AIToolGrade.com

CONTEXT
- Project: AIToolGrade.com - read CLAUDE.md before starting
- Stack: vanilla HTML/CSS, no frameworks, all styles inline
- Working dir: ~/Desktop/ClaudeWork/aitoolgrade/
- Constraints: research-framing only, no hands-on testing claims, follow all prohibited language rules in CLAUDE.md

SUCCESS CRITERIA (ALL MUST BE TRUE)
1. review/[tool-name].html built - full content, score [SCORE]/10, pros/cons, pricing table, verdict box, Review schema, BreadcrumbList schema, [AUTHOR] byline linking to author page
2. Nav Reviews dropdown updated in nav.js only (single source of truth — propagates to all pages; no per-page nav edits)
3. Card added to reviews.html and category/[CATEGORY].html
4. Row added to compare.html
5. Homepage [CATEGORY] count incremented by 1
6. sitemap.xml updated with new URL
7. Grep check run for prohibited language - zero results before deploying
8. All files git pushed and SSH deployed
9. Confirm live URL is accessible before stopping

OPERATING RULES
1. Read CLAUDE.md first - follow all conventions exactly
2. Output full task list before writing any code
3. Self-verify each step before moving to the next
4. Use existing review pages as templates for HTML structure and styling
5. Research tool from primary sources - official docs, pricing page, community feedback
6. Do not make hands-on testing claims - research-based framing only
7. Do not deploy until grep check passes
8. Confirm SSH deploy is live before stopping

DEPLOY COMMAND
SSH: ssh -p 65002 u877849432@145.79.4.163
Deploy: cd ~/domains/aitoolgrade.com/public_html && git fetch origin && git reset --hard origin/main

Begin by outputting your plan. Then execute end-to-end without checking in until done or genuinely blocked.

Final step after deploy: paste the live URL into Perplexity and ask — "Review [LIVE URL] for promotional language, unsupported claims, and anything that reads more like marketing than research-based analysis. Flag specific phrases that should be qualified or removed." Fix any flagged issues with a quick Claude Code prompt before promoting on social.


## Missing File Structure Details

### Additional Pages (root level)
- how-we-review.html - methodology page explaining research process
- contribute.html - contributor recruitment page
- contact.html, advertise.html - standard pages
- affiliate-disclosure.html, privacy-policy.html, terms-of-use.html, cookie-policy.html

### Author Folder
- author/marcus-veil.html - Marcus Veil bio page
- author/priya-nolan.html - Priya Nolan bio page
- author/marcusveil.jpg - Marcus profile photo
- author/marcusbanner.jpeg - Marcus X banner
- author/priyanolan.jpeg - Priya profile photo
- author/priyabanner.jpg - Priya X banner

### Image Folder
- img/reviews/ - pricing screenshots for review pages
- Files: cursor-pricing.jpg, grammarly-pricing.jpg, jasper-pricing.jpg, perplexity-interface.jpg, perplexity-pricing.jpg

### Review Page HTML Structure
Every review page must include:
1. head with meta, fonts, inline styles, Review schema, BreadcrumbList schema
2. Nav placeholder that loads `nav.js` (renders the full dropdown — all reviews, 6 categories — from the single source of truth; do not hardcode nav markup)
3. Review hero: breadcrumb, tool icon, name, category, score, verdict banner
4. Byline: Researched by [Author link] - AIToolGrade Editorial Team - Last verified [Month Year]
5. review-body div: related post callout, What is X, Who is it for, Key features, Pricing table, Score breakdown, Pros/cons, Verdict box
6. Footer 4-column grid

### Href patterns by file depth (for non-nav content links)
Nav links are generated by `nav.js` (server-relative depth detection) — these patterns apply only
to links authored in page content (breadcrumbs, in-body links):
- Root files: href="review/jasper.html"
- review/ and category/ files: href="../review/jasper.html"
- blog/ files: href="../../review/jasper.html"
- author/ files: href="../review/jasper.html"

### Schema required on every review page
1. Review schema - includes itemReviewed SoftwareApplication with applicationCategory + operatingSystem + offers
2. BreadcrumbList schema - Home > Reviews > Tool Name

### Schema required on every blog post
1. Article schema - author Person, publisher Organization, datePublished, dateModified
2. BreadcrumbList schema - Home > Blog > Post Title


## Social Posting Workflow

When a new review or blog post is published, ask Claude to write posts for all three accounts.
Prompt: "Write X posts for [article name]"

### Post Types Per Article
1. Main posts x3 (one per account)
2. Engagement posts x3 (cross-account replies/quotes 1-2 days later)
3. Follow-up post for @aitoolgrade (links to related content)

### 4-Day Posting Cadence
- Day 1: @aitoolgrade main post + @marcusveil_ main post
- Day 2: @priyanolan main post
- Day 3: Marcus engagement post + Priya engagement post
- Day 4: @aitoolgrade follow-up linking to related content

### Voice Guidelines Per Account
- @aitoolgrade: Authoritative, factual, links to article, no personality
- @marcusveil_: Analytical, direct, skeptical-but-fair, adds technical context
- @priyanolan: Warm, accessible, relatable angle, everyday professional perspective

### Engagement Post Rules
- Marcus quotes or replies to Priya adding technical depth
- Priya quotes or replies to Marcus making it more accessible
- Keep them feeling natural — not scripted
- Space them out — do not post all at once

### No Automation
X posting is manual. Write posts in Claude.ai, copy and paste to each account.
Do not attempt to automate X posting via n8n or Claude Code.

PROMPT TEMPLATE (copy from here):

[TOOL NAME] review page fully built, deployed, and social posts generated for AIToolGrade.com

CONTEXT
- Project: AIToolGrade.com - read CLAUDE.md before starting
- Stack: vanilla HTML/CSS, no frameworks, all styles inline
- Working dir: ~/Desktop/ClaudeWork/aitoolgrade/
- Constraints: research-framing only, no hands-on testing claims, follow all prohibited language rules in CLAUDE.md
- Author: [AUTHOR] (Marcus Veil for technical/coding/automation tools, Priya Nolan for writing/productivity tools)
- Category: [CATEGORY]

SUCCESS CRITERIA (ALL MUST BE TRUE)
1. review/[tool-name].html built - full content, score/10, pros/cons, pricing table, verdict box, Review schema, BreadcrumbList schema, [AUTHOR] byline linking to author page
2. Nav Reviews dropdown updated in nav.js only (single source of truth — propagates to all pages; no per-page nav edits)
3. Card added to reviews.html and category/[CATEGORY].html
4. Row added to compare.html
5. Homepage [CATEGORY] count incremented by 1
6. sitemap.xml updated with new URL
7. Grep check run for prohibited language - zero results before deploying
8. All files git pushed and SSH deployed
9. Confirm live URL is accessible before stopping
10. Social posts file created at ~/Desktop/ClaudeWork/aitoolgrade/social-posts/[tool-name]-posts.md
11. Email summary sent to richn33@gmail.com with live URL and social posts

SOCIAL POSTS TO GENERATE (save to file)
Following the voice guidelines in CLAUDE.md, generate:
- @aitoolgrade main post (authoritative, factual, links to review)
- @marcusveil_ main post (analytical, direct, technical angle)
- @priyanolan main post (warm, accessible, everyday professional angle)
- Marcus engagement post (quotes or replies to Priya with technical depth)
- Priya engagement post (quotes or replies to Marcus making it accessible)
- @aitoolgrade follow-up post (links to related content on site)

POSTING CADENCE (include in social posts file)
- Day 1: @aitoolgrade main + @marcusveil_ main
- Day 2: @priyanolan main
- Day 3: Marcus engagement + Priya engagement
- Day 4: @aitoolgrade follow-up

OPERATING RULES
1. Read CLAUDE.md first - follow all conventions exactly
2. Output full task list before writing any code
3. Self-verify each step before moving to the next
4. Use existing review pages as templates for HTML structure and styling
5. Research tool from primary sources - official docs, pricing page, community feedback
6. Do not make hands-on testing claims - research-based framing only
7. Do not deploy until grep check passes
8. Confirm SSH deploy is live before stopping
9. Create social-posts/ folder if it does not exist
10. Send completion email via Gmail MCP to richn33@gmail.com with live URL and path to social posts file

DEPLOY COMMAND
SSH: ssh -p 65002 u877849432@145.79.4.163
Deploy: cd ~/domains/aitoolgrade.com/public_html && git fetch origin && git reset --hard origin/main

Begin by outputting your plan. Then execute end-to-end without checking in until done or genuinely blocked.

Final step after deploy (before generating social posts): paste the live URL into Perplexity and ask — "Review [LIVE URL] for promotional language, unsupported claims, and anything that reads more like marketing than research-based analysis. Flag specific phrases that should be qualified or removed." Fix any flagged issues with a quick Claude Code prompt before promoting on social.

## Schema Markup
All schema is JSON-LD in the head of each page. Do not add duplicate schema.

Required on every review page:
1. Review schema - reviewRating + author + itemReviewed (SoftwareApplication with applicationCategory + operatingSystem + offers)
2. BreadcrumbList schema - Home > Reviews > Tool Name

Required on every blog post:
1. Article schema - headline + author Person + publisher Organization + datePublished + dateModified
2. BreadcrumbList schema - Home > Blog > Post Title

Organization schema on index.html only.
Validate at: search.google.com/test/rich-results

## Factual Accuracy Rules
- Never claim a specific number of tools evaluated unless documented
- Do not claim personal hands-on testing of any tool
- Rich Nashawaty bio: 20 years in SEO, search strategy, content, digital growth
- Do not add biographical details beyond what is established

## Pricing Last Verified

All pricing verified May 2026. Update this table when pricing changes are confirmed.

| Tool | Last Verified | Notes |
|---|---|---|
| ChatGPT | May 2026 | 7-tier structure — Free, Go $8, Plus $20, Pro $100, Pro $200, Business $20-25, Enterprise |
| Cursor | May 2026 | Credit-based since June 2025 — ~225 usable requests at Pro when selecting frontier models manually |
| Grammarly | May 2026 | Premium renamed to Pro, Business replaced by Enterprise |
| Perplexity | May 2026 | Max $200 tier added, Comet browser now free |
| Jasper | May 2026 | Boss Mode discontinued, Starter gone, Creator $49/Pro $69 |
| Notion AI | May 2026 | $10 add-on gone since May 2025, full AI requires Business $20/user/month |

All tools verified May 25, 2026 via research agent brief — no new changes beyond what was updated May 19-20.

## Long-Term SEO Strategy
Key Google ranking systems:
1. Helpful Content System - every piece must genuinely help someone decide whether to use a tool
2. Reviews System - screenshots, specific observations, methodology transparency
3. Link Analysis - quality inbound links from relevant sources required for competitive queries

Near-term: screenshots on remaining reviews, methodology callout box, keep adding content
Medium-term: contributor bylines, outreach for links from AI newsletters
Longer-term: topic clusters, deep comparison posts (2000+ words)

Content published to date: 26 reviews, 12 blog posts, 1 comparison page, 1 resources page
Next content priorities (from May 24, 2026 session):
- Monitor Search Console in 2-3 weeks for position movement on Notion AI, Copy.ai, Midjourney rewrites
- Monitor CTR improvement on Bolt.new and ChatGPT vs Claude
- Next rewrite candidates: identify from next Search Console export

## Content Queue (updated June 6, 2026 session)

### Remaining queue
- (none currently) — brief fully cleared. Next priorities now come from Search Console
  data, not the research-agent brief. See "Search Console Optimization" for current
  rewrite candidates.

### Completed
- Grok Build review ✅ (June 7, 2026) — AI Coding, 6.7, Marcus Veil. xAI's first terminal-native agentic coding CLI; third lab-backed entry alongside Claude Code and Codex CLI. Standout feature is 8 parallel sub-agents each isolated in its own Git worktree — a genuine architectural first the category lacks. Underlying grok-build-0.1 scores 70.8% SWE-Bench Verified (17 pts below Claude Code's 87.6%); 256K context; MCP-compatible (Claude Code MCPs work unchanged); plan mode; headless -p CI mode. Arena Mode announced but not yet live. Carries the yellow COI box (AIToolGrade uses Claude Code; Grok Build is a direct competitor). Pricing trajectory is the key practical fact: $99/mo SuperHeavy intro reverts to $299/mo after 6 months (most expensive in category); SuperGrok $30 / X Premium+ $40 give basic access; API $0.20/M in, $1.50/M out (cheapest tokens in category). Early-beta score — revisit Q3 2026 when Arena Mode ships. datePublished/dateModified 2026-06-07. NOT added to compare.html (consistent with claude-code/kimi-code/deepseek-v4, which were also left out of that curated subset).
- Kimi Code review ✅ (June 5, 2026) — AI Coding, 7.8, Marcus Veil. Moonshot AI's open-source Claude Code competitor powered by Kimi K2.6 (1T-param MoE, 32B active; 80.2% SWE-bench Verified, ties GPT-5.5 on SWE-bench Pro). Leads on the MCP-compatibility migration story (every Claude Code MCP server works unchanged) and Agent Swarms (up to 300 parallel agents). Carries the yellow COI disclosure box (AIToolGrade uses Claude; Kimi Code is a direct competitor) plus the same Chinese-company data-residency treatment as DeepSeek V4. Pricing $0.60/M input (~25x cheaper than Opus 4.7). datePublished/dateModified 2026-06-05.
- "Best Free AI Tools for Students 2026" blog post ✅ (June 4, 2026) — Guide, Priya Nolan. Organized by job (studying/research/writing/coding/visual/notes) rather than ranking, with an honest free-tier rule stating each tool's exact limits upfront. Covers NotebookLM, Perplexity, ChatGPT, Grammarly, GitHub Copilot, Leonardo AI (not yet reviewed), Notion AI. Includes the "$0 with a .edu email" student stack table and a non-preachy academic-integrity note. datePublished/dateModified 2026-06-04.
- NotebookLM review ✅ (June 3, 2026) — Productivity, 8.7, Priya Nolan. Google's source-grounded research assistant (answers only from uploaded sources, no open-web hallucination). Audio Overviews given prominent coverage as the most-loved community feature; carries the NotebookLM vs Perplexity vs ChatGPT table and the explicit "use both" (NotebookLM + Perplexity) recommendation. Free tier scored 10/10 on value. datePublished/dateModified 2026-06-03.
- HeyGen review ✅ (June 3, 2026) — AI Video, 8.1, Priya Nolan. Realism leader (Avatar IV), photo-to-avatar, 175+ language translation, used by 40,000+ businesses. Carries the HeyGen vs Synthesia comparison table and an honest treatment of the credit-opacity issue (the #1 community complaint, partially addressed by the Feb 2026 upfront-estimate feature). datePublished/dateModified 2026-06-02.
- "Claude Code vs Cursor vs GitHub Copilot 2026" blog post ✅ (June 2, 2026) — Comparison, Marcus Veil. Leads with the 46% / 19% / 9% developer love-rating stat. Three-scenario head-to-head, full comparison table, team-pricing reality check ($190 / $400 / $1,250 for 10 devs), and a "use two tools" (Cursor + Claude Code) conclusion. Carries the COI yellow box near the top + editorial disclosure at the bottom (AIToolGrade uses Claude Code; scored conservatively at 8.0).
- Claude Code review ✅ (June 1, 2026) — AI Coding, 8.0, Anthropic's coding agent (1M context, Opus 4.7 87.6% SWE-bench, Agent Teams). Carries a prominent conflict-of-interest disclosure: AIToolGrade is built and maintained with Claude Code — the most significant COI on the site, placed immediately after the methodology callout, before the score. Score deliberately conservative (community evidence supports 8.5–9.0).
- DeepSeek V4 review ✅ (May 31, 2026) — AI Coding, 8.1, open-weight cost-disruptor
- Perplexity Computer review ✅ (May 31, 2026) — Productivity, 7.4, multi-agent / Cowork competitor
- "ChatGPT Pro $100 vs $200" blog post ✅ (May 2026)
- Thin review sweep — writesonic, windsurf, zapier, synthesia, n8n, github-copilot all 2,000+ words ✅ (May 29, 2026)
- "Best AI Coding Agents 2026" blog post ✅ (May 28, 2026)
- Google Antigravity 2.0 review ✅ (May 28, 2026)
- Lovable review ✅ (May 26, 2026)
- Best AI App Builders comparison post (Lovable vs Bolt vs Replit) ✅ (May 26, 2026)
- Cursor pricing blog post ✅
- ChatGPT Go vs Plus blog post ✅
- ChatGPT, Cursor, Grammarly, Perplexity, Jasper, Notion AI pricing all updated ✅

## Search Console Optimization

### June 5, 2026 — Search Console-driven rewrites
Based on GSC data (3-month period ending June 5):
- review/bolt.html — 252 impressions, position 11.6 → deep rewrite (2,808 words)
  New title: "Bolt.new Review 2026: WebContainers, Figma Import, and the Token Problem"
  Added: Bolt Cloud V2, multi-model, Figma import, Discussion Mode, token problem section
- review/adobe-firefly.html — 96 impressions, position 20.7 → deep rewrite (2,446 words)
  New title: "Adobe Firefly Review 2026: Runway Video, FLUX.2, and the Model Marketplace Strategy"
  Added: Runway Gen-4.5 partnership, FLUX.2, model marketplace strategy, updated pricing

Both authored by Marcus Veil. "Hands-on tested" → "Research verified" on both. Scores corrected and synced across reviews.html, compare.html, and category pages: bolt 8.6 → 8.3, adobe-firefly 8.4 → 8.7. dateModified 2026-06-05.

Reminders set:
- June 19, 2026 — check bolt.html and adobe-firefly.html for position movement
- Also check: notion-ai (was 66.5→36.2), copyai (80), midjourney (77)

Next Search Console candidates (not yet rewritten):
- review/n8n.html — 123 impressions, position 67.2
- review/writesonic.html — 160 impressions, position 77.7

### June 3, 2026 — New reviews published
- review/heygen.html — 8.1/10, Priya Nolan, AI Video
- review/notebooklm.html — 8.7/10, Priya Nolan, Productivity
- blog/claude-code-vs-cursor-vs-github-copilot-2026.html — Marcus Veil, Comparison

### June 2, 2026 — New comparison post
blog/claude-code-vs-cursor-vs-github-copilot-2026.html published
Target: "claude code vs cursor vs github copilot 2026"
Author: Marcus Veil
COI disclosure included — AIToolGrade uses Claude Code

### Last audit: May 24, 2026
Data source: Google Search Console — 3-month performance report

### Deep rewrites completed (position improvement goal)
| Page | Query | Position before | Action taken | Date |
|---|---|---|---|---|
| review/notion-ai.html | notion ai review | 66.5 | Deep rewrite — 2,594 words, Custom Agents, AI paywall controversy, Notion vs ChatGPT table | May 2026 |
| review/copyai.html | copy ai review | 80-81 | Deep rewrite — 2,076 words, Fullcast acquisition Oct 2025, GTM pivot, Trustpilot 1.9/5 | May 2026 |
| review/midjourney.html | midjourney review | 77.2 | Deep rewrite — 2,051 words, V8 Alpha March 2026, Trustpilot 1.5/5, model lineup | May 2026 |

### CTR optimizations completed (click improvement goal — already ranking)
| Page | Query | Position | Action taken | Date |
|---|---|---|---|---|
| review/bolt.html | bolt design to code | 8.4 | New title with Figma-to-code angle, 70% wall section added | May 2026 |
| blog/chatgpt-vs-claude-vs-perplexity.html | chatgpt vs claude | 5.3 | New title with benchmark data, verdict up front, benchmark table added | May 2026 |

### May 29, 2026 — Thin review sweep
All 6 remaining thin reviews rewritten to 2,000+ words ahead of May 2026 Google Core Update rollout (completing ~June 4, 2026).
- Do not analyze Search Console data until after June 4
- Check all 9 rewritten reviews for position movement week of June 7

### May 30, 2026 — Jasper deep rewrite
review/jasper.html — ~1,300 words → 2,106 words
Score corrected 9.2 → 8.2
Added: Jasper IQ section, 100+ agents, Content Pipelines, "The Jasper IQ Question", comparison table
Removed: "Hands-on tested" badge → "Research verified"

### How to prioritize future rewrites
1. Export queries from Search Console sorted by impressions descending
2. Identify pages with position 15-80 and 5+ impressions — these are rewrite candidates
3. Identify pages with position 5-15 and impressions but 0 clicks — these are CTR candidates
4. Check what top-ranking competitors cover that our review does not
5. Deep rewrite target: 2,000+ words, specific sections competitors rank on, updated pricing/features

### Rewrite checklist per page
- New SEO title including year and most-searched angle
- Updated meta description with specific hook (stat, controversy, verdict)
- Add sections covering topics top-ranking competitors include
- Update pricing to current
- Update dateModified in schema
- Run prohibited language check

## Thin Reviews — Rewrite Priority (COMPLETED May 29, 2026)

All reviews now 2,000+ words. Zero thin pages remaining.

### Completed rewrites
| Review | Before | After | Date |
|---|---|---|---|
| writesonic.html | 1,554 words | 2,124 words | May 29, 2026 |
| windsurf.html | 1,681 words | 2,000+ words | May 29, 2026 |
| zapier.html | 1,683 words | 2,000+ words | May 29, 2026 |
| synthesia.html | 1,654 words | 2,067 words | May 29, 2026 |
| n8n.html | 1,720 words | 2,082 words | May 29, 2026 |
| github-copilot.html | 1,786 words | 2,000+ words | May 29, 2026 |

### Earlier deep rewrites (Search Console data — May 24, 2026)
| Review | Before | After | Date |
|---|---|---|---|
| notion-ai.html | ~1,000 words | 2,594 words | May 24, 2026 |
| copyai.html | ~700 words | 2,963 words | May 24, 2026 |
| midjourney.html | ~900 words | 2,989 words | May 24, 2026 |

### Protected list (all 2,000+ words)
writesonic, windsurf, zapier, synthesia, n8n, github-copilot,
notion-ai, copyai, midjourney, replit, lovable, descript,
claude-cowork, microsoft-agent-365, chatgpt, grammarly,
perplexity, cursor, bolt, google-antigravity, jasper

Rewrite process:
1. Web search top-ranking competitors for "[tool] review 2026"
2. Identify sections they cover that we don't
3. Update pricing, add comparison table, expand community sentiment
4. Target 2,000+ words
5. Update dateModified in schema and byline

## Google AI Optimization (Updated May 2026)
Source: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide

Traditional SEO still governs AI Overviews and AI Mode — no separate AEO/GEO strategy needed.
Google's generative AI features pull from the same core ranking systems as regular Search.

### What matters most
- **Non-commodity content**: This is the priority. Generic listicles ("7 Best AI Writing Tools")
  are commodity content — content that could be produced by a generative AI model. AIToolGrade must
  go deeper: specific observations, documented evidence, unique scoring rationale.
- **Unique POV and methodology transparency**: Key differentiators vs G2, TechRadar, PCMag.
  Research-based framing is fine but must add genuine insight beyond what competitors offer.
  Our scoring methodology and community sentiment analysis are the differentiators — lean into them.
- **Structured, human-readable content**: Headings, clear sections, well-organized prose.
  Already doing this — maintain it.
- **Images and screenshots**: Create additional AI surface area beyond web links. Already have
  pricing screenshots — expand this across more reviews.

### What to ignore (Google confirmed these don't matter for AI search)
- llms.txt files — not needed
- "Chunking" content into small pieces — not needed
- Rewriting content specifically for AI phrasing — not needed
- Seeking inauthentic mentions — actively penalized
- Structured data is NOT required for AI features (still worth keeping for rich results)

### Tension point to watch
AIToolGrade's research-based positioning conflicts with Google's preference for first-hand reviews
with unique personal experience. Mitigation: lean harder on methodology transparency, community
sentiment, and scoring specificity to differentiate from pure AI-generated summaries. Consider
adding a "What users are saying" section to reviews sourced from Reddit/community to add a layer
of real-world perspective.

## Affiliate Programs

Tracker file: ~/Desktop/ClaudeWork/aitoolgrade/affiliate-tracker.md
Last updated: May 2026

Networks:
- Impact.com — applied May 19, 2026, pending approval. Search for Adobe, Grammarly, Semrush once approved.
- PartnerStack — rejected May 2026 (early-stage traffic). Reapply in 90 days.

Confirmed active programs:
- Adobe Firefly — Impact marketplace
- Grammarly — Impact marketplace
- Semrush — Impact marketplace ($200 + 30% recurring)
- Synthesia — synthesia.io/affiliates direct
- Notion — not accepting new affiliates (check quarterly)

Confirmed dead/paused:
- Jasper, Writesonic, Copy.ai — programs pulled
- Cursor, GitHub Copilot, Midjourney, ChatGPT — no programs exist

Adjacent programs (resources.html):
- Hostinger, NordVPN, Shopify, HubSpot — placeholders live, awaiting affiliate URLs
- resources.html live at aitoolgrade.com/resources.html

Affiliate link Claude Code prompt: ready to run when URLs approved — located in session notes May 19 2026.

## Blog Posts Published

_14 blog posts deployed in `blog/` (excluding index.html). Descript and Lovable are **review**
pages (`review/`), not blog posts — they are tracked in the File Structure review list, not here._

| Post | Author | Date | Target Keyword |
|---|---|---|---|
| Cursor vs Windsurf vs GitHub Copilot | Marcus Veil | April 2026 | cursor vs windsurf |
| Best Free AI Tools 2026 | Priya Nolan | April 2026 | best free ai tools 2026 |
| Best AI Tools for SEO 2026 | Marcus Veil | April 2026 | best ai tools seo |
| ChatGPT vs Claude vs Perplexity | Priya Nolan | April 2026 | chatgpt vs claude vs perplexity |
| How to Automate Your Business with n8n | Marcus Veil | April 2026 | how to automate business n8n |
| Cursor Pricing Explained | Marcus Veil | May 2026 | cursor pricing 2026 |
| Notion AI Pricing 2026 | Priya Nolan | May 2026 | notion ai pricing 2026 |
| Best AI Agents for Non-Developers 2026 | Priya Nolan | May 2026 | best ai agents 2026 |
| ChatGPT Go vs Plus 2026 | Priya Nolan | May 2026 | chatgpt go vs plus |
| Best AI App Builders 2026: Lovable vs Bolt vs Replit | Marcus Veil | May 2026 | best ai app builders 2026 |
| Best AI Coding Agents 2026 | Marcus Veil | May 2026 | best ai coding agents 2026 |
| ChatGPT Pro $100 vs $200 | Marcus Veil | May 2026 | chatgpt pro $100 vs $200 |
| Claude Code vs Cursor vs GitHub Copilot 2026 | Marcus Veil | June 2026 | claude code vs cursor vs github copilot 2026 |
| Best Free AI Tools for Students 2026 | Priya Nolan | June 2026 | best free ai tools for students 2026 |

## Research Agent

A weekly automated research agent that runs every Sunday at 7am via launchd on Rich's Mac.
Emails a structured brief to richn33@gmail.com every Sunday morning.

Purpose: Tells Rich what to work on for AIToolGrade that week — new tools to review, 
pricing updates needed, blog post opportunities, and what competitors are covering.

What the brief covers:
1. New tools worth reviewing - 3-5 tools not yet on site with estimated scores
2. Pricing changes - flags if any of the 26 reviewed tools have updated pricing
3. Trending search queries - high-opportunity keywords to target with new content
4. Competitor activity - topics G2/TechRadar/PCMag are covering that we are not
5. Community sentiment - Reddit discussions about tools getting significant attention

How to act on it:
- New tool recommendation → run the Claude Code review template to build and deploy
- Pricing change flagged → update the relevant review page pricing section
- Trending query → write a new blog post targeting that keyword
- Competitor topic → add to content backlog

Location: ~/Desktop/ClaudeWork/aitoolgrade_research/
CLAUDE.md: ~/Desktop/ClaudeWork/aitoolgrade_research/CLAUDE.md
Manual trigger: python3 ~/Desktop/ClaudeWork/aitoolgrade_research/research_agent.py
Schedule: Every Sunday 7am via ~/Library/LaunchAgents/com.aitoolgrade.research.plist

### Agent tuning (Last upgraded May 25, 2026)
- max_tokens reduced to 1000 — Gmail clips emails over ~102KB, so the brief must stay compact
- Conciseness instruction updated: bullet points only, max 1 sentence per item, max 3 items per section, under 300 words total
- API key updated May 25, 2026

## Site Architecture

### Nav — single source of truth (implemented May 30, 2026)
File: nav.js (project root)
All 61 HTML pages reference nav.js — zero hardcoded nav blocks remain.
To add a new review to nav: edit nav.js only — one line, updates all pages.
To add a new category: edit nav.js only.
4,292 lines of duplicated nav HTML removed.
Note: depth detection is server-relative — test via HTTP server not file://

### Mobile nav
Hamburger menu implemented May 30, 2026 — all 61 pages.
Toggle logic embedded in nav.js (not per-file inline scripts).

### Table of Contents
Added to all 24 review pages May 30, 2026.
Numbered TOC, var(--bg2) card, mono label, accent links.
Placed after intro section, before first H2.
"What Users Are Saying" excluded from TOC.

## Site Maintenance

### What Users Are Saying sections
Added to all 24 reviews (May 2026). Sources: Reddit + G2/Trustpilot per tool.
Update community sentiment quotes when research agent briefs surface significant new feedback.

### Nav
Standardized across all pages May 2026, then converted to a single source of truth (`nav.js`)
May 30, 2026 — now rendered from `nav.js` on all 61 pages (see Site Architecture). No per-page
nav markup remains.
Dropdown hover fix applied May 2026 — uses .nav-dropdown::after pseudo-element bridge (now in nav.js).
When adding new reviews: edit `nav.js` only (one line); depth/relative paths are handled
automatically by server-relative detection — no per-page path adjustments.

### Pricing updates
Run pricing check on all tools monthly — use research agent brief as trigger.
Always update: pricing table, What Changed callout box, byline "Last verified [Month Year]", schema dateModified.

### Conflict of interest disclosure
Claude Cowork review includes editorial disclosure — AIToolGrade uses Claude for content production.
Apply similar disclosure to any future Anthropic product reviews.

### Pending Cleanup
- [ ] Audit images/reviews/<tool>/ directory for orphaned feature.png files not referenced in any review page. Flagged May 31, 2026 during Jasper screenshot fix. Check each tool folder and remove any unreferenced images.

## Sitemap

File: sitemap.xml (root level)
Last updated: May 30, 2026

Rules:
- Reviews: changefreq="monthly", priority=0.8
- Blog posts: changefreq="weekly", priority=0.7
- Static pages (about, how-we-review, etc.): changefreq="yearly", priority=0.5
- Update lastmod date every time a page is added or significantly updated
- Run sitemap audit whenever new reviews or blog posts are added
- Submit updated sitemap to Google Search Console after significant additions

Current page count: 67 URLs (as of June 7, 2026) — one per HTML page.
(June 7, 2026: added `review/grok-build.html` — AI Coding, lastmod 2026-06-07.)
(June 5, 2026: added `review/kimi-code.html` — AI Coding, lastmod 2026-06-05.)
(June 4, 2026: added `blog/best-free-ai-tools-students-2026.html` — Guide, lastmod 2026-06-04.)
(June 3, 2026: added `review/notebooklm.html` — Productivity, lastmod 2026-06-03.)
(June 3, 2026: added `review/heygen.html` — AI Video, lastmod 2026-06-02.)
(June 2, 2026: added `blog/claude-code-vs-cursor-vs-github-copilot-2026.html`.)
(June 1, 2026: added `review/claude-code.html`.)
(May 31, 2026: added `review/deepseek-v4.html`.)
(May 31, 2026: added `review/perplexity-computer.html`.)
(May 30, 2026: added the previously-missing `blog/best-ai-agents-non-developers-2026.html` entry.)

## Technical Fixes Applied (May 2026)

### Duplicate indexing fix
- index.html canonical points to https://aitoolgrade.com/
- .htaccess 301 redirect: /index.html → /
- Sitemap uses https://aitoolgrade.com/ not /index.html

### Canonical tags
- All pages audited and canonical tags verified/added May 2026 — coverage now 61/61 pages (June 1, 2026)
- Format: <link rel="canonical" href="https://aitoolgrade.com/[path]" />
- blog/index.html canonical: https://aitoolgrade.com/blog/

### Internal links
- 267 index.html href instances replaced with clean root URLs May 2026
- All homepage links now use / not index.html
- blog/index.html links now use /blog/

### Nav dropdown hover fix
- Bridge pseudo-element moved to .nav-dropdown::after (May 2026)
- Previous fix (.dropdown-menu::before) failed because pointer-events:none on hidden dropdown killed the bridge
- Current fix is always interactive regardless of dropdown state
