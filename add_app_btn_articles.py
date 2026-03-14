import os, re

base = r'c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website'

# APP 访问按钮 HTML（用在文章页右侧栏）
APP_BTN_RIGHT = '''
      <!-- 访问手机APP按钮 -->
      <div style="margin-top:20px;padding-top:18px;border-top:1px solid #f0f0f0;">
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

article_pages = []
for cat in ['spirit', 'mind', 'body', 'partnership', 'ai']:
    cat_path = os.path.join(base, cat)
    if not os.path.isdir(cat_path):
        continue
    for d in os.listdir(cat_path):
        fp = os.path.join(cat_path, d, 'index.html')
        if os.path.isfile(fp):
            article_pages.append(fp)

added = 0
skipped = 0
no_sidebar = 0

for fpath in article_pages:
    with open(fpath, encoding='utf-8') as f:
        html = f.read()
    if '访问手机版APP' in html:
        skipped += 1
        continue
    # 文章页右侧栏结束标记
    if '</aside>\n  </div>' in html:
        html = html.replace('</aside>\n  </div>', APP_BTN_RIGHT + '\n    </aside>\n  </div>', 1)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        added += 1
    elif '</aside>\n</div>' in html:
        html = html.replace('</aside>\n</div>', APP_BTN_RIGHT + '\n    </aside>\n</div>', 1)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        added += 1
    else:
        # 没有右侧栏的文章页（新版），插在 footer 前
        if '<footer>' in html and '访问手机版APP' not in html:
            # 在关注我们区块前加一个浮动按钮
            floating_btn = '''
  <!-- 手机APP浮动按钮 -->
  <div style="position:fixed;bottom:80px;right:20px;z-index:9999;">
    <a href="https://jinfuku.github.io/fukuxinli/app/" target="_blank"
       style="display:flex;align-items:center;gap:8px;padding:10px 16px;
              background:linear-gradient(135deg,#00c853 0%,#2196f3 100%);
              color:white;text-decoration:none;border-radius:50px;
              font-size:13px;font-weight:600;
              box-shadow:0 4px 18px rgba(0,200,83,0.4);">
      <span style="font-size:18px;">📱</span>手机版APP
    </a>
  </div>'''
            html = html.replace('<footer>', floating_btn + '\n  <footer>', 1)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
            added += 1
        else:
            no_sidebar += 1

print(f'APP button: added to {added} article pages, skipped {skipped}, no-match {no_sidebar}')
