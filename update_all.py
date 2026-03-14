import os, re
from urllib.parse import quote

base = r'c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website'

# APP 访问按钮 HTML（放在侧边栏分类目录 </ul> 之后）
APP_BTN = '''
      <!-- 访问手机APP按钮 -->
      <div style="margin-top:20px;">
        <a href="https://jinfuku.github.io/fukuxinli/app/" target="_blank"
           style="display:flex;align-items:center;gap:10px;padding:12px 16px;
                  background:linear-gradient(135deg,#00c853 0%,#2196f3 100%);
                  color:white;text-decoration:none;border-radius:12px;
                  font-size:14px;font-weight:600;
                  box-shadow:0 4px 14px rgba(0,200,83,0.3);
                  transition:all 0.3s cubic-bezier(.4,0,.2,1);"
           onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 20px rgba(0,200,83,0.4)'"
           onmouseout="this.style.transform='';this.style.boxShadow='0 4px 14px rgba(0,200,83,0.3)'">
          <span style="font-size:22px;">📱</span>
          <div>
            <div>访问手机版APP</div>
            <div style="font-size:11px;opacity:0.85;font-weight:400;margin-top:2px;">随时随地阅读</div>
          </div>
        </a>
      </div>'''

# 要处理的所有分类页
category_pages = [
    os.path.join(base, 'spirit', 'index.html'),
    os.path.join(base, 'mind', 'index.html'),
    os.path.join(base, 'body', 'index.html'),
    os.path.join(base, 'partnership', 'index.html'),
    os.path.join(base, 'ai', 'index.html'),
    os.path.join(base, 'about', 'index.html'),
]

# 所有文章页（递归找）
article_pages = []
for cat in ['spirit', 'mind', 'body', 'partnership', 'ai']:
    cat_path = os.path.join(base, cat)
    for d in os.listdir(cat_path):
        fp = os.path.join(cat_path, d, 'index.html')
        if os.path.isfile(fp):
            article_pages.append(fp)

all_pages = category_pages + article_pages

# ============================================================
# 给所有页面侧边栏加 APP 按钮
# ============================================================
MARKER = '<h3>分类目录</h3>'
added = 0
skipped = 0
for fpath in all_pages:
    if not os.path.isfile(fpath):
        continue
    with open(fpath, encoding='utf-8') as f:
        html = f.read()
    if '访问手机版APP' in html:
        skipped += 1
        continue
    if MARKER not in html:
        print(f'  No sidebar found: {fpath}')
        skipped += 1
        continue
    # 找到侧边栏 </ul> 后面插入
    # 找第一个 <h3>分类目录</h3> 后的第一个 </ul>
    idx = html.find(MARKER)
    ul_end = html.find('</ul>', idx)
    if ul_end == -1:
        print(f'  No </ul> after sidebar: {fpath}')
        continue
    insert_pos = ul_end + len('</ul>')
    html = html[:insert_pos] + APP_BTN + html[insert_pos:]
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    added += 1

print(f'APP button: added to {added} pages, skipped {skipped}')

# ============================================================
# 更新 spirit/index.html：加入3篇迁移来的文章
# ============================================================
spirit_idx = os.path.join(base, 'spirit', 'index.html')
with open(spirit_idx, encoding='utf-8') as f:
    html = f.read()

new_articles = '''
        <div class="article">
          <h3><a href="/fukuxinli/spirit/%E7%B3%BB%E7%BB%9F%E6%8E%92%E5%88%97%E7%94%9F%E5%91%BD%E6%95%B4%E5%90%88%E9%97%AD%E9%97%A8%E8%AF%BB%E4%B9%A6%E4%BC%9A%E6%8B%9B%E5%8B%9F/">招募 | 系统排列&amp;生命整合闭门读书会</a></h3>
          <div class="meta">
            <span>[神 · 生命整合]</span>
            <span>2026-03-14</span>
          </div>
          <div class="summary">
            <p>2年读书会：4次个案权益、共读11本内勒斯生命整合系列新书、每周腾讯会议讲书、问答次数不限。第二期读书会成员招募中。</p>
          </div>
        </div>

        <div class="article">
          <h3><a href="/fukuxinli/spirit/%E7%A6%8F%E5%BA%93%E5%BF%83%E7%90%86%E7%B3%BB%E7%BB%9F%E6%8E%92%E5%88%97%E7%94%9F%E5%91%BD%E6%95%B4%E5%90%88%E8%BF%9B%E4%BF%AE%E7%8F%AD/">福库心理系统排列&amp;生命整合进修班</a></h3>
          <div class="meta">
            <span>[神 · 生命整合]</span>
            <span>2026-03-14</span>
          </div>
          <div class="summary">
            <p>内勒斯博士最新编写的系统排列&amp;生命整合继续教育课程，16小时8个模块，涵盖意识发展7个阶段，由靳福库（内勒斯生命整合学院授权导师）主讲。</p>
          </div>
        </div>

        <div class="article">
          <h3><a href="/fukuxinli/spirit/%E6%88%91%E4%BB%AC%E7%94%9F%E6%B4%BB%E7%9A%84%E4%B8%96%E7%95%8C%E6%84%8F%E8%AF%86%E4%B8%8E%E7%B2%BE%E7%A5%9E%E4%B9%8B%E6%97%85%E7%9B%AE%E5%BD%95/">《我们生活的世界——意识与精神之旅》目录</a></h3>
          <div class="meta">
            <span>[神 · 生命整合]</span>
            <span>2026-03-14</span>
          </div>
          <div class="summary">
            <p>威尔菲德·内勒斯2020年德语著作目录。通过7个生命与意识阶段，从共生统一意识到全意识（死亡），呈现生命与意识发展的全景图。</p>
          </div>
        </div>
'''

# 插入在文章列表最前面
marker = '<h2>神（意识、生命整合）</h2>\n\n      \n\n        <div class="article">'
if marker in html and '系统排列生命整合闭门读书会招募' not in html:
    html = html.replace(
        '<h2>神（意识、生命整合）</h2>\n\n      \n\n        <div class="article">',
        '<h2>神（意识、生命整合）</h2>\n\n      ' + new_articles + '\n        <div class="article">'
    )
    with open(spirit_idx, 'w', encoding='utf-8') as f:
        f.write(html)
    print('spirit/index.html: 3 articles added')
else:
    print('spirit/index.html: articles already present or marker not found')

# ============================================================
# 更新 mind/index.html：移除3篇已迁移的文章
# ============================================================
mind_idx = os.path.join(base, 'mind', 'index.html')
with open(mind_idx, encoding='utf-8') as f:
    html = f.read()

# 移除这3篇（用正则匹配 article div）
patterns_to_remove = [
    r'\s*<div class="article">\s*<h3><a href="/fukuxinli/mind/%E7%B3%BB%E7%BB%9F%E6%8E%92%E5%88%97%E7%94%9F%E5%91%BD%E6%95%B4%E5%90%88%E9%97%AD%E9%97%A8%E8%AF%BB%E4%B9%A6%E4%BC%9A%E6%8B%9B%E5%8B%9F/">[^<]+</a></h3>.*?</div>\s*</div>',
    r'\s*<div class="article">\s*<h3><a href="/fukuxinli/mind/%E7%A6%8F%E5%BA%93%E5%BF%83%E7%90%86%E7%B3%BB%E7%BB%9F%E6%8E%92%E5%88%97%E7%94%9F%E5%91%BD%E6%95%B4%E5%90%88%E8%BF%9B%E4%BF%AE%E7%8F%AD/">[^<]+</a></h3>.*?</div>\s*</div>',
    r'\s*<div class="article">\s*<h3><a href="/fukuxinli/mind/%E6%88%91%E4%BB%AC%E7%94%9F%E6%B4%BB%E7%9A%84%E4%B8%96%E7%95%8C%E6%84%8F%E8%AF%86%E4%B8%8E%E7%B2%BE%E7%A5%9E%E4%B9%8B%E6%97%85%E7%9B%AE%E5%BD%95/">[^<]+</a></h3>.*?</div>\s*</div>',
]
removed = 0
for p in patterns_to_remove:
    new_html, n = re.subn(p, '', html, flags=re.DOTALL)
    if n:
        html = new_html
        removed += n

with open(mind_idx, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'mind/index.html: removed {removed} migrated articles')

# ============================================================
# 更新 APP (fuku-app/index.html)：3篇文章 category 改为 神，URL 改为 spirit
# ============================================================
app_file = r'c:/Users/jinfu/WorkBuddy/Claw/fuku-app/index.html'
with open(app_file, encoding='utf-8') as f:
    app_html = f.read()

# 1. 招募读书会
app_html = app_html.replace(
    "title: '招募 | 系统排列&生命整合闭门读书会',\n                category: '心',",
    "title: '招募 | 系统排列&生命整合闭门读书会',\n                category: '神',"
)
app_html = app_html.replace(
    "url: 'https://jinfuku.github.io/fukuxinli/mind/%E7%B3%BB%E7%BB%9F%E6%8E%92%E5%88%97%E7%94%9F%E5%91%BD%E6%95%B4%E5%90%88%E9%97%AD%E9%97%A8%E8%AF%BB%E4%B9%A6%E4%BC%9A%E6%8B%9B%E5%8B%9F/'",
    "url: 'https://jinfuku.github.io/fukuxinli/spirit/%E7%B3%BB%E7%BB%9F%E6%8E%92%E5%88%97%E7%94%9F%E5%91%BD%E6%95%B4%E5%90%88%E9%97%AD%E9%97%A8%E8%AF%BB%E4%B9%A6%E4%BC%9A%E6%8B%9B%E5%8B%9F/'"
)

# 2. 进修班
app_html = app_html.replace(
    "title: '福库心理系统排列&生命整合进修班',\n                category: '心',",
    "title: '福库心理系统排列&生命整合进修班',\n                category: '神',"
)
app_html = app_html.replace(
    "url: 'https://jinfuku.github.io/fukuxinli/mind/%E7%A6%8F%E5%BA%93%E5%BF%83%E7%90%86%E7%B3%BB%E7%BB%9F%E6%8E%92%E5%88%97%E7%94%9F%E5%91%BD%E6%95%B4%E5%90%88%E8%BF%9B%E4%BF%AE%E7%8F%AD/'",
    "url: 'https://jinfuku.github.io/fukuxinli/spirit/%E7%A6%8F%E5%BA%93%E5%BF%83%E7%90%86%E7%B3%BB%E7%BB%9F%E6%8E%92%E5%88%97%E7%94%9F%E5%91%BD%E6%95%B4%E5%90%88%E8%BF%9B%E4%BF%AE%E7%8F%AD/'"
)

# 3. 《我们生活的世界》
app_html = app_html.replace(
    "title: '《我们生活的世界——意识与精神之旅》目录',\n                category: '心',",
    "title: '《我们生活的世界——意识与精神之旅》目录',\n                category: '神',"
)
app_html = app_html.replace(
    "url: 'https://jinfuku.github.io/fukuxinli/mind/%E6%88%91%E4%BB%AC%E7%94%9F%E6%B4%BB%E7%9A%84%E4%B8%96%E7%95%8C%E6%84%8F%E8%AF%86%E4%B8%8E%E7%B2%BE%E7%A5%9E%E4%B9%8B%E6%97%85%E7%9B%AE%E5%BD%95/'",
    "url: 'https://jinfuku.github.io/fukuxinli/spirit/%E6%88%91%E4%BB%AC%E7%94%9F%E6%B4%BB%E7%9A%84%E4%B8%96%E7%95%8C%E6%84%8F%E8%AF%86%E4%B8%8E%E7%B2%BE%E7%A5%9E%E4%B9%8B%E6%97%85%E7%9B%AE%E5%BD%95/'"
)

with open(app_file, 'w', encoding='utf-8') as f:
    f.write(app_html)
print('fuku-app/index.html: 3 articles updated to category 神 with spirit URLs')

print('\nAll tasks completed!')
