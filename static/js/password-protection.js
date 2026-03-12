/**
 * 福库心理 - 付费文章密码保护功能（支持试读模式）
 *
 * 使用说明：
 * 1. 在文章的 Front Matter 中添加：password: "您的密码"
 * 2. 在文章内容中添加 <!-- MORE --> 标记来分割试读部分和付费内容
 * 3. 未付费用户可以看到试读部分，输入密码后才能阅读完整内容
 */

// 已解锁的文章列表（存储在 localStorage 中）
const UNLOCKED_ARTICLES_KEY = 'fuku_unlocked_articles';

// 获取已解锁的文章列表
function getUnlockedArticles() {
    const unlocked = localStorage.getItem(UNLOCKED_ARTICLES_KEY);
    return unlocked ? JSON.parse(unlocked) : {};
}

// 保存已解锁的文章列表
function saveUnlockedArticles(unlocked) {
    localStorage.setItem(UNLOCKED_ARTICLES_KEY, JSON.stringify(unlocked));
}

// 检查文章是否已解锁
function isArticleUnlocked(articleId) {
    const unlocked = getUnlockedArticles();
    return unlocked[articleId] === true;
}

// 解锁文章
function unlockArticle(articleId) {
    const unlocked = getUnlockedArticles();
    unlocked[articleId] = true;
    saveUnlockedArticles(unlocked);
}

// 显示密码输入对话框
function showPasswordDialog(articleId, articleTitle) {
    // 创建对话框
    const dialog = document.createElement('div');
    dialog.id = 'password-dialog';
    dialog.innerHTML = `
        <div class="password-dialog-overlay">
            <div class="password-dialog-content">
                <div class="password-dialog-header">
                    <h3>🔒 付费文章</h3>
                    <button class="close-btn" onclick="closePasswordDialog()">×</button>
                </div>
                <div class="password-dialog-body">
                    <p class="article-title">${articleTitle}</p>
                    <p class="hint">这是一篇付费文章，请输入访问密码：</p>
                    <input type="password" id="password-input" class="password-input" placeholder="请输入密码" onkeypress="handlePasswordKeypress(event, '${articleId}')">
                    <div class="error-message" id="error-message" style="display: none;"></div>
                    <button class="confirm-btn" onclick="verifyPassword('${articleId}')">确认</button>
                    <button class="cancel-btn" onclick="closePasswordDialog()">取消</button>
                </div>
            </div>
        </div>
    `;

    // 添加到页面
    document.body.appendChild(dialog);

    // 聚焦密码输入框
    setTimeout(() => {
        document.getElementById('password-input').focus();
    }, 100);
}

// 关闭密码对话框
function closePasswordDialog() {
    const dialog = document.getElementById('password-dialog');
    if (dialog) {
        dialog.remove();
    }
}

// 处理密码输入框的回车键
function handlePasswordKeypress(event, articleId) {
    if (event.key === 'Enter') {
        verifyPassword(articleId);
    }
}

// 验证密码
function verifyPassword(articleId) {
    const password = document.getElementById('password-input').value;
    const errorMessage = document.getElementById('error-message');

    // 获取文章的正确密码（从页面上的隐藏元素中获取）
    const correctPassword = document.getElementById('correct-password-' + articleId)?.value;

    if (!correctPassword) {
        errorMessage.textContent = '错误：无法获取文章密码信息';
        errorMessage.style.display = 'block';
        return;
    }

    // 验证密码
    if (password === correctPassword) {
        // 密码正确，解锁文章
        unlockArticle(articleId);
        closePasswordDialog();

        // 显示成功提示
        showSuccessMessage('密码验证成功！文章已解锁');

        // 重新加载页面以显示文章内容
        setTimeout(() => {
            location.reload();
        }, 1000);
    } else {
        // 密码错误
        errorMessage.textContent = '密码错误，请重新输入';
        errorMessage.style.display = 'block';
        document.getElementById('password-input').value = '';
        document.getElementById('password-input').focus();
    }
}

// 显示成功提示
function showSuccessMessage(message) {
    const toast = document.createElement('div');
    toast.className = 'success-toast';
    toast.textContent = message;
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, 3000);
}

// 检查文章是否需要密码保护并显示内容
function checkPasswordProtection() {
    // 检查文章是否有密码保护
    const passwordElement = document.getElementById('correct-password');

    if (!passwordElement) {
        // 没有密码保护，正常显示
        return;
    }

    // 生成文章 ID（使用页面 URL 生成）
    const articleId = generateArticleId();
    const isUnlocked = isArticleUnlocked(articleId);

    if (isUnlocked) {
        // 已解锁，正常显示文章内容
        return;
    }

    // 未解锁，隐藏文章内容，显示密码输入提示
    hideProtectedContent(articleId);
}

// 生成文章 ID
function generateArticleId() {
    // 使用页面 URL 生成唯一 ID
    const url = window.location.pathname;
    return btoa(url).replace(/[^a-zA-Z0-9]/g, '');
}

// 隐藏受保护的内容（支持试读模式）
function hideProtectedContent(articleId) {
    // 查找文章正文内容
    const articleBody = document.querySelector('.article-body');
    const articleTitle = document.querySelector('.article-content h1')?.textContent || '付费文章';

    if (articleBody) {
        const content = articleBody.innerHTML;
        const moreMarker = '<!-- MORE -->';

        if (content.includes(moreMarker)) {
            // 支持"微信式试读"：显示前半部分，隐藏后半部分
            const [previewPart, paidPart] = content.split(moreMarker);

            // 替换文章内容为预览部分
            articleBody.innerHTML = previewPart;

            // 创建付费内容分割线
            const divider = document.createElement('div');
            divider.className = 'paid-content-divider';
            divider.innerHTML = `
                <div class="locked-content">
                    <div class="lock-icon">🔒</div>
                    <h2>付费内容</h2>
                    <p>以上是文章的免费试读部分。</p>
                    <p>如需阅读完整内容，请输入访问密码解锁。</p>
                    <button class="unlock-btn" onclick="showPasswordDialog('${articleId}', '${articleTitle}')">输入密码解锁</button>
                    <p class="hint">提示：如果您已经购买了访问权限，请联系福库老师获取密码。</p>
                </div>
            `;

            // 在预览部分后面添加付费提示
            articleBody.appendChild(divider);
        } else {
            // 如果没有 <!-- MORE --> 标记，则完全隐藏内容（兼容旧模式）
            articleBody.style.display = 'none';

            const passwordPrompt = document.createElement('div');
            passwordPrompt.className = 'password-prompt';
            passwordPrompt.innerHTML = `
                <div class="locked-content">
                    <div class="lock-icon">🔒</div>
                    <h2>付费文章</h2>
                    <p>这篇文章是付费内容，需要输入访问密码才能阅读。</p>
                    <button class="unlock-btn" onclick="showPasswordDialog('${articleId}', '${articleTitle}')">输入密码解锁</button>
                    <p class="hint">提示：如果您已经购买了访问权限，请联系福库老师获取密码。</p>
                </div>
            `;

            // 在文章正文前插入密码提示
            articleBody.parentNode.insertBefore(passwordPrompt, articleBody);
        }
    }
}

// 解锁文章内容（完整显示）
function showFullContent(articleId) {
    const articleBody = document.querySelector('.article-body');
    if (!articleBody) return;

    // 恢复完整内容（需要从页面加载时保存的原始内容中获取）
    const originalContent = articleBody.getAttribute('data-original-content');
    if (originalContent) {
        // 移除 <!-- MORE --> 标记，显示完整内容
        const fullContent = originalContent.replace(/<!-- MORE -->/g, '');
        articleBody.innerHTML = fullContent;
    }
}

// 页面加载时检查密码保护
document.addEventListener('DOMContentLoaded', function() {
    // 保存原始内容（用于解锁后恢复）
    const articleBody = document.querySelector('.article-body');
    if (articleBody) {
        articleBody.setAttribute('data-original-content', articleBody.innerHTML);
    }

    checkPasswordProtection();
});
