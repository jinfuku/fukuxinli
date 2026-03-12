#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
福库心理 - Markdown文章自动转换工具

功能：
1. 读取Markdown文章文件
2. 解析元数据（YAML front matter）
3. 转换为HTML网页
4. 生成RSS XML
5. 自动处理图片、列表、表格等
"""

import os
import re
import yaml
import markdown
from datetime import datetime
from pathlib import Path


class ArticleConverter:
    """文章转换器类"""
    
    def __init__(self, base_path='.'):
        self.base_path = Path(base_path)
        
    def parse_front_matter(self, content):
        """解析YAML front matter"""
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                front_matter = parts[1].strip()
                article_content = parts[2].strip()
                try:
                    metadata = yaml.safe_load(front_matter)
                    return metadata, article_content
                except yaml.YAMLError:
                    pass
        return {}, content
    
    def markdown_to_html(self, md_content, metadata):
        """将Markdown转换为HTML"""
        
        # 配置Markdown扩展
        md_extensions = [
            'tables',           # 表格
            'fenced_code',      # 代码块
            'nl2br',            # 换行转<br>
            'sane_lists',       # 智能列表
            'attr_list',        # 属性列表
            'def_list',         # 定义列表
            'abbr',             # 缩写
            'footnotes',        # 脚注
        ]
        
        md = markdown.Markdown(extensions=md_extensions)
        html_content = md.convert(md_content)
        
        return html_content
    
    def generate_article_html(self, metadata, html_content, article_path):
        """生成完整文章HTML"""
        
        title = metadata.get('title', '未命名文章')
        category = metadata.get('category', '')
        tags = metadata.get('tags', [])
        date = metadata.get('date', datetime.now().strftime('%Y-%m-%d'))
        author = metadata.get('author', '福库心理')
        summary = metadata.get('summary', '')
        
        tags_html = ' '.join([f'<span class="tag">#{tag}</span>' for tag in tags])
        
        # 检测是否有图片
        has_images = '<img' in html_content or 'video' in html_content.lower()
        
        html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - 福库心理 - 身心神同调</title>
  
  <link rel="stylesheet" href="/css/password-protection.css">
  <style>
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
      background-color: #f5f5f7;
      color: #1d1d1f;
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-rendering: optimizeLegibility;
    }}
    
    /* 优化文章正文样式 */
    .article-content {{
      font-size: 15px;
      line-height: 1.8;
      color: #424245;
      letter-spacing: 0.03em;
    }}

    .article-content h1 {{
      font-size: 2.2em;
      color: #1d1d1f;
      margin-top: 1.5em;
      margin-bottom: 1em;
      font-weight: 700;
      letter-spacing: -0.5px;
    }}

    .article-content h2 {{
      font-size: 1.8em;
      color: #2196f3;
      margin-top: 2em;
      margin-bottom: 1.2em;
      font-weight: 600;
      letter-spacing: -0.3px;
      border-bottom: 2px solid #e5e5e7;
      padding-bottom: 0.5em;
    }}

    .article-content h3 {{
      font-size: 1.5em;
      color: #00c853;
      margin-top: 1.8em;
      margin-bottom: 1em;
      font-weight: 600;
      letter-spacing: -0.2px;
    }}

    .article-content h4 {{
      font-size: 1.3em;
      color: #1d1d1f;
      margin-top: 1.5em;
      margin-bottom: 0.8em;
      font-weight: 600;
    }}

    .article-content p {{
      margin-bottom: 1.5em;
      text-align: justify;
      text-justify: inter-ideograph;
    }}

    .article-content strong {{
      font-weight: 600;
      color: #1d1d1f;
    }}

    .article-content em {{
      font-style: italic;
    }}

    .article-content code {{
      background: #f5f5f7;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: 'SF Mono', Monaco, monospace;
      font-size: 0.9em;
      color: #00c853;
    }}

    .article-content pre {{
      background: #1d1d1f;
      color: #f5f5f7;
      padding: 20px;
      border-radius: 12px;
      overflow-x: auto;
      margin: 20px 0;
    }}

    .article-content pre code {{
      background: none;
      color: inherit;
      padding: 0;
    }}

    .article-content ul, 
    .article-content ol {{
      margin: 1.5em 0;
      padding-left: 2em;
    }}

    .article-content li {{
      margin-bottom: 0.8em;
      line-height: 1.8;
    }}

    .article-content blockquote {{
      border-left: 4px solid #00c853;
      padding-left: 20px;
      margin: 20px 0;
      color: #6e6e73;
      font-style: italic;
      background: #f9f9fb;
      padding: 20px;
      border-radius: 0 12px 12px 0;
    }}

    .article-content hr {{
      border: none;
      height: 2px;
      background: linear-gradient(90deg, #00c853 0%, #2196f3 100%);
      margin: 30px 0;
      border-radius: 2px;
    }}

    .article-content a {{
      color: #00c853;
      text-decoration: none;
      transition: all 0.3s ease;
      font-weight: 500;
    }}

    .article-content a:hover {{
      color: #2196f3;
      text-decoration: underline;
    }}

    .article-content table {{
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
      border-radius: 12px;
      overflow: hidden;
    }}

    .article-content th {{
      background: linear-gradient(135deg, #00c853 0%, #2196f3 100%);
      color: white;
      font-weight: 600;
      padding: 15px;
      text-align: left;
    }}

    .article-content td {{
      padding: 12px 15px;
      border-bottom: 1px solid #e5e5e7;
      background: white;
    }}

    .article-content tr:hover {{
      background: #f9f9fb;
    }}

    /* 图片样式 */
    .article-content img {{
      max-width: 100%;
      height: auto;
      border-radius: 12px;
      margin: 25px 0;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
      transition: all 0.3s ease;
      cursor: pointer;
    }}

    .article-content img:hover {{
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
      transform: scale(1.01);
    }}

    /* 视频样式 */
    .article-content video {{
      width: 100%;
      border-radius: 16px;
      margin: 30px 0;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
    }}

    .article-content iframe {{
      width: 100%;
      border-radius: 16px;
      margin: 30px 0;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
    }}

    /* 居中图片 */
    .article-content div[align="center"] {{
      text-align: center;
      margin: 30px 0;
    }}

    .article-content div[align="center"] p {{
      color: #86868b;
      font-size: 14px;
      margin-top: 10px;
      font-style: italic;
    }}
    
    /* Header */
    header {{
      background: linear-gradient(135deg, #00c853 0%, #2196f3 100%);
      color: white;
      padding: 12px 0 16px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12);
      position: sticky;
      top: 0;
      z-index: 1000;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
    }}

    header .container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 20px;
      text-align: center;
    }}

    header h1 {{
      font-size: 32px;
      margin-bottom: 6px;
      font-weight: 700;
      letter-spacing: -0.3px;
      text-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }}

    nav ul {{
      list-style: none;
      display: flex;
      gap: 15px;
      flex-wrap: wrap;
      justify-content: center;
      margin-top: 12px;
    }}

    nav a {{
      color: white;
      text-decoration: none;
      font-size: 15px;
      font-weight: 500;
      padding: 10px 20px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      transition: all 0.3s ease;
    }}

    nav a:hover {{
      background: rgba(255, 255, 255, 0.25);
      transform: translateY(-2px);
    }}
    
    /* 文章容器 */
    .article-container {{
      max-width: 900px;
      margin: 40px auto;
      padding: 40px 50px;
      background: white;
      border-radius: 20px;
      box-shadow: 0 2px 16px rgba(0, 0, 0, 0.06);
    }}
    
    .article-header {{
      margin-bottom: 40px;
      padding-bottom: 30px;
      border-bottom: 2px solid #e5e5e7;
    }}
    
    .article-meta {{
      display: flex;
      gap: 20px;
      margin: 20px 0;
      flex-wrap: wrap;
    }}
    
    .meta-item {{
      display: flex;
      align-items: center;
      gap: 8px;
      color: #86868b;
      font-size: 14px;
      font-weight: 500;
    }}
    
    .category-badge {{
      display: inline-block;
      padding: 6px 16px;
      background: linear-gradient(135deg, #00c853 0%, #009624 100%);
      color: white;
      border-radius: 20px;
      font-size: 14px;
      font-weight: 600;
    }}
    
    .tag {{
      background: #f5f5f7;
      color: #6e6e73;
      padding: 4px 12px;
      border-radius: 15px;
      font-size: 13px;
      font-weight: 500;
    }}
    
    .summary {{
      background: linear-gradient(135deg, #f0fff4 0%, #e3f2fd 100%);
      padding: 20px 25px;
      border-radius: 12px;
      margin-top: 25px;
      border-left: 4px solid #00c853;
      font-size: 15px;
      line-height: 1.8;
      color: #424245;
    }}
    
    /* 返回按钮 */
    .back-button {{
      display: inline-block;
      padding: 12px 24px;
      background: linear-gradient(135deg, #2196f3 0%, #1976d2 100%);
      color: white;
      text-decoration: none;
      border-radius: 12px;
      font-weight: 600;
      margin: 20px 0;
      transition: all 0.3s ease;
      box-shadow: 0 4px 12px rgba(33, 150, 243, 0.3);
    }}
    
    .back-button:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(33, 150, 243, 0.4);
    }}
    
    /* Footer */
    footer {{
      background: linear-gradient(135deg, #1d1d1f 0%, #2d2d2f 100%);
      color: white;
      padding: 40px 0;
      margin-top: 60px;
      text-align: center;
    }}
    
    footer p {{
      color: #a1a1a6;
      font-size: 14px;
      margin: 5px 0;
    }}
    
    /* 响应式 */
    @media (max-width: 768px) {{
      .article-container {{
        padding: 25px 20px;
        margin: 20px;
      }}
      
      header h1 {{
        font-size: 24px;
      }}
      
      nav a {{
        font-size: 13px;
        padding: 8px 14px;
      }}
      
      .article-content img {{
        border-radius: 8px;
      }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="container">
      <h1>福库身心同调</h1>
      <nav>
        <ul>
          <li><a href="/fukuxinli/">首页</a></li>
          <li><a href="/fukuxinli/body/">身</a></li>
          <li><a href="/fukuxinli/mind/">心</a></li>
          <li><a href="/fukuxinli/spirit/">神</a></li>
          <li><a href="/fukuxinli/partnership/">伴侣关系</a></li>
          <li><a href="/fukuxinli/ai/">AI</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <div class="article-container">
    <div class="article-header">
      <h1>{title}</h1>
      <div class="article-meta">
        <span class="meta-item">
          <span class="category-badge">{category}</span>
        </span>
        <span class="meta-item">📅 {date}</span>
        <span class="meta-item">✍️ {author}</span>
      </div>
      {f'<div class="summary"><strong>摘要：</strong>{summary}</div>' if summary else ''}
    </div>
    
    <div class="article-content">
      {html_content}
    </div>
    
    <div style="margin-top: 50px; padding-top: 30px; border-top: 2px solid #e5e5e7;">
      <p style="color: #86868b; font-size: 14px; margin-bottom: 15px;">标签：{tags_html}</p>
      <a href="/fukuxinli/{category.lower()}/" class="back-button">← 返回{category}分类</a>
    </div>
  </div>

  <footer>
    <p>&copy; 2026 靳福库 - 福库心理 - 身心神同调</p>
    <p>身心神同调，开启生命的新可能</p>
  </footer>

  <script>
    // 图片点击放大
    document.querySelectorAll('.article-content img').forEach(img => {{
      img.addEventListener('click', function() {{
        window.open(this.src, '_blank');
      }});
    }});
  </script>
</body>
</html>'''
        
        return html_template
    
    def generate_rss_xml(self, metadata, html_content, article_path):
        """生成RSS XML"""
        
        title = metadata.get('title', '未命名文章')
        date = metadata.get('date', datetime.now().strftime('%Y-%m-%d'))
        summary = metadata.get('summary', '')
        
        # 提取纯文本摘要
        import re
        text_only = re.sub('<[^<]+?>', '', html_content)
        text_only = text_only[:200] + '...' if len(text_only) > 200 else text_only
        description = summary or text_only
        
        # 获取文章相对路径
        relative_path = str(article_path.relative_to(self.base_path))
        link = f'/fukuxinli/{relative_path}'
        
        xml_template = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>{title}</title>
    <link>{link}</link>
    <description>{description}</description>
    <pubDate>{date}</pubDate>
    <item>
      <title>{title}</title>
      <link>{link}</link>
      <description><![CDATA[{description}]]></description>
      <pubDate>{date}</pubDate>
    </item>
  </channel>
</rss>'''
        
        return xml_template
    
    def convert_article(self, md_file_path):
        """转换单个文章文件"""
        
        md_path = Path(md_file_path)
        
        if not md_path.exists():
            print(f"❌ 文件不存在: {{md_path}}")
            return False
        
        # 读取Markdown文件
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
        except Exception as e:
            print(f"❌ 读取文件失败: {{e}}")
            return False
        
        # 解析元数据
        metadata, article_content = self.parse_front_matter(md_content)
        
        if not metadata.get('title'):
            print(f"⚠️  警告: 文章缺少title元数据")
        
        # 转换Markdown为HTML
        html_content = self.markdown_to_html(article_content, metadata)
        
        # 生成完整HTML
        article_html = self.generate_article_html(metadata, html_content, md_path)
        
        # 生成RSS XML
        rss_xml = self.generate_rss_xml(metadata, html_content, md_path)
        
        # 写入index.html
        html_output_path = md_path.parent / 'index.html'
        try:
            with open(html_output_path, 'w', encoding='utf-8') as f:
                f.write(article_html)
            print(f"✅ 已生成: {{html_output_path}}")
        except Exception as e:
            print(f"❌ 写入HTML失败: {{e}}")
            return False
        
        # 写入index.xml
        xml_output_path = md_path.parent / 'index.xml'
        try:
            with open(xml_output_path, 'w', encoding='utf-8') as f:
                f.write(rss_xml)
            print(f"✅ 已生成: {{xml_output_path}}")
        except Exception as e:
            print(f"❌ 写入XML失败: {{e}}")
            return False
        
        return True
    
    def convert_all_articles(self, start_path='.'):
        """转换所有文章"""
        
        start_path = Path(start_path)
        md_files = list(start_path.rglob('index.md'))
        
        if not md_files:
            print("❌ 未找到任何index.md文件")
            return
        
        print(f"📝 找到 {{len(md_files)}} 篇文章")
        print("=" * 50)
        
        success_count = 0
        for md_file in md_files:
            if self.convert_article(md_file):
                success_count += 1
            print()
        
        print("=" * 50)
        print(f"✅ 转换完成: {{success_count}}/{{len(md_files)}} 篇文章成功")


def main():
    """主函数"""
    
    print("=" * 50)
    print("福库心理 - Markdown文章自动转换工具")
    print("=" * 50)
    print()
    
    # 创建转换器实例
    converter = ArticleConverter()
    
    # 检查命令行参数
    import sys
    if len(sys.argv) > 1:
        # 转换指定文件
        md_file = sys.argv[1]
        converter.convert_article(md_file)
    else:
        # 转换所有文章
        converter.convert_all_articles()


if __name__ == '__main__':
    main()
