#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量处理所有分类页 + 文章页：
1. 把旧导航样式替换为首页那种毛玻璃 Apple 风格导航
2. 把关注我们区块里的静态小二维码卡片改为图标样式（去掉小图，改为弹窗）
3. 确保弹窗 HTML + JS 存在
"""
import os, re

BASE = r"c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website"

# ─────────────────────────────────────────────
# 需要处理的页面（分类页 + 文章页，不含首页/about）
# ─────────────────────────────────────────────
PAGES = [
    "spirit/index.html",
    "mind/index.html",
    "body/index.html",
    "partnership/index.html",
    "ai/index.html",
    "about/index.html",
    # 文章页
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

# ─────────────────────────────────────────────
# 旧导航 CSS（各页面有细微差异，用正则匹配整个块）
# ─────────────────────────────────────────────
OLD_NAV_CSS_PATTERN = re.compile(
    r'(/\*.*?[Nn]av.*?\*/\s*)?'
    r'nav\s+ul\s*\{[^}]*\}\s*'
    r'nav\s+a\s*\{[^}]*\}\s*'
    r'nav\s+a:hover\s*\{[^}]*\}',
    re.DOTALL
)

NEW_NAV_CSS = """    /* Navigation with Apple-style glass cards */
    nav ul {
      list-style: none;
      display: flex;
      gap: 15px;
      flex-wrap: wrap;
      justify-content: center;
    }

    nav a {
      color: white;
      text-decoration: none;
      font-size: 15px;
      font-weight: 500;
      padding: 10px 20px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1),
                  inset 0 1px 0 rgba(255, 255, 255, 0.2);
      border: 1px solid rgba(255, 255, 255, 0.2);
      display: inline-block;
    }

    nav a:hover {
      background: rgba(255, 255, 255, 0.25);
      transform: translateY(-2px);
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15),
                  0 4px 8px rgba(0, 0, 0, 0.1),
                  inset 0 1px 0 rgba(255, 255, 255, 0.3);
    }

    nav a:active {
      transform: translateY(0);
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1),
                  inset 0 2px 4px rgba(0, 0, 0, 0.1);
    }"""

# 旧 header CSS（仅有 background + shadow，没有 sticky/backdrop）
OLD_HEADER_SIMPLE = re.compile(
    r'(header\s*\{)'
    r'([^}]*background[^}]*)'
    r'(\})',
    re.DOTALL
)

NEW_HEADER_ADDITIONS = """\n      position: sticky;\n      top: 0;\n      z-index: 1000;\n      backdrop-filter: blur(20px);\n      -webkit-backdrop-filter: blur(20px);\n      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12),\n                  0 1px 3px rgba(0, 0, 0, 0.08);"""

# ─────────────────────────────────────────────
# 旧二维码卡片（带小图）→ 新卡片（图标 + 弹窗）
# ─────────────────────────────────────────────
OLD_QR_MP = re.compile(
    r'<a\s+href="#"\s+class="social-card qr-card"\s+onclick="return false;"\s+style="cursor:default;">\s*'
    r'<div class="qr-img-wrap"><img[^>]*qrcode-mp[^>]*></div>\s*'
    r'<h3>微信公众号</h3><p>福库身心同调</p><span class="qr-hint">扫码关注</span>\s*'
    r'</a>',
    re.DOTALL
)
NEW_QR_MP = '''<a href="#" class="social-card" onclick="event.preventDefault();showQrModal('扫码关注微信公众号');">
          <div class="social-icon wechat-icon"></div><h3>微信公众号</h3><p>福库身心同调</p><span class="qr-hint">点击扫码关注</span>
        </a>'''

OLD_QR_VIDEO = re.compile(
    r'<a\s+href="#"\s+class="social-card qr-card"\s+onclick="return false;"\s+style="cursor:default;">\s*'
    r'<div class="qr-img-wrap"><img[^>]*qrcode-video[^>]*></div>\s*'
    r'<h3>微信视频号</h3><p>福库身心同调</p><span class="qr-hint">扫码观看</span>\s*'
    r'</a>',
    re.DOTALL
)
NEW_QR_VIDEO = '''<a href="#" class="social-card" onclick="event.preventDefault();showQrModal('扫码观看微信视频号');">
          <div class="social-icon video-icon"></div><h3>微信视频号</h3><p>福库身心同调</p><span class="qr-hint">点击扫码观看</span>
        </a>'''

# ─────────────────────────────────────────────
# 弹窗 HTML + JS（注入在 </body> 前，如果还没有的话）
# ─────────────────────────────────────────────
QR_MODAL_HTML = """
  <!-- 二维码弹窗 -->
  <div id="qrModal" class="qr-modal" onclick="closeQrModal(event)">
    <div class="qr-modal-content">
      <span class="close-btn" onclick="closeQrModal()">&times;</span>
      <h3 id="qrTitle">扫码关注</h3>
      <img id="qrImage" src="/fukuxinli/images/qrcode-mp.jpg" alt="二维码" style="width:220px;height:220px;object-fit:contain;border-radius:12px;border:1px solid #e5e5e7;display:block;margin:0 auto 16px;">
      <p id="qrDesc" style="color:#86868b;font-size:14px;margin:0;">打开微信，扫一扫即可关注</p>
    </div>
  </div>
  <script>
    function showQrModal(title) {
      var modal = document.getElementById('qrModal');
      var qrTitle = document.getElementById('qrTitle');
      var qrImage = document.getElementById('qrImage');
      var qrDesc  = document.getElementById('qrDesc');
      qrTitle.textContent = title;
      if (title && title.indexOf('视频号') !== -1) {
        qrImage.src = '/fukuxinli/images/qrcode-video.jpg';
        qrImage.alt = '视频号二维码';
        qrDesc.textContent = '打开微信，扫一扫即可观看视频号';
      } else {
        qrImage.src = '/fukuxinli/images/qrcode-mp.jpg';
        qrImage.alt = '公众号二维码';
        qrDesc.textContent = '打开微信，扫一扫即可关注公众号';
      }
      modal.classList.add('active');
    }
    function closeQrModal(event) {
      if (!event || event.target.id === 'qrModal') {
        document.getElementById('qrModal').classList.remove('active');
      }
    }
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeQrModal();
    });
  </script>"""

# 弹窗 CSS（注入在 </style> 前，如果还没有的话）
QR_MODAL_CSS = """
    /* 二维码弹窗 */
    .qr-modal {
      display: none; position: fixed; z-index: 10000;
      left: 0; top: 0; width: 100%; height: 100%;
      background-color: rgba(0,0,0,0.7);
      backdrop-filter: blur(5px); -webkit-backdrop-filter: blur(5px);
      align-items: center; justify-content: center;
    }
    .qr-modal.active { display: flex; }
    .qr-modal-content {
      background: white; border-radius: 20px; padding: 40px;
      max-width: 320px; width: 90%; text-align: center; position: relative;
      box-shadow: 0 20px 60px rgba(0,0,0,0.3);
      animation: modalIn 0.3s ease;
    }
    @keyframes modalIn { from { opacity:0; transform: translateY(-20px); } to { opacity:1; transform: translateY(0); } }
    .qr-modal-content h3 { font-size: 20px; color: #1d1d1f; margin-bottom: 20px; font-weight: 600; }
    .close-btn {
      position: absolute; top: 14px; right: 18px;
      font-size: 24px; cursor: pointer; color: #86868b; line-height: 1;
    }
    .close-btn:hover { color: #1d1d1f; }
    /* 微信公众号图标 */
    .wechat-icon { background: linear-gradient(135deg,#07c160 0%,#06ad56 100%); color:white; box-shadow: 0 4px 12px rgba(7,193,96,0.3); }
    .wechat-icon::after { content:'微'; }
    /* 视频号图标 */
    .video-icon { background: linear-gradient(135deg,#faad14 0%,#f5923e 100%); color:white; box-shadow: 0 4px 12px rgba(250,173,20,0.3); }
    .video-icon::after { content:'▶'; }"""

# ─────────────────────────────────────────────
# 主处理函数
# ─────────────────────────────────────────────
changed = 0
skipped = 0

for rel_path in PAGES:
    full_path = os.path.join(BASE, rel_path).replace("/", os.sep)
    if not os.path.exists(full_path):
        print(f"  SKIP (not found): {rel_path}")
        skipped += 1
        continue

    with open(full_path, "r", encoding="utf-8") as f:
        html = f.read()

    original = html

    # ── 1. 替换 header CSS：加上 sticky + backdrop-filter
    if "position: sticky" not in html and "position:sticky" not in html:
        html = re.sub(
            r'(header\s*\{)([^}]*)(box-shadow[^;]*;)',
            lambda m: m.group(1) + m.group(2) + m.group(3) +
                "\n      position: sticky;\n      top: 0;\n      z-index: 1000;\n      backdrop-filter: blur(20px);\n      -webkit-backdrop-filter: blur(20px);",
            html, count=1, flags=re.DOTALL
        )

    # ── 2. 替换 nav CSS
    match = OLD_NAV_CSS_PATTERN.search(html)
    if match:
        html = html[:match.start()] + NEW_NAV_CSS + html[match.end():]

    # ── 3. 去掉关注我们里的静态小二维码图，改为图标+弹窗
    html = OLD_QR_MP.sub(NEW_QR_MP, html)
    html = OLD_QR_VIDEO.sub(NEW_QR_VIDEO, html)

    # ── 4. 确保弹窗 CSS 存在
    if "qr-modal" not in html:
        html = html.replace("</style>", QR_MODAL_CSS + "\n  </style>", 1)

    # ── 5. 确保弹窗 HTML + JS 存在
    if "id=\"qrModal\"" not in html:
        html = html.replace("</body>", QR_MODAL_HTML + "\n</body>", 1)

    if html != original:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  OK: {rel_path}")
        changed += 1
    else:
        print(f"  UNCHANGED: {rel_path}")

print(f"\n完成：修改 {changed} 个，跳过 {skipped} 个")
