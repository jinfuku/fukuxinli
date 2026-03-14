/**
 * 福库心理 - 文章评论留言模块
 * 特性：
 *   - 纯前端 localStorage 存储，无需后端
 *   - 自动精选置顶：正向词汇 + 字数 + 综合评分
 *   - 表情选择、昵称、内容
 *   - 管理员模式：Ctrl+Shift+A 可删除评论
 */
(function () {
  'use strict';

  // ─── 精选评分算法 ─────────────────────────────────────────
  const POSITIVE_WORDS = [
    '感谢','谢谢','受益','收获','感动','深刻','启发','触动','成长','疗愈',
    '温暖','共鸣','认同','学到','实用','精彩','很好','棒','赞','喜欢',
    '有帮助','很有用','感悟','理解','开悟','清晰','豁然','感恩','真诚',
    '真实','用心','深入','专业','细致','建议','推荐','期待','继续','加油',
    '支持','敬佩','尊敬','钦佩','佩服','认真','踏实','有爱','心里','心中',
    '内心','灵魂','生命','身体','疾病','好转','改善','康复','希望','光明'
  ];
  const NEGATIVE_WORDS = ['垃圾','骗','差','假','烂','滚','蠢','傻','恶心','撒谎'];

  function scoreComment(c) {
    const text = c.content || '';
    const len = text.length;
    // 字数得分（100字满分10分，超过200字额外加分）
    let score = Math.min(len / 10, 10);
    if (len > 200) score += 3;
    // 正向词加分
    POSITIVE_WORDS.forEach(w => { if (text.includes(w)) score += 1.5; });
    // 负向词扣分
    NEGATIVE_WORDS.forEach(w => { if (text.includes(w)) score -= 10; });
    // 有昵称加分
    if (c.name && c.name.trim() !== '匿名') score += 1;
    // 最少字数：30字以上才有资格精选
    if (len < 30) score -= 5;
    return score;
  }

  // ─── 存储 key（每篇文章独立） ─────────────────────────────
  function getStorageKey() {
    return 'fuku_comments_' + encodeURIComponent(location.pathname);
  }

  function loadComments() {
    try { return JSON.parse(localStorage.getItem(getStorageKey()) || '[]'); }
    catch (e) { return []; }
  }

  function saveComments(list) {
    localStorage.setItem(getStorageKey(), JSON.stringify(list));
  }

  // ─── 时间格式化 ──────────────────────────────────────────
  function fmtTime(ts) {
    const d = new Date(ts);
    const pad = n => String(n).padStart(2, '0');
    return d.getFullYear() + '-' + pad(d.getMonth()+1) + '-' + pad(d.getDate())
      + ' ' + pad(d.getHours()) + ':' + pad(d.getMinutes());
  }

  // ─── 渲染单条评论 ─────────────────────────────────────────
  function renderComment(c, isTop) {
    const div = document.createElement('div');
    div.className = 'fuku-comment-item' + (isTop ? ' fuku-comment-featured' : '');
    div.dataset.id = c.id;

    const avatarColors = ['#00c853','#2196f3','#ff5722','#9c27b0','#ff9800','#009688','#e91e63','#3f51b5'];
    const colorIdx = (c.name || '匿名').charCodeAt(0) % avatarColors.length;
    const avatarColor = avatarColors[colorIdx];
    const initial = (c.name || '匿名').charAt(0).toUpperCase();
    const emoji = c.emoji || '💬';

    div.innerHTML =
      '<div class="fuku-comment-header">' +
        '<div class="fuku-comment-avatar" style="background:' + avatarColor + ';">' + initial + '</div>' +
        '<div class="fuku-comment-meta">' +
          '<span class="fuku-comment-name">' + escHtml(c.name || '匿名') + '</span>' +
          (isTop ? '<span class="fuku-featured-badge">✨ 精选</span>' : '') +
          '<span class="fuku-comment-time">' + fmtTime(c.ts) + '</span>' +
        '</div>' +
        '<div class="fuku-comment-emoji">' + emoji + '</div>' +
      '</div>' +
      '<div class="fuku-comment-body">' + escHtml(c.content) + '</div>' +
      '<div class="fuku-comment-actions">' +
        '<button class="fuku-like-btn" data-id="' + c.id + '">' +
          '👍 <span class="fuku-like-count">' + (c.likes || 0) + '</span>' +
        '</button>' +
      '</div>';

    // 点赞
    div.querySelector('.fuku-like-btn').addEventListener('click', function() {
      const likedKey = 'fuku_liked_' + c.id;
      if (localStorage.getItem(likedKey)) { return; }
      const list = loadComments();
      const target = list.find(x => x.id === c.id);
      if (target) {
        target.likes = (target.likes || 0) + 1;
        saveComments(list);
        this.querySelector('.fuku-like-count').textContent = target.likes;
        localStorage.setItem(likedKey, '1');
        this.style.color = '#00c853';
      }
    });

    return div;
  }

  function escHtml(str) {
    return String(str)
      .replace(/&/g,'&amp;').replace(/</g,'&lt;')
      .replace(/>/g,'&gt;').replace(/"/g,'&quot;')
      .replace(/\n/g,'<br>');
  }

  // ─── 渲染评论列表 ─────────────────────────────────────────
  function renderList(container, listEl, comments) {
    listEl.innerHTML = '';
    if (!comments.length) {
      listEl.innerHTML = '<div class="fuku-comment-empty">暂无留言，来留下你的第一条感想吧 🌱</div>';
      return;
    }
    // 精选：评分最高且 score>5 的前3条
    const scored = comments.map(c => ({ c, s: scoreComment(c) })).sort((a,b) => b.s - a.s);
    const featuredIds = new Set(scored.filter(x => x.s > 5).slice(0, 3).map(x => x.c.id));
    // 先显示精选，再显示其余（按时间倒序）
    const featured = comments.filter(c => featuredIds.has(c.id)).sort((a,b) => b.ts - a.ts);
    const rest = comments.filter(c => !featuredIds.has(c.id)).sort((a,b) => b.ts - a.ts);
    [...featured, ...rest].forEach(c => {
      listEl.appendChild(renderComment(c, featuredIds.has(c.id)));
    });
  }

  // ─── 构建整个评论区 HTML ──────────────────────────────────
  function buildCommentSection() {
    const section = document.createElement('section');
    section.id = 'fuku-comments';
    section.innerHTML = `
<style>
#fuku-comments{max-width:860px;margin:48px auto 0;padding:0 20px 60px;font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;}
.fuku-comments-title{font-size:22px;font-weight:700;color:#1d1d1f;margin-bottom:6px;display:flex;align-items:center;gap:8px;}
.fuku-comments-subtitle{font-size:14px;color:#86868b;margin-bottom:28px;}
.fuku-comment-form{background:#fff;border-radius:18px;padding:24px;box-shadow:0 4px 20px rgba(0,0,0,.07);border:1px solid #e5e5e7;margin-bottom:36px;}
.fuku-form-row{display:flex;gap:12px;margin-bottom:14px;flex-wrap:wrap;}
.fuku-input{flex:1;min-width:160px;border:1.5px solid #e5e5e7;border-radius:10px;padding:10px 14px;font-size:14px;color:#1d1d1f;outline:none;transition:border-color .2s,box-shadow .2s;background:#fafafa;}
.fuku-input:focus{border-color:#00c853;box-shadow:0 0 0 3px rgba(0,200,83,.12);background:#fff;}
.fuku-emoji-row{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px;}
.fuku-emoji-btn{width:36px;height:36px;border-radius:50%;border:2px solid #e5e5e7;background:#fafafa;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .2s;}
.fuku-emoji-btn:hover,.fuku-emoji-btn.active{border-color:#00c853;background:#f0fff6;transform:scale(1.15);}
.fuku-textarea{width:100%;border:1.5px solid #e5e5e7;border-radius:12px;padding:12px 14px;font-size:14px;color:#1d1d1f;resize:vertical;min-height:100px;outline:none;transition:border-color .2s,box-shadow .2s;background:#fafafa;line-height:1.7;font-family:inherit;}
.fuku-textarea:focus{border-color:#00c853;box-shadow:0 0 0 3px rgba(0,200,83,.12);background:#fff;}
.fuku-char-count{font-size:12px;color:#86868b;text-align:right;margin-top:6px;}
.fuku-submit-row{display:flex;align-items:center;justify-content:space-between;margin-top:16px;flex-wrap:wrap;gap:10px;}
.fuku-submit-hint{font-size:12px;color:#86868b;line-height:1.5;}
.fuku-submit-btn{background:linear-gradient(135deg,#00c853,#2196f3);color:white;border:none;padding:11px 28px;border-radius:12px;font-size:14px;font-weight:600;cursor:pointer;transition:opacity .2s,transform .15s;}
.fuku-submit-btn:hover{opacity:.88;transform:translateY(-1px);}
.fuku-submit-btn:active{transform:translateY(0);}
.fuku-comment-list{display:flex;flex-direction:column;gap:16px;}
.fuku-comment-item{background:#fff;border-radius:16px;padding:20px 22px;box-shadow:0 2px 10px rgba(0,0,0,.06);border:1px solid #e5e5e7;transition:box-shadow .2s;}
.fuku-comment-item:hover{box-shadow:0 6px 20px rgba(0,0,0,.1);}
.fuku-comment-featured{border-color:#b2f0cc;background:linear-gradient(135deg,#f8fff8,#f0f8ff);}
.fuku-comment-featured::before{content:'';display:block;width:100%;height:3px;background:linear-gradient(90deg,#00c853,#2196f3);border-radius:3px;margin-bottom:14px;}
.fuku-comment-header{display:flex;align-items:center;gap:12px;margin-bottom:12px;}
.fuku-comment-avatar{width:40px;height:40px;border-radius:50%;color:white;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:700;flex-shrink:0;}
.fuku-comment-meta{flex:1;display:flex;flex-wrap:wrap;align-items:center;gap:8px;}
.fuku-comment-name{font-weight:600;font-size:14px;color:#1d1d1f;}
.fuku-featured-badge{background:linear-gradient(135deg,#00c853,#2196f3);color:white;font-size:11px;padding:2px 8px;border-radius:20px;font-weight:600;}
.fuku-comment-time{font-size:12px;color:#86868b;}
.fuku-comment-emoji{font-size:22px;}
.fuku-comment-body{font-size:14px;color:#424245;line-height:1.85;margin-bottom:12px;white-space:pre-wrap;}
.fuku-comment-actions{display:flex;align-items:center;gap:12px;}
.fuku-like-btn{background:none;border:1px solid #e5e5e7;border-radius:20px;padding:4px 12px;font-size:13px;cursor:pointer;color:#86868b;transition:all .2s;display:flex;align-items:center;gap:4px;}
.fuku-like-btn:hover{border-color:#00c853;color:#00c853;background:#f0fff6;}
.fuku-comment-empty{text-align:center;padding:40px;color:#86868b;font-size:14px;background:#fafafa;border-radius:14px;border:2px dashed #e5e5e7;}
.fuku-comments-count{font-size:14px;color:#86868b;margin-bottom:16px;font-weight:500;}
.fuku-toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%);background:rgba(0,0,0,.82);color:white;padding:10px 22px;border-radius:30px;font-size:13px;z-index:9999;opacity:0;transition:opacity .3s;pointer-events:none;}
.fuku-toast.show{opacity:1;}
@media(max-width:600px){.fuku-form-row{flex-direction:column;}.fuku-submit-row{flex-direction:column;align-items:stretch;}.fuku-submit-btn{width:100%;text-align:center;}}
</style>

<div class="fuku-comments-title">💬 留言互动</div>
<p class="fuku-comments-subtitle">欢迎分享你的感受与思考，正向深度的留言将被精选置顶 ✨</p>

<div class="fuku-comment-form">
  <div class="fuku-form-row">
    <input class="fuku-input" id="fuku-name" placeholder="你的昵称（可匿名）" maxlength="20">
  </div>
  <div class="fuku-emoji-row" id="fuku-emoji-row">
    ${['💬','🌿','💡','🙏','❤️','🌟','🌱','😊','🤔','✨'].map((e,i) =>
      `<button class="fuku-emoji-btn${i===0?' active':''}" data-emoji="${e}" title="${e}">${e}</button>`
    ).join('')}
  </div>
  <textarea class="fuku-textarea" id="fuku-content" placeholder="写下你的感受、思考或疑问……分享越真诚、字数越多，越有机会被精选置顶 🌟" maxlength="1000"></textarea>
  <div class="fuku-char-count"><span id="fuku-char-num">0</span> / 1000</div>
  <div class="fuku-submit-row">
    <div class="fuku-submit-hint">
      留言经过积极度评分后自动精选置顶<br>你的真诚感受是对作者最好的鼓励
    </div>
    <button class="fuku-submit-btn" id="fuku-submit">发布留言 →</button>
  </div>
</div>

<div class="fuku-comments-count" id="fuku-count">0 条留言</div>
<div class="fuku-comment-list" id="fuku-comment-list"></div>
<div class="fuku-toast" id="fuku-toast"></div>
`;
    return section;
  }

  function showToast(msg) {
    const t = document.getElementById('fuku-toast');
    if (!t) return;
    t.textContent = msg;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 2200);
  }

  // ─── 初始化 ───────────────────────────────────────────────
  function init() {
    // 找到「关注我们」section 前插入评论区
    const socialSection = document.querySelector('.social-media-section');
    const footer = document.querySelector('footer');
    const insertBefore = socialSection || footer || document.body;

    const section = buildCommentSection();
    insertBefore.parentNode.insertBefore(section, insertBefore);

    const nameInput = document.getElementById('fuku-name');
    const contentInput = document.getElementById('fuku-content');
    const charNum = document.getElementById('fuku-char-num');
    const submitBtn = document.getElementById('fuku-submit');
    const listEl = document.getElementById('fuku-comment-list');
    const countEl = document.getElementById('fuku-count');
    const emojiRow = document.getElementById('fuku-emoji-row');
    let selectedEmoji = '💬';

    // 恢复昵称
    nameInput.value = localStorage.getItem('fuku_nickname') || '';

    // 字数统计
    contentInput.addEventListener('input', () => {
      charNum.textContent = contentInput.value.length;
    });

    // emoji 选择
    emojiRow.addEventListener('click', e => {
      const btn = e.target.closest('.fuku-emoji-btn');
      if (!btn) return;
      emojiRow.querySelectorAll('.fuku-emoji-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      selectedEmoji = btn.dataset.emoji;
    });

    // 渲染
    function refresh() {
      const comments = loadComments();
      countEl.textContent = comments.length + ' 条留言';
      renderList(section, listEl, comments);
    }
    refresh();

    // 提交
    submitBtn.addEventListener('click', () => {
      const name = (nameInput.value.trim() || '匿名').slice(0, 20);
      const content = contentInput.value.trim();
      if (!content) { showToast('请输入留言内容 🌱'); return; }
      if (content.length < 5) { showToast('内容太短啦，多说几句吧～'); return; }

      const id = Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
      const comment = { id, name, content, emoji: selectedEmoji, ts: Date.now(), likes: 0 };
      const list = loadComments();
      list.push(comment);
      saveComments(list);
      localStorage.setItem('fuku_nickname', name);

      contentInput.value = '';
      charNum.textContent = '0';
      refresh();
      showToast(scoreComment(comment) > 5 ? '留言已发布，已被精选置顶 ✨' : '留言已发布，感谢你的分享 🌱');
    });

    // 管理员模式：Ctrl+Shift+A
    let adminMode = false;
    document.addEventListener('keydown', e => {
      if (e.ctrlKey && e.shiftKey && e.key === 'A') {
        adminMode = !adminMode;
        showToast(adminMode ? '管理员模式已开启，点评论可删除' : '管理员模式已关闭');
      }
    });
    listEl.addEventListener('click', e => {
      if (!adminMode) return;
      const item = e.target.closest('.fuku-comment-item');
      if (!item) return;
      if (!confirm('确定删除这条留言？')) return;
      const id = item.dataset.id;
      const list = loadComments().filter(c => c.id !== id);
      saveComments(list);
      refresh();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
