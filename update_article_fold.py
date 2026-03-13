# -*- coding: utf-8 -*-
"""
为文章添加折叠功能和操作按钮
"""

import re

def update_file():
    with open('index-enhanced.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到所有文章的模式
    # 每篇文章结构：<div class="article"> ... <div class="summary">...</div> ... </div>
    
    # 在每个 </div> 前面，如果是文章的结束，添加操作按钮
    # 我们需要找到每篇文章的标题和链接
    
    lines = content.split('\n')
    new_lines = []
    in_article = False
    article_start_idx = -1
    article_title = ''
    article_url = ''
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 检测文章开始
        if '<div class="article">' in line:
            in_article = True
            article_start_idx = i
        
        # 提取文章标题和链接
        if in_article and '<h3><a href="' in line:
            match = re.search(r'<h3><a href="([^"]+)">([^<]+)</a></h3>', line)
            if match:
                article_url = match.group(1)
                article_title = match.group(2)
        
        # 检测文章结束 - 找到summary结束后的第一个</div>
        if in_article and '</div>' in line and article_title:
            # 检查下一行是否是新的文章或者文章列表结束
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                # 如果下一行是新的文章或文章列表结束
                if '<div class="article">' in next_line or '</div>' in next_line:
                    # 在当前</div>前添加操作按钮
                    indent = '            '
                    buttons = f'''
{indent}<div class="article-actions">
{indent}    <button onclick="shareArticle('{article_title}', '{article_url}')">📤 分享</button>
{indent}    <a href="{article_url}" style="text-decoration: none;"><button>📖 阅读全文</button></a>
{indent}</div>'''
                    new_lines.append(buttons)
                    
                    # 重置状态
                    in_article = False
                    article_title = ''
                    article_url = ''
        
        new_lines.append(line)
        i += 1
    
    # 写回文件
    with open('index-enhanced.html', 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    print("更新完成！")

if __name__ == '__main__':
    update_file()
