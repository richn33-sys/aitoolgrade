#!/usr/bin/env python3
"""
Updates ~/Desktop/ClaudeWork/aitoolgrade/about.html
Adds a "Built by" / creator section before the footer.
Run from anywhere: python3 update_aitoolgrade_about.py
"""

import os

path = os.path.expanduser("~/Desktop/ClaudeWork/aitoolgrade/about.html")
content = open(path).read()

new_section = """
  <h2>Who built this</h2>
  <div class="values-grid">
    <div class="value-card" style="grid-column: 1 / -1;">
      <div class="value-desc" style="font-size:1rem; line-height:1.75;">
        AIToolGrade was built by <a href="https://richnashawaty.com" target="_blank" rel="noopener" style="color:var(--accent);text-decoration:none;border-bottom:1px solid rgba(232,93,38,0.3);">Rich Nashawaty</a> — an SEO consultant and AI automation specialist based in Boston, MA with 20 years of experience across freelance, agency, and enterprise organizations. Rich has led SEO strategy at global scale, managing sites across 19 languages and 11 international domains. He builds AI-powered tools and automation systems as part of his broader work helping businesses grow through search and automation. AIToolGrade is one of several projects he has built to provide independent, research-based resources for the AI community.
      </div>
    </div>
  </div>
"""

old = "  <h2>How we make money</h2>"
new = new_section + "\n  <h2>How we make money</h2>"

if old in content:
    content = content.replace(old, new)
    open(path, "w").write(content)
    print("✅ AIToolGrade about.html updated successfully")
    print("   Added 'Who built this' section with link to richnashawaty.com")
else:
    print("❌ Could not find insertion point — check the file manually")
    print("   Looking for: 'How we make money'")
