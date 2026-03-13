# -*- coding: utf-8 -*-
"""
为文章添加折叠功能和操作按钮
按钮放在评论区之后，文章结束之前
"""

import re

with open('index-enhanced.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到每篇文章的标题和链接
article_pattern = r'<div class="article">\s*<h3><a href="([^"]+)">([^<]+)</a></h3>'

articles = re.findall(article_pattern, content)
print(f"找到 {len(articles)} 篇文章")

# 对于每篇文章，在评论区结束后、</div>(article结束)前添加按钮
# 第一篇文章（深度心理治疗案例分享）有评论区，其他文章可能没有

# 方案：在每个 </div>\s*</div> 模式前添加按钮
# 这个模式表示 summary 或 comments-section 的结束，然后是 article 的结束

# 更精确的方案：
# 在每个 </div>\s*</div>\s*<div class="article"> 前，在第一个</div>后添加按钮
# 或者在 </div>\s*</div>\s*</main> 前添加按钮

# 处理每篇文章
for i, (url, title) in enumerate(articles):
    # 为每篇文章添加操作按钮
    # 按钮应该放在文章的最后，即 </div> (article结束) 之前
    
    # 创建按钮HTML
    buttons_html = f'''
            <div class="article-actions">
                <button onclick="shareArticle('{title}', '{url}')">📤 分享</button>
                <a href="{url}" style="text-decoration: none;"><button>📖 阅读全文</button></a>
            </div>'''
    
    # 找到这篇文章的结束位置
    # 方法：找到下一个文章开始的位置，然后向前找到</div>
    
    if i < len(articles) - 1:
        next_url = articles[i+1][0]
        # 在下一个文章开始前添加按钮
        next_article_start = f'<div class="article">\n            <h3><a href="{next_url}">'
        
        # 找到这个位置
        pos = content.find(next_article_start)
        if pos > 0:
            # 向前找到 </div>\s*</div> 模式
            before = content[:pos]
            # 找到最后一个 </div>
            last_div_end = before.rfind('</div>')
            if last_div_end > 0:
                # 在这个 </div> 前面插入按钮
                # 但我们需要找到是哪个 </div>
                # 检查前一个字符
                insert_pos = last_div_end
                # 找到正确的缩进
                line_start = before.rfind('\n', 0, insert_pos) + 1
                indent = before[line_start:insert_pos]
                
                # 插入按钮
                content = content[:insert_pos] + buttons_html + '\n          ' + content[insert_pos:]
                print(f"已为 '{title}' 添加按钮")
    else:
        # 最后一篇文章，在 </main> 前添加
        main_end = content.find('</main>')
        if main_end > 0:
            # 找到这之前的 </div>
            before = content[:main_end]
            last_div_end = before.rfind('</div>')
            if last_div_end > 0:
                content = content[:last_div_end] + buttons_html + '\n          ' + content[last_div_end:]
                print(f"已为 '{title}' 添加按钮")

# 保存文件
with open('index-enhanced.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n所有文章按钮已添加完成！")
