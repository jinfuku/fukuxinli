import os, re, glob

WEBSITE_ROOT = r'c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website'

# 所有文章详情页（非分类首页）
ARTICLE_DIRS = ['body', 'mind', 'spirit', 'partnership', 'ai']
article_pages = []
for d in ARTICLE_DIRS:
    pattern = os.path.join(WEBSITE_ROOT, d, '*', 'index.html')
    article_pages.extend(glob.glob(pattern))

# 评论模块脚本注入标记 + 注入代码
COMMENTS_MARKER = 'comments.js'
COMMENTS_TAG = '\n<script src="/fukuxinli/js/comments.js"></script>\n'

# 公众号二维码卡片替换（旧内容 → 新内容带真实二维码）
OLD_MP_CARD = '<a href="#" class="social-card" onclick="return false;">\n          <div class="social-icon wechat-icon"></div><h3>微信公众号</h3><p>福库身心同调</p><span class="qr-hint">扫码关注</span>\n        </a>'
NEW_MP_CARD = '''<a href="#" class="social-card qr-card" onclick="return false;" style="cursor:default;">
          <div class="qr-img-wrap"><img src="/fukuxinli/images/qrcode-mp.jpg" alt="公众号二维码" class="qr-img"></div>
          <h3>微信公众号</h3><p>福库身心同调</p><span class="qr-hint">扫码关注</span>
        </a>'''

OLD_VIDEO_CARD = '<a href="#" class="social-card" onclick="return false;">\n          <div class="social-icon video-icon"></div><h3>微信视频号</h3><p>福库身心同调</p><span class="qr-hint">扫码观看</span>\n        </a>'
NEW_VIDEO_CARD = '''<a href="#" class="social-card qr-card" onclick="return false;" style="cursor:default;">
          <div class="qr-img-wrap"><img src="/fukuxinli/images/qrcode-video.jpg" alt="视频号二维码" class="qr-img"></div>
          <h3>微信视频号</h3><p>福库身心同调</p><span class="qr-hint">扫码观看</span>
        </a>'''

# 二维码卡片样式（插入到已有样式块之后，若未添加）
QR_STYLE = '''
    /* ─── 二维码卡片样式 ─── */
    .qr-card { padding: 14px 10px; }
    .qr-img-wrap { width: 100%; margin-bottom: 10px; }
    .qr-img { width: 100%; max-width: 120px; height: auto; display: block; margin: 0 auto; border-radius: 8px; border: 1px solid #e5e5e7; }
'''

def process_article(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # 1. 注入评论模块脚本（在 </body> 前）
    if COMMENTS_MARKER not in content:
        content = content.replace('</body>', COMMENTS_TAG + '</body>', 1)
        changed = True
        print('[Comments] Added to:', filepath)
    else:
        print('[Skip-comments] Already has:', filepath)

    # 2. 替换公众号二维码卡片
    if OLD_MP_CARD in content:
        content = content.replace(OLD_MP_CARD, NEW_MP_CARD)
        changed = True
        print('[QR-MP] Updated in:', filepath)

    # 3. 替换视频号二维码卡片
    if OLD_VIDEO_CARD in content:
        content = content.replace(OLD_VIDEO_CARD, NEW_VIDEO_CARD)
        changed = True
        print('[QR-Video] Updated in:', filepath)

    # 4. 添加二维码卡片样式（如果还没有）
    if 'qr-img-wrap' not in content and '.social-media-section' in content:
        content = content.replace('    /* ========== 关注我们区域样式 ========== */',
                                  '    /* ========== 关注我们区域样式 ========== */' + QR_STYLE)
        changed = True
        print('[QR-Style] Added to:', filepath)

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print('=== Processing %d article pages ===' % len(article_pages))
for p in article_pages:
    process_article(p)

# 同样处理分类首页（也有 social-media-section）
CATEGORY_PAGES = [os.path.join(WEBSITE_ROOT, d, 'index.html') for d in ARTICLE_DIRS]
print('\n=== Processing category pages ===')
for p in CATEGORY_PAGES:
    if os.path.exists(p):
        process_article(p)

# 处理 about/index.html
about_p = os.path.join(WEBSITE_ROOT, 'about', 'index.html')
print('\n=== Processing about page ===')
if os.path.exists(about_p):
    process_article(about_p)

print('\nAll done!')
