// AIToolGrade nav — single source of truth
// To add a new review: add one line in the Reviews dropdown below, affects all pages
// To change nav structure: edit here only
//
// Path model: absolute links (/, /#categories, /blog/, /#newsletter) are
// depth-independent and stay as-is. Relative links (category/, reviews.html,
// review/, compare.html) are prefixed with `prefix` so they resolve from any
// folder depth. Served from the domain root, output is identical to the old
// hardcoded nav on every page.
(function () {
  // Detect folder depth from the pathname, then build a `../` prefix.
  var path = window.location.pathname;
  var segments = path.split('/').filter(Boolean);
  // Drop a trailing filename (e.g. cursor.html) so only directories count.
  if (segments.length > 0 && segments[segments.length - 1].indexOf('.') > -1) {
    segments.pop();
  }
  var depth = segments.length;
  var prefix = depth === 0 ? '' : new Array(depth).fill('..').join('/') + '/';

  var nav =
    '<nav>' +
    '<div class="nav-inner">' +
    '<button class="nav-toggle" type="button" aria-label="Toggle menu" aria-expanded="false">☰</button>' +
    '<a href="/" class="nav-logo">AI Tool<span>Grade</span></a>' +
    '<div class="nav-links">' +
    '<div class="nav-dropdown">' +
    '<a href="/#categories">Categories</a>' +
    '<div class="dropdown-menu">' +
    '<a href="' + prefix + 'category/writing.html">AI Writing</a>' +
    '<a href="' + prefix + 'category/coding.html">AI Coding</a>' +
    '<a href="' + prefix + 'category/image.html">AI Image</a>' +
    '<a href="' + prefix + 'category/automation.html">Automation</a>' +
    '<a href="' + prefix + 'category/video.html">AI Video</a>' +
    '<a href="' + prefix + 'category/productivity.html">Productivity</a>' +
    '</div>' +
    '</div>' +
    '<div class="nav-dropdown">' +
    '<a href="' + prefix + 'reviews.html">Reviews</a>' +
    '<div class="dropdown-menu">' +
    '<a href="' + prefix + 'review/jasper.html">Jasper AI</a>' +
    '<a href="' + prefix + 'review/copyai.html">Copy.ai</a>' +
    '<a href="' + prefix + 'review/cursor.html">Cursor</a>' +
    '<a href="' + prefix + 'review/chatgpt.html">ChatGPT</a>' +
    '<a href="' + prefix + 'review/writesonic.html">Writesonic</a>' +
    '<a href="' + prefix + 'review/github-copilot.html">GitHub Copilot</a>' +
    '<a href="' + prefix + 'review/windsurf.html">Windsurf</a>' +
    '<a href="' + prefix + 'review/bolt.html">Bolt.new</a>' +
    '<a href="' + prefix + 'review/lovable.html">Lovable</a>' +
    '<a href="' + prefix + 'review/google-antigravity.html">Google Antigravity</a>' +
    '<a href="' + prefix + 'review/deepseek-v4.html">DeepSeek V4</a>' +
    '<a href="' + prefix + 'review/zapier.html">Zapier</a>' +
    '<a href="' + prefix + 'review/n8n.html">n8n</a>' +
    '<a href="' + prefix + 'review/microsoft-agent-365.html">Microsoft Agent 365</a>' +
    '<a href="' + prefix + 'review/midjourney.html">Midjourney</a>' +
    '<a href="' + prefix + 'review/adobe-firefly.html">Adobe Firefly</a>' +
    '<a href="' + prefix + 'review/leonardo-ai.html">Leonardo AI</a>' +
    '<a href="' + prefix + 'review/runway.html">Runway</a>' +
    '<a href="' + prefix + 'review/synthesia.html">Synthesia</a>' +
    '<a href="' + prefix + 'review/descript.html">Descript</a>' +
    '<a href="' + prefix + 'review/notion-ai.html">Notion AI</a>' +
    '<a href="' + prefix + 'review/perplexity.html">Perplexity AI</a>' +
    '<a href="' + prefix + 'review/perplexity-computer.html">Perplexity Computer</a>' +
    '<a href="' + prefix + 'review/grammarly.html">Grammarly</a>' +
    '<a href="' + prefix + 'review/replit.html">Replit</a>' +
    '<a href="' + prefix + 'review/claude-cowork.html">Claude Cowork</a>' +
    '</div>' +
    '</div>' +
    '<a href="' + prefix + 'compare.html">Compare</a>' +
    '<a href="/blog/">Blog</a>' +
    '<a href="/#newsletter" class="nav-cta">Get Updates</a>' +
    '</div>' +
    '</div>' +
    '</nav>';

  document.write(nav);

  // Mobile hamburger toggle. Delegated on document so it works no matter when
  // the nav is injected. Toggles `nav-open` on <nav>; the existing CSS shows
  // .nav-links when nav has .nav-open at the 768px breakpoint.
  document.addEventListener('click', function (e) {
    var nav = document.querySelector('nav');
    if (!nav) return;
    var toggle = e.target.closest && e.target.closest('.nav-toggle');
    if (toggle) {
      var open = nav.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      e.preventDefault();
      return;
    }
    if (nav.classList.contains('nav-open')) {
      if ((e.target.closest && e.target.closest('.nav-links a')) || !(e.target.closest && e.target.closest('nav'))) {
        nav.classList.remove('nav-open');
        var t = nav.querySelector('.nav-toggle');
        if (t) t.setAttribute('aria-expanded', 'false');
      }
    }
  });
})();
