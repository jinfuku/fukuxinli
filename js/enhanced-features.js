// 福库心理网站增强功能
// 包含：标签系统、文章聚合、分享功能、相关推荐

// ============ 文章数据库 ============
const articleDatabase = {
    "推拿起疗愈身体的力量": {
        category: "身",
        tags: ["推拿", "中医", "疗愈", "身体"],
        series: "中医理疗系列",
        price: 9.9,
        url: "/body/推拿疗愈身体的力量/"
    },
    "艾灸的温暖疗愈": {
        category: "身",
        tags: ["艾灸", "中医", "疗愈", "身体"],
        series: "中医理疗系列",
        price: 9.9,
        url: "/body/艾灸的温暖疗愈/"
    },
    "存在主义心理治疗的基本概念": {
        category: "心",
        tags: ["存在主义", "心理咨询", "欧文·亚隆"],
        series: "心理咨询系列",
        price: 9.9,
        url: "/mind/存在主义心理治疗的基本概念/"
    },
    "深度心理治疗案例分享": {
        category: "心",
        tags: ["深度心理治疗", "案例", "心理咨询", "系统排列"],
        series: "心理咨询系列",
        price: 99, // 系列合集
        url: "/mind/深度心理治疗案例分享/"
    },
    "意识与生命整合的探索": {
        category: "神",
        tags: ["意识", "生命整合", "威尔菲德·内勒斯", "心灵"],
        series: "内勒斯理论系列",
        price: 9.9,
        url: "/spirit/意识与生命整合的探索/"
    },
    "威尔菲德内勒斯核心概念术语翻译对照表": {
        category: "神",
        tags: ["威尔菲德·内勒斯", "概念术语", "翻译", "系统排列"],
        series: "内勒斯理论系列",
        price: 99, // 系列合集
        url: "/spirit/威尔菲德内勒斯核心概念术语翻译对照表/"
    },
    "伴侣关系中的沟通艺术": {
        category: "伴侣关系",
        tags: ["伴侣关系", "沟通", "心理学", "关系"],
        series: "关系系列",
        price: 9.9,
        url: "/partnership/伴侣关系中的沟通艺术/"
    },
    "AI在心理咨询中的辅助作用": {
        category: "AI",
        tags: ["AI", "人工智能", "心理咨询", "科技"],
        series: "科技与心理系列",
        price: 9.9,
        url: "/ai/ai在心理咨询中的辅助作用/"
    }
};

// ============ 标签聚合系统 ============

// 渲染文章标签
function renderTags(tags) {
    if (!tags || tags.length === 0) return '';
    
    const tagsHtml = tags.map(tag => 
        `<span class="tag" onclick="showArticlesByTag('${tag}')">#${tag}</span>`
    ).join('');
    
    return `<div class="tags-container"><span class="tags-label">话题标签：</span>${tagsHtml}</div>`;
}

// 显示指定标签的所有文章
function showArticlesByTag(tag) {
    const modal = document.createElement('div');
    modal.className = 'tag-modal';
    modal.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0,0,0,0.8);
        z-index: 2000;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
    `;
    
    const articles = getArticlesByTag(tag);
    const articlesHtml = articles.length > 0 
        ? articles.map(article => `
            <div class="tag-article-item" onclick="window.location.href='${article.url}'">
                <h4 class="tag-article-title">${article.title}</h4>
                <div class="tag-article-meta">
                    <span class="tag-article-category">${article.category}</span>
                    <span class="tag-article-price">￥${article.price}</span>
                </div>
            </div>
        `).join('')
        : '<p class="no-articles">暂无相关文章</p>';
    
    modal.innerHTML = `
        <div class="tag-modal-content">
            <div class="tag-modal-header">
                <h3>标签：#${tag}</h3>
                <button class="close-btn" onclick="this.closest('.tag-modal').remove()">×</button>
            </div>
            <div class="tag-modal-body">
                ${articlesHtml}
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
}

// 根据标签获取文章
function getArticlesByTag(tag) {
    const results = [];
    for (const [title, article] of Object.entries(articleDatabase)) {
        if (article.tags && article.tags.includes(tag)) {
            results.push({
                title: title,
                category: article.category,
                price: article.price,
                url: article.url
            });
        }
    }
    return results;
}

// ============ 相关文章推荐系统 ============

// 渲染相关文章推荐
function renderRelatedArticles(currentTitle) {
    const currentArticle = articleDatabase[currentTitle];
    if (!currentArticle) return '';
    
    let relatedArticles = [];
    
    // 1. 同系列文章
    if (currentArticle.series) {
        for (const [title, article] of Object.entries(articleDatabase)) {
            if (title !== currentTitle && article.series === currentArticle.series) {
                relatedArticles.push({
                    title: title,
                    category: article.category,
                    reason: '同系列',
                    url: article.url
                });
            }
        }
    }
    
    // 2. 同标签文章
    if (currentArticle.tags) {
        for (const [title, article] of Object.entries(articleDatabase)) {
            if (title !== currentTitle && article.tags) {
                const commonTags = currentArticle.tags.filter(t => article.tags.includes(t));
                if (commonTags.length > 0 && !relatedArticles.find(r => r.title === title)) {
                    relatedArticles.push({
                        title: title,
                        category: article.category,
                        reason: '同标签',
                        url: article.url
                    });
                }
            }
        }
    }
    
    // 3. 同分类文章
    for (const [title, article] of Object.entries(articleDatabase)) {
        if (title !== currentTitle && article.category === currentArticle.category) {
            if (!relatedArticles.find(r => r.title === title)) {
                relatedArticles.push({
                    title: title,
                    category: article.category,
                    reason: '同分类',
                    url: article.url
                });
            }
        }
    }
    
    // 限制推荐数量
    relatedArticles = relatedArticles.slice(0, 5);
    
    if (relatedArticles.length === 0) return '';
    
    const articlesHtml = relatedArticles.map(article => `
        <div class="related-article-item" onclick="window.location.href='${article.url}'">
            <div class="related-article-title">${article.title}</div>
            <div class="related-article-meta">
                <span class="related-article-category">${article.category}</span>
                <span class="related-article-reason">${article.reason}</span>
            </div>
        </div>
    `).join('');
    
    return `
        <div class="related-articles">
            <h3>📚 相关文章推荐</h3>
            <div class="related-articles-list">
                ${articlesHtml}
            </div>
        </div>
    `;
}

// ============ 分享功能 ============

// 渲染分享按钮
function renderShareButton() {
    const shareBtn = document.createElement('button');
    shareBtn.className = 'share-button';
    shareBtn.innerHTML = '📤 分享';
    shareBtn.onclick = showShareMenu;
    return shareBtn;
}

// 显示分享菜单
function showShareMenu() {
    const url = window.location.href;
    const title = document.querySelector('h1')?.textContent || '福库心理 - 身心神同调';
    const description = document.querySelector('meta[name="description"]')?.content || '';
    
    const modal = document.createElement('div');
    modal.className = 'share-modal';
    modal.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0,0,0,0.8);
        z-index: 2000;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
    `;
    
    modal.innerHTML = `
        <div class="share-modal-content">
            <div class="share-modal-header">
                <h3>分享文章</h3>
                <button class="close-btn" onclick="this.closest('.share-modal').remove()">×</button>
            </div>
            <div class="share-modal-body">
                <div class="share-platforms">
                    <button class="share-platform" onclick="copyShareLink()">
                        <span class="platform-icon">🔗</span>
                        <span class="platform-name">复制链接</span>
                    </button>
                    <button class="share-platform" onclick="shareToWeChat()">
                        <span class="platform-icon">💬</span>
                        <span class="platform-name">微信好友</span>
                    </button>
                    <button class="share-platform" onclick="shareToMoments()">
                        <span class="platform-icon">⭕</span>
                        <span class="platform-name">朋友圈</span>
                    </button>
                </div>
                <div class="share-url">
                    <label>文章链接：</label>
                    <input type="text" id="share-url" value="${url}" readonly>
                    <button onclick="copyShareLink()">复制</button>
                </div>
                <div class="share-qr" id="share-qr" style="display: none;">
                    <p>微信扫描二维码分享</p>
                </div>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
}

// 复制分享链接
function copyShareLink() {
    const urlInput = document.getElementById('share-url');
    if (urlInput) {
        urlInput.select();
        navigator.clipboard.writeText(urlInput.value).then(() => {
            showToast('链接已复制到剪贴板！');
        }).catch(() => {
            // 回退方案
            document.execCommand('copy');
            showToast('链接已复制到剪贴板！');
        });
    }
}

// 分享到微信好友
function shareToWeChat() {
    // 微信网页版分享需要使用微信JS-SDK
    // 这里提供一个提示，实际功能需要后端支持
    showToast('请使用微信扫一扫功能分享文章');
    
    // 显示二维码（使用二维码API生成）
    const qrContainer = document.querySelector('#share-qr');
    if (qrContainer) {
        const url = encodeURIComponent(window.location.href);
        qrContainer.style.display = 'block';
        qrContainer.innerHTML = `
            <p>微信扫描二维码分享</p>
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${url}" 
                 alt="分享二维码" 
                 style="max-width: 200px; margin: 10px auto; display: block;">
        `;
    }
}

// 分享到朋友圈
function shareToMoments() {
    showToast('请使用微信扫一扫功能，然后分享到朋友圈');
    shareToWeChat();
}

// 显示提示信息
function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    toast.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(0,0,0,0.8);
        color: white;
        padding: 15px 25px;
        border-radius: 8px;
        z-index: 3000;
        animation: fadeIn 0.3s ease;
    `;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'fadeOut 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 2000);
}

// ============ 初始化功能 ============

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    // 添加CSS样式
    const style = document.createElement('style');
    style.textContent = `
        /* 标签样式 */
        .tags-container {
            margin: 20px 0;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
            border-left: 3px solid #00c853;
        }
        
        .tags-label {
            font-weight: 600;
            color: #333;
            margin-right: 10px;
        }
        
        .tag {
            display: inline-block;
            padding: 5px 12px;
            margin: 3px;
            background: linear-gradient(135deg, #00c853, #2196f3);
            color: white;
            border-radius: 15px;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .tag:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        /* 分享按钮样式 */
        .share-button {
            position: fixed;
            top: 80px;
            right: 20px;
            padding: 12px 20px;
            background: linear-gradient(135deg, #00c853, #2196f3);
            color: white;
            border: none;
            border-radius: 25px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            z-index: 1000;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transition: all 0.3s;
        }
        
        .share-button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 16px rgba(0,0,0,0.2);
        }
        
        /* 模态框样式 */
        .tag-modal, .share-modal {
            animation: fadeIn 0.3s ease;
        }
        
        .tag-modal-content, .share-modal-content {
            background: white;
            border-radius: 12px;
            max-width: 500px;
            width: 100%;
            max-height: 80vh;
            overflow-y: auto;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }
        
        .tag-modal-header, .share-modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
            border-bottom: 1px solid #e0e0e0;
        }
        
        .tag-modal-header h3, .share-modal-header h3 {
            margin: 0;
            color: #333;
        }
        
        .close-btn {
            background: none;
            border: none;
            font-size: 24px;
            cursor: pointer;
            color: #666;
            padding: 0;
            width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .close-btn:hover {
            color: #333;
        }
        
        .tag-modal-body {
            padding: 20px;
        }
        
        .tag-article-item {
            padding: 15px;
            margin-bottom: 10px;
            background: #f8f9fa;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .tag-article-item:hover {
            background: #e8f5e9;
            transform: translateX(5px);
        }
        
        .tag-article-title {
            margin: 0 0 8px 0;
            color: #333;
            font-size: 16px;
        }
        
        .tag-article-meta {
            display: flex;
            gap: 10px;
        }
        
        .tag-article-category {
            color: #00c853;
            font-size: 12px;
            padding: 2px 8px;
            background: #e8f5e9;
            border-radius: 10px;
        }
        
        .tag-article-price {
            color: #ff5722;
            font-size: 12px;
            font-weight: 600;
        }
        
        .no-articles {
            text-align: center;
            color: #999;
            padding: 40px;
        }
        
        /* 分享平台按钮 */
        .share-platforms {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .share-platform {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
            background: #f8f9fa;
            border: 2px solid transparent;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .share-platform:hover {
            background: white;
            border-color: #00c853;
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        .platform-icon {
            font-size: 32px;
            margin-bottom: 8px;
        }
        
        .platform-name {
            font-size: 13px;
            color: #333;
        }
        
        .share-url {
            margin-bottom: 20px;
        }
        
        .share-url label {
            display: block;
            margin-bottom: 8px;
            color: #666;
            font-size: 14px;
        }
        
        .share-url input {
            width: calc(100% - 70px);
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 13px;
        }
        
        .share-url button {
            padding: 10px 15px;
            margin-left: 5px;
            background: #00c853;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 13px;
        }
        
        .share-url button:hover {
            background: #00a846;
        }
        
        .share-qr {
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
        }
        
        .share-qr p {
            margin-bottom: 10px;
            color: #666;
            font-size: 14px;
        }
        
        /* 相关文章样式 */
        .related-articles {
            margin: 30px 0;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        .related-articles h3 {
            color: #00c853;
            margin-bottom: 20px;
            font-size: 20px;
        }
        
        .related-articles-list {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        
        .related-article-item {
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
            border-left: 3px solid transparent;
        }
        
        .related-article-item:hover {
            background: white;
            border-left-color: #00c853;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transform: translateX(5px);
        }
        
        .related-article-title {
            color: #333;
            font-size: 15px;
            margin-bottom: 8px;
            line-height: 1.5;
        }
        
        .related-article-meta {
            display: flex;
            gap: 10px;
        }
        
        .related-article-category {
            color: #00c853;
            font-size: 12px;
            padding: 2px 8px;
            background: #e8f5e9;
            border-radius: 10px;
        }
        
        .related-article-reason {
            color: #2196f3;
            font-size: 12px;
            padding: 2px 8px;
            background: #e3f2fd;
            border-radius: 10px;
        }
        
        /* 动画 */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes fadeOut {
            from { opacity: 1; }
            to { opacity: 0; }
        }
        
        /* 响应式 */
        @media (max-width: 768px) {
            .share-button {
                top: 70px;
                right: 15px;
                padding: 10px 16px;
                font-size: 13px;
            }
            
            .share-platforms {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .share-url input {
                width: calc(100% - 60px);
                font-size: 12px;
            }
        }
    `;
    document.head.appendChild(style);
    
    // 在文章详情页添加标签和分享功能
    const articleTitle = document.querySelector('h1');
    if (articleTitle) {
        const titleText = articleTitle.textContent.trim();
        
        // 添加分享按钮
        document.body.appendChild(renderShareButton());
        
        // 添加标签（在文章标题下方）
        const articleData = articleDatabase[titleText];
        if (articleData && articleData.tags) {
            const tagsHtml = renderTags(articleData.tags);
            const tagsContainer = document.createElement('div');
            tagsContainer.innerHTML = tagsHtml;
            articleTitle.parentNode.insertBefore(tagsContainer, articleTitle.nextSibling);
        }
        
        // 添加相关文章（在文章末尾）
        const relatedArticlesHtml = renderRelatedArticles(titleText);
        if (relatedArticlesHtml) {
            const relatedContainer = document.createElement('div');
            relatedContainer.innerHTML = relatedArticlesHtml;
            
            // 找到文章内容的末尾
            const articleContent = document.querySelector('main, .main-content, .article-content');
            if (articleContent) {
                articleContent.appendChild(relatedContainer);
            }
        }
    }
    
    // 在右侧边栏添加相关推荐（如果存在）
    const sidebarRight = document.querySelector('.sidebar-right, aside:last-of-type');
    if (sidebarRight) {
        const titleText = document.querySelector('h1')?.textContent.trim();
        const relatedArticlesHtml = renderRelatedArticles(titleText);
        if (relatedArticlesHtml) {
            const relatedSection = document.createElement('div');
            relatedSection.innerHTML = relatedArticlesHtml;
            relatedSection.style.marginTop = '30px';
            sidebarRight.appendChild(relatedSection);
        }
    }
});

// 导出到全局
window.showArticlesByTag = showArticlesByTag;
window.showShareMenu = showShareMenu;
window.copyShareLink = copyShareLink;
window.shareToWeChat = shareToWeChat;
window.shareToMoments = shareToMoments;
