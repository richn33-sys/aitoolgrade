# Screenshot Insert Claude Code Prompt

Use this prompt in Claude Code after saving screenshots for a tool.
Replace [TOOL] with the tool name (e.g. cursor, notion-ai, lovable).

---

Read CLAUDE.md at ~/Desktop/ClaudeWork/aitoolgrade/CLAUDE.md before starting.

TASK: Insert screenshots into review/[TOOL].html

SCREENSHOTS AVAILABLE (check which exist in ~/Desktop/ClaudeWork/aitoolgrade/images/reviews/[TOOL]/):
- pricing.png — pricing page
- interface.png — main UI
- feature.png — key feature

FOR EACH SCREENSHOT THAT EXISTS, insert an image block in the appropriate section:

Pricing screenshot: insert after the pricing table
Interface screenshot: insert after the intro/overview section  
Feature screenshot: insert after the relevant feature description

IMAGE HTML TEMPLATE:
<figure style="margin: 24px 0;">
  <img src="../images/reviews/[TOOL]/[filename].png"
       alt="[descriptive alt text — be specific, e.g. Cursor Pro pricing page showing credit-based tiers May 2026]"
       style="width: 100%; border-radius: 10px; border: 1px solid var(--border);"
       loading="lazy">
  <figcaption style="font-family: var(--mono); font-size: 11px; color: var(--text3); margin-top: 8px; text-align: center;">
    [Caption — e.g. "Cursor pricing page — May 2026"]
  </figcaption>
</figure>

RULES:
- Alt text must be descriptive and specific — include tool name, what is shown, and date
- Never use generic alt text like "screenshot" or "image"
- Adjust relative path if inserting into blog posts (../../images/reviews/[TOOL]/)
- Do not add more than 3 images per review
- After inserting, run prohibited language check

After inserting:
git add . && git commit -m "Add screenshots to [TOOL] review"
Output SSH deploy command.
