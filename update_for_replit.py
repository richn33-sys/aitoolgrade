#!/usr/bin/env python3
"""
AIToolGrade — Replit review integration script
Run from: ~/Desktop/ClaudeWork/aitoolgrade/
Usage: python3 update_for_replit.py

What this does:
  1. Copies replit.html into review/
  2. Adds Replit to nav dropdown on ALL pages (root, review/, category/, blog/)
  3. Adds card to category/coding.html
  4. Adds card to reviews.html
  5. Adds row to compare.html
  6. Updates homepage AI Coding count from 4 → 5
  7. Adds entry to sitemap.xml

Run once, then: git add . && git commit -m "Add Replit review" && git push
Then SSH deploy as usual.
"""

import os, shutil
from pathlib import Path

BASE = Path(__file__).parent
REVIEW_SRC = BASE / "replit.html"

# ─── Step 1: Copy review file ──────────────────────────────────────────────
dest = BASE / "review" / "replit.html"
if REVIEW_SRC.exists():
    shutil.copy(REVIEW_SRC, dest)
    print(f"✅ Copied replit.html → review/replit.html")
else:
    print(f"⚠️  replit.html not found next to script — skipping copy (assumes already in review/)")


# ─── Nav insertion helpers ─────────────────────────────────────────────────
REPLIT_ROOT  = '          <a href="review/replit.html">Replit</a>'
REPLIT_SUB   = '          <a href="../review/replit.html">Replit</a>'
REPLIT_BLOG  = '          <a href="../../review/replit.html">Replit</a>'

def insert_after(content, anchor, new_line):
    lines = content.split('\n')
    result = []
    inserted = False
    for line in lines:
        result.append(line)
        if not inserted and anchor.strip() in line:
            result.append(new_line)
            inserted = True
    if not inserted:
        print(f"  ⚠️  Anchor not found: {anchor.strip()[:60]}")
    return '\n'.join(result)

def already_has_replit(content):
    return 'replit.html' in content


# ─── Step 2: Update nav on all pages ──────────────────────────────────────
root_files     = list(BASE.glob("*.html"))
review_files   = list((BASE / "review").glob("*.html"))
category_files = list((BASE / "category").glob("*.html"))
blog_files     = list((BASE / "blog").glob("*.html"))

# Insert Replit after Bolt.new in the nav dropdown
all_files = {
    'root':     (root_files,     REPLIT_ROOT,  'href="review/bolt.html"'),
    'review':   (review_files,   REPLIT_SUB,   'href="../review/bolt.html"'),
    'category': (category_files, REPLIT_SUB,   'href="../review/bolt.html"'),
    'blog':     (blog_files,     REPLIT_BLOG,  'href="../../review/bolt.html"'),
}

print("\n📋 Updating nav on all pages...")
for loc, (files, new_line, anchor) in all_files.items():
    for f in files:
        content = f.read_text(encoding='utf-8')
        if already_has_replit(content):
            print(f"  ⏭  {f.name} — already has Replit")
            continue
        updated = insert_after(content, anchor, new_line)
        f.write_text(updated, encoding='utf-8')
        print(f"  ✅ {loc}/{f.name} — nav updated")


# ─── Step 3: Add card to category/coding.html ─────────────────────────────
CODING_CARD = '''
      <!-- Replit -->
      <div class="tool-card">
        <div class="tool-card-header">
          <div>
            <div class="tool-name">Replit</div>
            <div class="tool-category">AI Coding</div>
          </div>
          <div class="tool-score">★ 8.3</div>
        </div>
        <p class="tool-desc">Browser-based AI development platform. Agent 3 builds and deploys complete apps from plain-language prompts — zero setup required. Credit-based billing requires monitoring for active builders.</p>
        <div class="tool-meta">
          <span class="tool-price">Free <span class="free-badge">FREE</span> · Core $20/mo</span>
        </div>
        <a href="../review/replit.html" class="tool-link">Read Review →</a>
      </div>
'''

coding_path = BASE / "category" / "coding.html"
if coding_path.exists():
    content = coding_path.read_text(encoding='utf-8')
    if 'replit.html' not in content:
        last_card = content.rfind('</div>\n      </div>')
        if last_card != -1:
            insert_pos = last_card + len('</div>\n      </div>')
            content = content[:insert_pos] + '\n' + CODING_CARD + content[insert_pos:]
            coding_path.write_text(content, encoding='utf-8')
            print("\n✅ category/coding.html — Replit card added")
        else:
            print("\n⚠️  category/coding.html — couldn't find insertion point, add card manually")
    else:
        print("\n⏭  category/coding.html — already has Replit")
else:
    print("\n⚠️  category/coding.html not found")


# ─── Step 4: Add card to reviews.html ─────────────────────────────────────
REVIEWS_CARD = '''
      <!-- Replit -->
      <div class="tool-card">
        <div class="tool-card-header">
          <div>
            <div class="tool-name">Replit</div>
            <div class="tool-category">AI Coding</div>
          </div>
          <div class="tool-score">★ 8.3</div>
        </div>
        <p class="tool-desc">Browser-based AI development platform. Agent 3 builds and deploys complete apps from plain-language prompts — zero setup required. Credit-based billing requires monitoring for active builders.</p>
        <div class="tool-meta">
          <span class="tool-price">Free <span class="free-badge">FREE</span> · Core $20/mo</span>
        </div>
        <a href="review/replit.html" class="tool-link">Read Review →</a>
      </div>
'''

reviews_path = BASE / "reviews.html"
if reviews_path.exists():
    content = reviews_path.read_text(encoding='utf-8')
    if 'replit.html' not in content:
        last_card = content.rfind('</div>\n      </div>')
        if last_card != -1:
            insert_pos = last_card + len('</div>\n      </div>')
            content = content[:insert_pos] + '\n' + REVIEWS_CARD + content[insert_pos:]
            reviews_path.write_text(content, encoding='utf-8')
            print("✅ reviews.html — Replit card added")
        else:
            print("⚠️  reviews.html — couldn't find insertion point, add card manually")
    else:
        print("⏭  reviews.html — already has Replit")
else:
    print("⚠️  reviews.html not found")


# ─── Step 5: Add row to compare.html ──────────────────────────────────────
COMPARE_ROW = '''            <tr>
              <td><a href="review/replit.html">Replit</a></td>
              <td>AI Coding</td>
              <td class="score-cell">8.3</td>
              <td>Free / $20/mo (Core)</td>
              <td>Web (browser only)</td>
              <td>Agent 3 autonomous coding, cloud IDE, one-click deploy</td>
            </tr>'''

compare_path = BASE / "compare.html"
if compare_path.exists():
    content = compare_path.read_text(encoding='utf-8')
    if 'replit.html' not in content:
        # Insert after bolt.html row if present, else before </tbody>
        if 'bolt.html' in content:
            bolt_idx = content.find('bolt.html')
            row_end = content.find('</tr>', bolt_idx)
            if row_end != -1:
                insert_pos = row_end + len('</tr>')
                content = content[:insert_pos] + '\n' + COMPARE_ROW + content[insert_pos:]
                compare_path.write_text(content, encoding='utf-8')
                print("✅ compare.html — Replit row added")
            else:
                print("⚠️  compare.html — couldn't find Bolt row end")
        elif '</tbody>' in content:
            content = content.replace('</tbody>', COMPARE_ROW + '\n            </tbody>', 1)
            compare_path.write_text(content, encoding='utf-8')
            print("✅ compare.html — Replit row added (before </tbody>)")
        else:
            print("⚠️  compare.html — couldn't find insertion point, add row manually")
    else:
        print("⏭  compare.html — already has Replit")
else:
    print("⚠️  compare.html not found")


# ─── Step 6: Update homepage AI Coding count 4 → 5 ────────────────────────
index_path = BASE / "index.html"
if index_path.exists():
    content = index_path.read_text(encoding='utf-8')
    # The CLAUDE.md documents AI Coding as 4 tools — now adding a 5th
    # Try the most specific pattern first
    old = '<div class="cat-count">4 tools reviewed</div>'
    new = '<div class="cat-count">5 tools reviewed</div>'
    if old in content:
        # Make sure we're updating the coding section, not another with count 4
        # Find coding section context
        coding_idx = content.lower().find('ai coding')
        count_idx = content.find(old)
        if abs(coding_idx - count_idx) < 500:
            content = content.replace(old, new, 1)
            index_path.write_text(content, encoding='utf-8')
            print("✅ index.html — AI Coding count updated: 4 → 5")
        else:
            # Safe fallback: replace first occurrence near coding section
            content = content.replace(old, new, 1)
            index_path.write_text(content, encoding='utf-8')
            print("✅ index.html — AI Coding count updated (verify correct section)")
    else:
        print("⚠️  index.html — couldn't auto-update count. Find '4 tools reviewed' in the AI Coding section and change to 5 manually.")
else:
    print("⚠️  index.html not found")


# ─── Step 7: Update sitemap.xml ───────────────────────────────────────────
SITEMAP_ENTRY = '''
  <url>
    <loc>https://aitoolgrade.com/review/replit.html</loc>
    <lastmod>2026-05-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>'''

sitemap_path = BASE / "sitemap.xml"
if sitemap_path.exists():
    content = sitemap_path.read_text(encoding='utf-8')
    if 'replit.html' not in content:
        content = content.replace('</urlset>', SITEMAP_ENTRY + '\n</urlset>')
        sitemap_path.write_text(content, encoding='utf-8')
        print("✅ sitemap.xml — Replit URL added")
    else:
        print("⏭  sitemap.xml — already has Replit")
else:
    print("⚠️  sitemap.xml not found")


print("\n🎉 Done. Next steps:")
print("   1. Preview review/replit.html in Safari")
print("   2. git add . && git commit -m 'Add Replit review' && git push")
print("   3. SSH in: ssh -p 65002 u877849432@145.79.4.163")
print("   4. cd ~/domains/aitoolgrade.com/public_html && git fetch origin && git reset --hard origin/main")
print("   5. Test live: https://aitoolgrade.com/review/replit.html")
