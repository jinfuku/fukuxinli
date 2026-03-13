# -*- coding: utf-8 -*-
"""
更新主页文章列表，添加标签和价格显示
"""

import sys
import io
from pathlib import Path

# 设置输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 文章数据
article_data = {
    "深度心理治疗案例分享": {
        "tags": ["#深度心理治疗", "#案例", "#心理咨询", "#系统排列"],
        "price": "99元",
        "badge": "系列合集"
    },
    "艾灸的温暖疗愈": {
        "tags": ["#艾灸", "#中医", "#疗愈", "#身体"],
        "price": "9.9元",
        "badge": ""
    },
    "ai在心理咨询中的辅助作用": {
        "tags": ["#AI", "#人工智能", "#心理咨询", "#科技"],
        "price": "9.9元",
        "badge": ""
    },
    "意识与生命整合的探索": {
        "tags": ["#意识", "#生命整合", "#威尔菲德·内勒斯", "#心灵"],
        "price": "9.9元",
        "badge": ""
    },
    "存在主义心理治疗的基本概念": {
        "tags": ["#存在主义", "#心理咨询", "#欧文·亚隆"],
        "price": "9.9元",
        "badge": ""
    },
    "伴侣关系中的沟通艺术": {
        "tags": ["#伴侣关系", "#沟通", "#心理学", "#关系"],
        "price": "9.9元",
        "badge": ""
    },
    "推拿疗愈身体的力量": {
        "tags": ["#推拿", "#中医", "#疗愈", "#身体"],
        "price": "9.9元",
        "badge": ""
    }
}

def update_index_file():
    """更新主页文件"""
    index_file = Path("c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website/index.html")
    
    # 读取文件
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 为每篇文章添加标签和价格
    for title, data in article_data.items():
        # 查找文章标题链接
        old_pattern = f'<h3><a href="/fukuxinli/'
        new_pattern = f'''    <div class="article-tags">
      {data["tags"].join(" ")}
    </div>
    <div class="article-price">
      <span class="price-tag">🔒 {data["price"]}</span>
      {f'<span class="series-badge">📦 {data["badge"]}</span>' if data["badge"] else ''}
    </div>
  </div>'''
        
        # 简化处理：只查找并替换文章元数据部分
        # 查找<div class="meta">部分
        meta_pattern = f'<div class="meta">\n              \n                <span>'
        
        if meta_pattern in content:
            # 查找具体的文章
            article_start = content.find(title)
            if article_start > 0:
                # 找到这篇文章的meta部分
                meta_start = content.find('<div class="meta">', article_start)
                meta_end = content.find('</div>', meta_start)
                
                if meta_start > 0 and meta_end > 0:
                    old_meta = content[meta_start:meta_end + 6]
                    
                    # 添加标签和价格信息
                    tags_html = f'''
    <div class="article-tags">
      {"".join([f'<span class="tag">{tag}</span>' for tag in data["tags"]])}
    </div>'''
                    
                    price_html = f'''
    <div class="article-price">
      <span class="price-tag">🔒 {data["price"]}</span>
      {f'<span class="series-badge">📦 {data["badge"]}</span>' if data["badge"] else ''}
    </div>'''
                    
                    new_meta = old_meta + tags_html + price_html
                    
                    content = content.replace(old_meta, new_meta)
    
    # 添加增强功能的CSS样式
    css_to_add = '''
    .article-tags {
      margin-top: 10px;
      padding: 8px;
      background: #f8f9fa;
      border-radius: 6px;
      border-left: 3px solid #00c853;
    }
    
    .article-tags .tag {
      display: inline-block;
      padding: 3px 10px;
      margin: 2px;
      background: linear-gradient(135deg, #00c853, #2196f3);
      color: white;
      border-radius: 12px;
      font-size: 12px;
      cursor: pointer;
      transition: all 0.3s;
    }
    
    .article-tags .tag:hover {
      transform: translateY(-2px);
      box-shadow: 0 3px 6px rgba(0,0,0,0.15);
    }
    
    .article-price {
      margin-top: 8px;
      display: flex;
      gap: 8px;
      align-items: center;
    }
    
    .price-tag {
      display: inline-block;
      padding: 4px 12px;
      background: linear-gradient(135deg, #ff5722, #ff9800);
      color: white;
      border-radius: 12px;
      font-size: 13px;
      font-weight: 600;
    }
    
    .series-badge {
      display: inline-block;
      padding: 4px 12px;
      background: linear-gradient(135deg, #9c27b0, #673ab7);
      color: white;
      border-radius: 12px;
      font-size: 13px;
      font-weight: 600;
    }
'''
    
    # 在</style>前添加CSS
    content = content.replace('</style>', f'{css_to_add}\n  </style>')
    
    # 写入文件
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("主页更新完成！")
    print("添加内容：")
    print("1. 每篇文章显示话题标签")
    print("2. 显示文章价格")
    print("3. 系列合集显示特殊徽章")
    print("4. 改进的样式设计")

if __name__ == "__main__":
    update_index_file()
