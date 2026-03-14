import os, shutil

src = r'c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website/partnership/马尔特伴侣关系整合过程排列BIP'
dst = r'c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website/partnership/马尔特伴侣关系整合过程BIP'

# 创建新目录（正确的路径）
os.makedirs(dst, exist_ok=True)
print(f'Created: {dst}')

# 读取现有文章内容
with open(src + '/index.html', encoding='utf-8') as f:
    html = f.read()

# 在文章正文底部（highlight-box 关于马尔特的框之后）插入公众号二维码展示块
qr_insert = '''
      <div style="margin:32px 0 0;padding:28px 24px;background:linear-gradient(135deg,#e8f5e9,#e3f2fd);border-radius:16px;text-align:center;border:1px solid rgba(0,200,83,0.15);">
        <p style="font-size:15px;color:#2e7d32;font-weight:600;margin:0 0 16px;">📱 关注福库身心同调公众号，获取更多内容</p>
        <img src="/fukuxinli/images/qrcode-mp.jpg" alt="福库身心同调公众号二维码" style="width:180px;height:180px;object-fit:contain;border-radius:12px;border:2px solid rgba(0,200,83,0.2);display:block;margin:0 auto 14px;box-shadow:0 4px 16px rgba(0,0,0,0.1);">
        <p style="font-size:13px;color:#86868b;margin:0;">打开微信，扫一扫即可关注</p>
        <p style="font-size:12px;color:#aaa;margin:8px 0 0;">本文由内勒斯博士授权翻译，更多内容请关注公众号</p>
      </div>
'''

# 在 </div><!-- article-body end --> 的 highlight-box 关于马尔特之后插入
old_marker = '''      <div class="highlight-box">
        <p><strong>关于马尔特·内勒斯（Malte Nelles）</strong>'''
new_marker = qr_insert + '\n      <div class="highlight-box">\n        <p><strong>关于马尔特·内勒斯（Malte Nelles）</strong>'

if old_marker in html:
    html = html.replace(old_marker, new_marker, 1)
    print('QR block inserted before author highlight box')
else:
    # fallback: insert before </div>\n  </div>\n\n  <a href=...back-link
    html = html.replace(
        '    </div>\n  </div>\n\n  <a href="/fukuxinli/partnership/" class="back-link">← 返回伴侣关系</a>',
        qr_insert + '\n    </div>\n  </div>\n\n  <a href="/fukuxinli/partnership/" class="back-link">← 返回伴侣关系</a>'
    )
    print('QR block inserted (fallback)')

with open(dst + '/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done! Written to:', dst + '/index.html')
