# -*- coding: utf-8 -*-
import re

with open('index-enhanced.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 移除所有错误位置的 article-actions 按钮块
pattern = r'\n\s*<div class="article-actions">.*?</div>\s*</div>'

def remove_wrong_buttons(match):
    return '\n            </div>'

content = re.sub(pattern, remove_wrong_buttons, content, flags=re.DOTALL)

with open('index-enhanced.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('清理完成！')
