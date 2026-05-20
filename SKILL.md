# Weekly Research Agent — SKILL.md

A reusable skill for building an automated weekly research brief that emails a structured intelligence report every Monday morning. Adapt for any niche site, newsletter, or content project.

---

## What This Skill Does

Builds a Python-based research agent that:
1. Runs automatically every Monday at 8am via macOS launchd
2. Calls the Anthropic API with web search to research 5 intelligence areas
3. Formats findings as a clean HTML email brief
4. Delivers it to your inbox before you start the week

Cost per run: ~$0.05–0.15 (Anthropic API usage)

---

## When To Use This Skill

Use this skill when a project needs ongoing competitive intelligence and you want it delivered automatically without manual effort. Good fit for:
- Niche review or affiliate sites (monitor competitors, pricing changes, trending topics)
- Newsletter projects (surface what to write about each week)
- SaaS or product businesses (track competitor activity and community sentiment)
- Any content project where staying current is important

---

## Required Inputs (Customize Per Project)

Before building, define these for your project:

| Input | Description | Example |
|---|---|---|
| `PROJECT_NAME` | Name used in email subjects and file names | `AIToolGrade` |
| `PROJECT_DESCRIPTION` | One sentence describing the site/project | `An AI tools review and affiliate site` |
| `CURRENT_ITEMS` | List of things already covered (so agent won't re-recommend them) | `["Jasper AI", "Cursor", "ChatGPT"]` |
| `ITEMS_TO_MONITOR` | Specific items to check for changes (pricing, updates, etc.) | `["Jasper AI", "Cursor", "Grammarly"]` |
| `COMPETITORS` | Sites to monitor for content gaps | `["G2", "TechRadar", "PCMag"]` |
| `COMMUNITIES` | Reddit subs or forums to monitor | `["r/artificial", "r/MachineLearning"]` |
| `ALERT_EMAIL` | Where the brief gets delivered | `you@gmail.com` |
| `FOLDER_NAME` | Local folder name | `aitoolgrade_research` |
| `PLIST_LABEL` | Unique launchd identifier | `com.aitoolgrade.research` |

---

## File Structure To Create

```
~/Desktop/ClaudeWork/[FOLDER_NAME]/
├── research_agent.py          ← main script (generated from template below)
├── .env                       ← API keys and email credentials (never commit)
├── com.[PLIST_LABEL].plist    ← launchd schedule config
└── CLAUDE.md                  ← project memory file
```

---

## Step 1 — Create The Folder

```bash
mkdir -p ~/Desktop/ClaudeWork/[FOLDER_NAME]
cd ~/Desktop/ClaudeWork/[FOLDER_NAME]
```

---

## Step 2 — Create The .env File

```bash
cat > .env << 'EOF'
GMAIL_USER=your_gmail@gmail.com
GMAIL_PASSWORD=your_gmail_app_password
ALERT_EMAIL=your_email@gmail.com
ANTHROPIC_API_KEY=your_anthropic_api_key
EOF
```

**Gmail App Password:** Go to Google Account → Security → 2-Step Verification → App Passwords. Generate one for "Mail". Use the 16-character password with no spaces.

**Never commit .env to git.** Add it to `.gitignore`.

---

## Step 3 — Create research_agent.py

Use this template. Replace all `[BRACKETED]` values with your project specifics.

```python
#!/usr/bin/env python3
"""
[PROJECT_NAME] Research Agent
Runs weekly via launchd — emails a research brief to [ALERT_EMAIL]
"""

import sys
import smtplib
import os
from pathlib import Path
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import anthropic

sys.path.insert(0, str(Path(__file__).parent))
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
ALERT_EMAIL = os.getenv("ALERT_EMAIL")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Items already covered — agent won't re-recommend these
CURRENT_ITEMS = [
    "[Item 1]", "[Item 2]", "[Item 3]"
    # Add more as your project grows
]

# Items to monitor for changes (pricing, updates, etc.)
ITEMS_TO_MONITOR = [
    "[Item A]", "[Item B]", "[Item C]"
]

# Competitor sites to watch
COMPETITORS = [
    "[Competitor 1]", "[Competitor 2]", "[Competitor 3]"
]

# Communities to monitor
COMMUNITIES = [
    "[r/subreddit1]", "[r/subreddit2]"
]

BRAND_COLOR = "[#hexcode]"   # Your brand accent color for the email header


def send_email(subject, html_body):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = GMAIL_USER
    msg["To"] = ALERT_EMAIL
    msg.attach(MIMEText(html_body, "html"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, ALERT_EMAIL, msg.as_string())


def run_research():
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    today = datetime.now().strftime("%B %d, %Y")
    current_list = ", ".join(CURRENT_ITEMS)
    monitor_list = ", ".join(ITEMS_TO_MONITOR)
    competitor_list = ", ".join(COMPETITORS)
    community_list = ", ".join(COMMUNITIES)

    prompt = f"""You are a research agent for [PROJECT_NAME] — [PROJECT_DESCRIPTION].
Today is {today}.

Already covered: {current_list}

Using web search, research the following and produce a structured weekly brief:

1. NEW [ITEMS] WORTH COVERING
   - Search for new [items] in [your niche] launched or gaining traction recently
   - Identify 3-5 NOT already covered
   - For each: name, why it's worth covering, priority level (high/medium/low)

2. CHANGES TO MONITOR
   - Check for updates or changes to: {monitor_list}
   - Flag anything that has changed and needs action

3. TRENDING TOPICS & KEYWORDS
   - Search for trending topics and search queries in [your niche]
   - Identify 3-5 high-opportunity angles to create content around

4. COMPETITOR ACTIVITY
   - Search for recent content from: {competitor_list}
   - Note topics they are covering that we are not

5. COMMUNITY SENTIMENT
   - Search {community_list} for hot discussions this week in [your niche]
   - Note anything getting significant attention (positive or negative)

Format your response as clean HTML for an email brief.
Be specific and actionable — every item should tell me exactly what to do next.
"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2000,
        tools=[{{"type": "web_search_20250305", "name": "web_search"}}],
        messages=[{{"role": "user", "content": prompt}}]
    )

    brief_html = ""
    for block in message.content:
        if hasattr(block, "text"):
            brief_html += block.text

    email_html = f"""
    <html><body style="font-family: Arial, sans-serif; max-width: 700px; margin: 0 auto; padding: 20px;">
    <h1 style="color: {BRAND_COLOR};">[PROJECT_NAME] Weekly Research Brief</h1>
    <p style="color: #666;">{today}</p>
    <hr style="border-color: #e2e0d8;">
    {brief_html}
    <hr style="border-color: #e2e0d8;">
    <p style="color: #999; font-size: 12px;">Generated by [PROJECT_NAME] Research Agent</p>
    </body></html>
    """

    send_email(f"📊 [PROJECT_NAME] Weekly Brief — {today}", email_html)
    print(f"Research brief sent successfully — {today}")


if __name__ == "__main__":
    try:
        run_research()
    except Exception as e:
        print(f"Error: {e}")
        try:
            send_email(
                "⚠️ [PROJECT_NAME] Research Agent Error",
                f"<p>Research agent failed with error: {str(e)}</p>"
            )
        except:
            pass
```

---

## Step 4 — Install Dependencies

```bash
pip3 install anthropic python-dotenv
```

---

## Step 5 — Test It Manually

```bash
python3 ~/Desktop/ClaudeWork/[FOLDER_NAME]/research_agent.py
```

Check your inbox. If it arrives, move to Step 6. If not, check the troubleshooting section below.

---

## Step 6 — Create The launchd Plist

Create this file at `~/Library/LaunchAgents/com.[PLIST_LABEL].plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.[PLIST_LABEL]</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/[YOUR_MAC_USERNAME]/Desktop/ClaudeWork/[FOLDER_NAME]/research_agent.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>1</integer>
        <key>Hour</key>
        <integer>8</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/tmp/[PLIST_LABEL].log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/[PLIST_LABEL].log</string>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
```

Then load it:

```bash
launchctl load ~/Library/LaunchAgents/com.[PLIST_LABEL].plist
launchctl list | grep [PLIST_LABEL]
```

A PID in the output means it's running. A `-` means it's loaded and waiting for the next Monday 8am trigger.

---

## Step 7 — Create The Project CLAUDE.md

Save this inside the project folder so any Claude session can pick up context:

```markdown
# [PROJECT_NAME] Research Agent — CLAUDE.md

## Overview
Weekly research agent for [PROJECT_NAME]. Runs every Monday at 8am via launchd.
Emails a structured brief to [ALERT_EMAIL].

## Location
~/Desktop/ClaudeWork/[FOLDER_NAME]/

## Files
- research_agent.py — main script
- .env — credentials (never share)
- com.[PLIST_LABEL].plist — schedule config
- CLAUDE.md — this file

## Schedule
launchd — every Monday 8:00 AM
Log: /tmp/[PLIST_LABEL].log

## Commands
launchctl list | grep [PLIST_LABEL]
launchctl unload ~/Library/LaunchAgents/com.[PLIST_LABEL].plist
launchctl load ~/Library/LaunchAgents/com.[PLIST_LABEL].plist
python3 ~/Desktop/ClaudeWork/[FOLDER_NAME]/research_agent.py

## Updating The Covered Items List
When new content is added to [PROJECT_NAME], update CURRENT_ITEMS
in research_agent.py so the agent stops recommending them.

## Troubleshooting
- 401 API error: check ANTHROPIC_API_KEY in .env
- Gmail auth error: use app password without spaces
- Agent not running: launchctl list | grep [PLIST_LABEL]
- Empty email: cat /tmp/[PLIST_LABEL].log
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| 401 API error | Check `ANTHROPIC_API_KEY` in `.env` |
| Gmail auth error | Use 16-char app password, no spaces |
| Agent not running | `launchctl list \| grep [PLIST_LABEL]` |
| Empty email arrives | Check `/tmp/[PLIST_LABEL].log` |
| Mac asleep on Monday | Mac must be awake — launchd won't wake it |
| Script runs but no email | Check spam folder; verify `ALERT_EMAIL` in `.env` |

---

## Customization Options

**Change the schedule** — edit the plist `StartCalendarInterval`. To run daily, remove `Weekday`.

**Add a 6th research area** — add a new numbered section to the prompt in `run_research()`.

**Change the model** — swap `claude-opus-4-5` for `claude-sonnet-4-6` to reduce cost (~70% cheaper, slightly less thorough).

**Multiple recipients** — change `ALERT_EMAIL` to a comma-separated string and update `sendmail()` accordingly.

---

## Estimated Costs

| Model | Est. cost per run | Est. monthly (4 runs) |
|---|---|---|
| claude-opus-4-5 | $0.05–0.15 | $0.20–0.60 |
| claude-sonnet-4-6 | $0.01–0.05 | $0.04–0.20 |

---

*Built from the AIToolGrade Research Agent — richnashawaty.com*
