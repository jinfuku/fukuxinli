# -*- coding: utf-8 -*-
"""
更新主页到增强版
1. 添加社交媒体区域
2. 添加平台logo图标
3. 更新样式
"""

import sys
import io
from pathlib import Path

# 设置输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def add_social_media_section():
    """在主页添加社交媒体区域"""
    main_file = Path("c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website/index.html")
    enhanced_file = Path("c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website/index-enhanced.html")

    # 读取主页
    with open(main_file, 'r', encoding='utf-8') as f:
        main_content = f.read()

    # 读取增强版
    with open(enhanced_file, 'r', encoding='utf-8') as f:
        enhanced_content = f.read()

    # 提取社交媒体CSS
    import re
    css_pattern = r'/\*\s*=\s*=+\s*社交媒体区域样式\s*=+\s*\*/(.+?)/\*\s*=\s*=+\s*新增国际社交媒体图标\s*=+\s*\*/'
    css_match = re.search(css_pattern, enhanced_content, re.DOTALL)

    if css_match:
        social_css = css_match.group(1)

        # 在</style>前添加社交媒体CSS
        main_content = main_content.replace('</style>', f'{social_css}\n  </style>')

    # 提取社交媒体HTML
    social_start = '<!-- 社交媒体链接区域 -->'
    social_end = '</section>'
    social_section_start = enhanced_content.find(social_start)
    social_section_end = enhanced_content.find(social_end, social_section_start) + len(social_end)

    if social_section_start > 0:
        social_html = enhanced_content[social_section_start:social_section_end]

        # 在footer之前添加社交媒体区域
        footer_pattern = '  <footer>'
        if footer_pattern in main_content:
            main_content = main_content.replace(footer_pattern, f'{social_html}\n\n  {footer_pattern}')

    # 写回文件
    with open(main_file, 'w', encoding='utf-8') as f:
        f.write(main_content)

    print("✓ 已添加社交媒体区域到主页")

def add_social_icons_svg():
    """添加SVG图标（如果需要）"""
    print("✓ 社交媒体区域已包含CSS样式图标")

def update_app_links():
    """更新APP中的链接指向增强版主页"""
    app_file = Path("c:/Users/jinfu/WorkBuddy/Claw/fuku-app/index.html")

    with open(app_file, 'r', encoding='utf-8') as f:
        app_content = f.read()

    # 更新网站URL为增强版
    app_content = app_content.replace(
        "const websiteUrl = 'https://jinfuku.github.io/fukuxinli/';",
        "const websiteUrl = 'https://jinfuku.github.io/fukuxinli/index-enhanced.html';"
    )

    # 写回文件
    with open(app_file, 'w', encoding='utf-8') as f:
        f.write(app_content)

    print("✓ 已更新APP链接指向增强版主页")

def copy_to_public():
    """复制更新后的主页到public目录"""
    import shutil

    main_file = Path("c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website/index.html")
    public_file = Path("c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website/public/index.html")

    shutil.copy2(main_file, public_file)
    print("✓ 已同步更新到public目录")

def main():
    print("=" * 60)
    print("更新主页到增强版")
    print("=" * 60)
    print()

    add_social_media_section()
    add_social_icons_svg()
    update_app_links()
    copy_to_public()

    print()
    print("=" * 60)
    print("更新完成！")
    print("=" * 60)
    print()
    print("更新内容：")
    print("1. ✓ 添加社交媒体区域（微信公众号、视频号、B站、小红书等）")
    print("2. ✓ 添加平台图标样式")
    print("3. ✓ 更新APP链接指向增强版主页")
    print("4. ✓ 同步到public目录")
    print()
    print("下一步：")
    print("1. 查看更新效果")
    print("2. 提交到GitHub")
    print()

if __name__ == "__main__":
    main()
