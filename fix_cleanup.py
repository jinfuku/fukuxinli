#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
删除虚假文章脚本：
1. 从 mind/index.html 删除「深度心理治疗案例分享」文章卡片
2. 从 index.html (首页) 删除相关文章链接
3. 删除 spirit/-p/ 垃圾目录
4. 在 spirit/index.html 添加「威尔菲德内勒斯核心概念术语翻译对照表」入口
"""

import os
import re
import shutil

BASE = r"c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website"

# ─────────────────────────────────────────
# 1. 从 mind/index.html 删除虚假文章卡片
# ─────────────────────────────────────────
mind_index = os.path.join(BASE, 'mind', 'index.html')
with open(mind_index, 'r', encoding='utf-8') as f:
    content = f.read()

# 用正则删除整个包含「深度心理治疗案例分享」的 article div
pattern = re.compile(
    r'\s*<div class="article">\s*<h3><a href="/fukuxinli/mind/%E6%B7%B1%E5%BA%A6%E5%BF%83%E7%90%86%E6%B2%BB%E7%96%97%E6%A1%88%E4%BE%8B%E5%88%86%E4%BA%AB/".*?</div>\s*</div>',
    re.DOTALL
)
new_content = pattern.sub('', content)
if new_content != content:
    with open(mind_index, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('[OK] Removed fake article card from mind/index.html')
else:
    print('[WARN] Article card not found in mind/index.html - may already be removed or URL differs')

# ─────────────────────────────────────────
# 2. 从首页 index.html 删除对应相关文章链接
# ─────────────────────────────────────────
home_index = os.path.join(BASE, 'index.html')
with open(home_index, 'r', encoding='utf-8') as f:
    content = f.read()

# 删除首页「相关文章」列表中的深度心理治疗案例分享链接
fake_link = r'\s*<li><a href="/fukuxinli/mind/%E6%B7%B1%E5%BA%A6%E5%BF%83%E7%90%86%E6%B2%BB%E7%96%97%E6%A1%88%E4%BE%8B%E5%88%86%E4%BA%AB/">深度心理治疗案例分享</a></li>'
new_content = re.sub(fake_link, '', content)
if new_content != content:
    with open(home_index, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('[OK] Removed fake article link from home index.html')
else:
    print('[INFO] Link not found in home index.html (already removed or not present)')

# ─────────────────────────────────────────
# 3. 删除 spirit/-p/ 垃圾目录
# ─────────────────────────────────────────
junk_dir = os.path.join(BASE, 'spirit', '-p')
if os.path.isdir(junk_dir):
    shutil.rmtree(junk_dir)
    print('[OK] Deleted junk directory: spirit/-p/')
else:
    print('[INFO] spirit/-p/ not found (already deleted or does not exist)')

# ─────────────────────────────────────────
# 4. 在 spirit/index.html 添加「威尔菲德内勒斯核心概念术语翻译对照表」文章入口
# ─────────────────────────────────────────
spirit_index = os.path.join(BASE, 'spirit', 'index.html')
with open(spirit_index, 'r', encoding='utf-8') as f:
    content = f.read()

target_url = '%E5%A8%81%E5%B0%94%E8%8F%B2%E5%BE%B7%E5%86%85%E5%8B%92%E6%96%AF%E6%A0%B8%E5%BF%83%E6%A6%82%E5%BF%B5%E6%9C%AF%E8%AF%AD%E7%BF%BB%E8%AF%91%E5%AF%B9%E7%85%A7%E8%A1%A8'
if target_url in content:
    print('[SKIP] Nelles term table already listed in spirit/index.html')
else:
    # 在第一个 <div class="article"> 前插入新文章卡片
    new_card = """
        <div class="article">
          <h3><a href="/fukuxinli/spirit/%E5%A8%81%E5%B0%94%E8%8F%B2%E5%BE%B7%E5%86%85%E5%8B%92%E6%96%AF%E6%A0%B8%E5%BF%83%E6%A6%82%E5%BF%B5%E6%9C%AF%E8%AF%AD%E7%BF%BB%E8%AF%91%E5%AF%B9%E7%85%A7%E8%A1%A8/">威尔菲德·内勒斯核心概念术语翻译对照表</a></h3>
          <div class="meta">
            <span>[神]</span>
            <span>2026-03-14</span>
          </div>
          <div class="summary">
            <p>威尔菲德·内勒斯生命整合学院核心概念术语的中英德三语翻译对照表，涵盖意识发展阶段、生命整合过程排列（LIP）等核心词汇，为学习者提供精准的术语参考。</p>
          </div>
        </div>

"""
    content = content.replace(
        '\n        <div class="article">',
        new_card + '        <div class="article">',
        1
    )
    with open(spirit_index, 'w', encoding='utf-8') as f:
        f.write(content)
    print('[OK] Added Nelles term table article to spirit/index.html')

print('\nAll done!')
