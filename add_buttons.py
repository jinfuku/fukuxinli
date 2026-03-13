import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 为每篇文章添加操作按钮
# 查找模式：在评论区结束后的 </div> 之后，文章结束前的 </div> 之前添加按钮

# 文章列表
articles = [
    ('深度心理治疗案例分享', '/fukuxinli/mind/%E6%B7%B1%E5%BA%A6%E5%BF%83%E7%90%86%E6%B2%BB%E7%96%97%E6%A1%88%E4%BE%8B%E5%88%86%E4%BA%AB/'),
    ('艾灸的温暖疗愈', '/fukuxinli/body/%E8%89%BE%E7%81%B8%E7%9A%84%E6%B8%A9%E6%9A%96%E7%96%97%E6%84%88/'),
    ('AI在心理咨询中的辅助作用', '/fukuxinli/ai/ai%E5%9C%A8%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2%E4%B8%AD%E7%9A%84%E8%BE%85%E5%8A%A9%E4%BD%9C%E7%94%A8/'),
    ('伴侣关系中的沟通艺术', '/fukuxinli/partnership/%E4%BC%B4%E4%BE%A3%E5%85%B3%E7%B3%BB%E4%B8%AD%E7%9A%84%E6%B2%9F%E9%80%9A%E8%89%BA%E6%9C%AF/'),
    ('意识与生命整合的探索', '/fukuxinli/spirit/%E6%84%8F%E8%AF%86%E4%B8%8E%E7%94%9F%E5%91%BD%E6%95%B4%E5%90%88%E7%9A%84%E6%8E%A2%E7%B4%A2/'),
    ('存在主义心理治疗的基本概念', '/fukuxinli/mind/%E5%AD%98%E5%9C%A8%E4%B8%BB%E4%B9%89%E5%BF%83%E7%90%86%E6%B2%BB%E7%96%97%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5/'),
    ('推拿疗愈身体的力量', '/fukuxinli/body/%E6%8E%A8%E6%8B%BF%E7%96%97%E6%84%88%E8%BA%AB%E4%BD%93%E7%9A%84%E5%8A%9B%E9%87%8F/'),
]

for title, url in articles:
    # 在评论区的最后一个 </div> 后，文章的 </div> 前添加按钮
    # 查找文章标题，然后找到下一个 </div></div> 模式
    pattern = rf'(</div>\s*</div>\s*</div>)\s*(</div>)\s*\n\s*(<div class="article">|</main>)'
    
    def add_buttons(match):
        closing_divs = match.group(1)
        article_close = match.group(2)
        next_element = match.group(3)
        
        buttons = f'''
            <div class="article-actions">
                <button onclick="shareArticle('{title}', '{url}')">📤 分享</button>
                <a href="{url}" style="text-decoration: none;"><button>📖 阅读全文</button></a>
            </div>
          {article_close}
        
        {next_element}'''
        
        return closing_divs + buttons
    
    content = re.sub(pattern, add_buttons, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("按钮添加完成！")
