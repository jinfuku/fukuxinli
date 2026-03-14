import os, re

BASE = r"c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website"

PAGES = [
    "spirit/index.html",
    "mind/index.html",
    "body/index.html",
    "partnership/index.html",
    "ai/index.html",
    "about/index.html",
    "spirit/张成谈内勒斯影响/index.html",
    "spirit/内勒斯生命整合过程排列LIP/index.html",
    "spirit/威尔菲德内勒斯核心概念术语翻译对照表/index.html",
    "spirit/意识与生命整合的探索/index.html",
    "mind/存在主义心理治疗的基本概念/index.html",
    "mind/系统排列生命整合闭门读书会招募/index.html",
    "mind/福库心理系统排列生命整合进修班/index.html",
    "mind/我们生活的世界意识与精神之旅目录/index.html",
    "body/推拿疗愈身体的力量/index.html",
    "body/艾灸的温暖疗愈/index.html",
    "partnership/马尔特伴侣关系整合过程排列BIP/index.html",
    "partnership/伴侣关系中的沟通艺术/index.html",
    "ai/ai在心理咨询中的辅助作用/index.html",
]

HEADER_CSS_INJECT = """
    /* Header — Apple sticky glass */
    header {
      background: linear-gradient(135deg, #00c853 0%, #2196f3 100%);
      color: white;
      padding: 15px 0 20px;
      position: sticky;
      top: 0;
      z-index: 1000;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12),
                  0 1px 3px rgba(0, 0, 0, 0.08);
    }
"""

changed = 0
for rel_path in PAGES:
    full = os.path.join(BASE, rel_path).replace("/", os.sep)
    if not os.path.exists(full):
        print(f"SKIP: {rel_path}")
        continue
    html = open(full, encoding="utf-8").read()
    orig = html

    # 如果已经有 sticky 就跳过
    if "position: sticky" in html or "position:sticky" in html:
        print(f"already sticky: {rel_path}")
        continue

    # 方案A：已有 header { ... }，在大括号内末尾插入
    def add_sticky_to_header(m):
        inner = m.group(2)
        if "position" not in inner:
            inner = inner.rstrip() + "\n      position: sticky;\n      top: 0;\n      z-index: 1000;\n      backdrop-filter: blur(20px);\n      -webkit-backdrop-filter: blur(20px);\n    "
        return m.group(1) + inner + m.group(3)

    new_html = re.sub(
        r'(header\s*\{)([^}]*?)(\})',
        add_sticky_to_header,
        html, count=1, flags=re.DOTALL
    )

    # 方案B：没有 header { ... }，在 body { ... } 后面插入完整规则
    if new_html == html:
        new_html = re.sub(
            r'(body\s*\{[^}]*\})',
            lambda m: m.group(0) + HEADER_CSS_INJECT,
            html, count=1, flags=re.DOTALL
        )

    if new_html != html:
        open(full, "w", encoding="utf-8").write(new_html)
        print(f"OK: {rel_path}")
        changed += 1
    else:
        print(f"UNCHANGED: {rel_path}")

print(f"\n完成：{changed} 个已更新")
