# Scheduler Import — How to Use `scheduler-import.csv`

A ready-to-import file of all currently-drafted X posts. Stays useful whether you keep
posting manually or move to a scheduler — it's just the drafts in a structured format.

## What's in it
18 posts across the three pieces that have drafts written:
- **ChatGPT Go vs Plus vs Pro 2026** (6 posts)
- **GitHub Copilot Token Billing 2026** (6 posts)
- **Grok Build Review** (6 posts; note its 6.7/10 score + COI — Claude Code is a competitor)

Columns: `article, account, day, type, scheduled_datetime, content`
- `scheduled_datetime` is intentionally **blank** — fill it per account before importing
  (I won't fabricate post dates). `day` holds the relative cadence (Day 1–4) to schedule from.
- `content` is the full tweet, link inline, hashtag included where used. All ≤280 chars
  (X shortens links to ~23). No threads — every row is a single tweet.

## Importing
- **Typefully** — Settings → Import, or paste rows into the bulk composer. Map `content` to
  the post body and `scheduled_datetime` to the schedule. Switch the active account per the
  `account` column (Typefully handles multiple connected accounts).
- **Buffer** — Bulk upload takes one post per line; paste the `content` column per profile,
  or use the CSV via a connector. Set times to match the `day` cadence.
- **Hypefury** — CSV bulk upload supports a content + time mapping; same approach.

## Cadence (per article)
- Day 1: @AIToolGrade main + @marcusveil_ main
- Day 2: @priyanolan main
- Day 3: Marcus engagement + Priya engagement (space them out, not back-to-back)
- Day 4: @AIToolGrade follow-up (links to a sibling post, not the same hub)

## Account safety note
Per CLAUDE.md, posting stays **manual during the establishment phase** — new low-follower
accounts on a perfect automated cadence get flagged. When you graduate, start with a
scheduler (semi-automated: you write, it posts) before full n8n + X API automation.

## Editorial
All posts ran the same prohibited-language scan as site content (clean). The ChatGPT Day 1
@marcusveil_ line was corrected June 28, 2026 (removed the stale "locks out reasoning models"
claim — Go runs the same GPT-5.5 Instant base as Plus; real gap is features + no GPT-5.5 Pro).

## Still needs drafts (not yet in the CSV)
The social backlog in CLAUDE.md — ZoomMate, v0, OpenCode, v0-vs-Lovable-vs-Bolt, Cursor
refresh, Perplexity Max vs Pro, Notion AI refresh, Grok Imagine Video (+ comparison), aider.
Generate with "Write X posts for [article]", then regenerate this CSV to include them.
