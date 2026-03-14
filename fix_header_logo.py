import os, re

BASE = "c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website/"

HEADER_INNER_CSS = """
    header .container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 20px;
      text-align: center;
    }

    .header-brand {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 20px;
      margin-bottom: 15px;
    }

    .header-logo {
      width: 70px;
      height: 70px;
      border-radius: 16px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
      transition: transform 0.3s ease;
      flex-shrink: 0;
    }

    .header-logo:hover {
      transform: scale(1.05) rotate(3deg);
    }

    .header-text {
      text-align: left;
    }

    header h1 {
      font-size: 32px;
      margin-bottom: 6px;
      font-weight: 700;
      letter-spacing: -0.3px;
      text-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
"""

# 需要修复的页面及其注入位置（在 header { } 闭合大括号后面插入）
PAGES = {
    "mind/index.html":        True,   # 缺全套
    "partnership/index.html": True,   # 缺全套
    "about/index.html":       False,  # 只缺 header h1
}

for rel, full_inject in PAGES.items():
    path = BASE + rel
    html = open(path, encoding="utf-8").read()
    orig = html

    if full_inject:
        # 在 header { ... } 之后插入完整 CSS
        html = re.sub(
            r'(header\s*\{[^}]*\})',
            lambda m: m.group(0) + HEADER_INNER_CSS,
            html, count=1, flags=re.DOTALL
        )
    else:
        # about 只补 header h1
        if "header h1" not in html:
            html = re.sub(
                r'(header\s*\{[^}]*\})',
                lambda m: m.group(0) + """
    header h1 {
      font-size: 32px;
      margin-bottom: 6px;
      font-weight: 700;
      letter-spacing: -0.3px;
      text-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
""",
                html, count=1, flags=re.DOTALL
            )

    if html != orig:
        open(path, "w", encoding="utf-8").write(html)
        print(f"FIXED: {rel}")
    else:
        print(f"UNCHANGED: {rel}")
