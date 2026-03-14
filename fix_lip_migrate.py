import os, shutil, re

base = r'c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website'

# ============================================================
# 任务1: 修复 LIP 404 - 创建正确目录名的文章（不带"排列"）
# ============================================================
lip_src = os.path.join(base, 'spirit', '内勒斯生命整合过程排列LIP')
lip_dst = os.path.join(base, 'spirit', '内勒斯生命整合过程LIP')

os.makedirs(lip_dst, exist_ok=True)
with open(lip_src + '/index.html', encoding='utf-8') as f:
    html = f.read()
# 导航链接保持不变，只写入新目录
with open(lip_dst + '/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'LIP: copied to {lip_dst}')

# ============================================================
# 任务2: 迁移3篇文章 mind -> spirit
# 文章目录名（mind下）→ 新目录名（spirit下）
# ============================================================
migrations = [
    ('系统排列生命整合闭门读书会招募', '系统排列生命整合闭门读书会招募'),
    ('福库心理系统排列生命整合进修班', '福库心理系统排列生命整合进修班'),
    ('我们生活的世界意识与精神之旅目录', '我们生活的世界意识与精神之旅目录'),
]

for dirname, newname in migrations:
    src = os.path.join(base, 'mind', dirname)
    dst = os.path.join(base, 'spirit', newname)
    if not os.path.isdir(src):
        print(f'SKIP (not found): {src}')
        continue
    os.makedirs(dst, exist_ok=True)
    with open(src + '/index.html', encoding='utf-8') as f:
        html = f.read()
    # 更新文章内部的返回链接：mind -> spirit
    html = html.replace('href="/fukuxinli/mind/"', 'href="/fukuxinli/spirit/"')
    html = html.replace('← 返回心', '← 返回神')
    html = html.replace('← 返回心理咨询', '← 返回神')
    # 更新 meta 标签分类
    html = html.replace('<span>心理咨询</span>', '<span>神 · 生命整合</span>')
    html = html.replace('<span>[心]</span>', '<span>[神 · 生命整合]</span>')
    with open(dst + '/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Migrated: mind/{dirname} -> spirit/{newname}')

print('All done.')
