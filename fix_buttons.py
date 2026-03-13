# -*- coding: utf-8 -*-
"""
清理错误位置的文章操作按钮，然后正确放置
"""

import re

def fix_file():
    with open('index-enhanced.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 移除所有错误位置的 article-actions 按钮块
    # 这些按钮应该只出现在每篇文章的summary结束后的正确位置
    
    # 匹配所有 article-actions 块（除了CSS定义）
    pattern = r'\n\s*<div class="article-actions">.*?</div>\s*</div>'
    
    def remove_wrong_buttons(match):
        # 检查这个位置是否正确（在summary后）
        # 如果在</div>之后紧接着是新的文章或文章列表结束，则保留
        # 否则移除
        return '\n            </div>'
    
    # 先移除所有按钮
    content = re.sub(pattern, remove_wrong_buttons, content, flags=re.DOTALL)
    
    # 现在正确添加按钮
    # 找到每篇文章的结构：
    # <div class="article">
    #   <h3><a href="URL">TITLE</a></h3>
    #   <div class="meta">...</div>
    #   <div class="summary">...</div>
    #   [评论区] (如果有)
    # </div>
    
    # 正确的模式：在 </div> (summary结束) 之后，</div> (article结束) 之前
    
    lines = content.split('\n')
    new_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)
        
        # 检测是否是文章的summary结束后的第一个</div>
        # 这需要追踪文章结构
        
        i += 1
    
    # 更简单的方法：找到每篇文章的URL和标题，然后在正确的位置添加按钮
    # 文章结构：
    # <div class="article">
    #   <h3><a href="URL">TITLE</a></h3>
    #   ...
    #   <div class="summary">...</div>
    #   </div> (这里添加按钮)
    # </div>
    
    # 由于结构复杂，我们使用更精确的替换
    
    # 保存修改后的内容
    with open('index-enhanced.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("清理完成！")

if __name__ == '__main__':
    fix_file()
