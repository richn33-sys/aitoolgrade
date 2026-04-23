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
├── review/              ← 16 individual tool review pages
│   ├── jasper.html          (AI Writing, 9.2)
│   ├── copyai.html          (AI Writing, 8.4)
│   ├── writesonic.html      (AI Writing, 8.1)
│   ├── cursor.html          (AI Coding, 9.4)
│   ├── github-copilot.html  (AI Coding, 8.8)
│   ├── windsurf.html        (AI Coding, 9.1)
│   ├── bolt.html            (AI Coding, 8.6)
│   ├── chatgpt.html         (Productivity, 9.0)
│   ├── notion-ai.html       (Productivity, 8.6)
│   ├── zapier.html          (Automation, 8.2)
│   ├── n8n.html             (Automation, 8.7)
│   ├── midjourney.html      (AI Image, 9.3)
│   ├── adobe-firefly.html   (AI Image, 8.4)
│   ├── leonardo-ai.html     (AI Image, 8.7)
│   ├── runway.html          (AI Video, 8.9)
│   └── synthesia.html       (AI Video, 8.3)
├── category/            ← 6 category listing pages
│   ├── writing.html
│   ├── coding.html
│   ├── image.html
│   ├── automation.html
│   ├── video.html
│   └── productivity.html
└── blog/
    ├── index.html
    ├── cursor-vs-windsurf-vs-github-copilot.html
    ├── best-free-ai-tools-2026.html
    └── how-to-automate-business-with-n8n.html
```

## Category Review Counts (homepage displays these — keep in sync)
- AI Writing: 3
- AI Coding: 4
- AI Image: 3
- Automation: 2
- AI Video: 2
- Productivity: 2

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

## Nav Structure (current — always keep ALL pages in sync when updating)
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
                       Zapier
                       n8n
                       Midjourney
                       Adobe Firefly
                       Leonardo AI
                       Runway
                       Synthesia
                       Notion AI
```

### Nav href patterns by file location
- Root files (`index.html`, `reviews.html`, etc): `href="review/jasper.html"`, `href="compare.html"`, `href="blog/index.html"`
- Sub files (`review/`, `category/`): `href="../review/jasper.html"`, `href="../compare.html"`, `href="../blog/index.html"`
- Blog posts (`blog/`): `href="../../review/jasper.html"`, `href="../../compare.html"`

### Logo link by location
- Root files: `href="index.html"`
- Sub files (`review/`, `category/`): `href="../index.html"`
- Blog posts (`blog/`): `href="../../index.html"`

## Coding Conventions
- **No JavaScript frameworks** — vanilla HTML/CSS only
- **No external CSS files** — all styles are inline `<style>` blocks in each HTML file
- **No separate JS files** — any JS is inline `<script>` at bottom of body
- **Self-contained pages** — each page has its full nav, styles, and footer
- Mobile breakpoint at `768px` — always include responsive styles
- Breadcrumbs on all non-homepage pages: `Home › Category › Page Name`

## Do NOT Touch Without Asking
- CSS variable names — changing them breaks all pages
- Nav link structure — always update ALL pages when adding nav items
- Footer affiliate disclosure link — legally required on every page
- Score ratings — don't change published scores without a reason
- Google Search Console verification meta tag in `index.html`: `l6ZuoKnWQSEezpQ3liP8-QwvV045Q2LQLML-ryisN0o`

## Adding a New Review Page
1. Use an existing review page as template (e.g. `review/cursor.html`)
2. Update: title, meta description, tool name, score, pros/cons, affiliate link
3. Add to nav dropdown in ALL pages (root + review/ + category/ + blog/)
4. Add a card to the relevant `category/` page
5. Add a card to `reviews.html`
6. Add a row to `compare.html`
7. Update homepage category count in `index.html`
8. Add URL to `sitemap.xml`
9. Push and SSH deploy

## Updating Nav on All Pages (Python pattern)
```python
import os, re

root_nav = '''<div class="nav-dropdown"><a href="reviews.html">Reviews</a>...'''
sub_nav = '''<div class="nav-dropdown"><a href="../reviews.html">Reviews</a>...'''

def update_nav(content, new_nav):
    pattern = r'<div class="nav-dropdown"><a href="[^"]*reviews\.html">Reviews</a><div class="dropdown-menu">.*?</div></div>'
    return re.sub(pattern, new_nav, content, flags=re.DOTALL)
```

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
