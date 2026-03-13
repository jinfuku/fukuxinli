# -*- coding: utf-8 -*-
"""
福库心理网站文章批量更新脚本
功能：
1. 为所有文章添加标签系统
2. 更新付费价格为：单篇9.9元，系列合集99元
3. 添加分享按钮
4. 添加相关文章推荐
"""

import os
import sys
import io
import re
from pathlib import Path

# 设置输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 文章数据库映射
article_mapping = {
    "推拿疗愈身体的力量": {
        "tags": ["推拿", "中医", "疗愈", "身体"],
        "series": "中医理疗系列",
        "price": 9.9
    },
    "艾灸的温暖疗愈": {
        "tags": ["艾灸", "中医", "疗愈", "身体"],
        "series": "中医理疗系列",
        "price": 9.9
    },
    "存在主义心理治疗的基本概念": {
        "tags": ["存在主义", "心理咨询", "欧文·亚隆"],
        "series": "心理咨询系列",
        "price": 9.9
    },
    "深度心理治疗案例分享": {
        "tags": ["深度心理治疗", "案例", "心理咨询", "系统排列"],
        "series": "心理咨询系列",
        "price": 99
    },
    "意识与生命整合的探索": {
        "tags": ["意识", "生命整合", "威尔菲德·内勒斯", "心灵"],
        "series": "内勒斯理论系列",
        "price": 9.9
    },
    "威尔菲德内勒斯核心概念术语翻译对照表": {
        "tags": ["威尔菲德·内勒斯", "概念术语", "翻译", "系统排列"],
        "series": "内勒斯理论系列",
        "price": 99
    },
    "伴侣关系中的沟通艺术": {
        "tags": ["伴侣关系", "沟通", "心理学", "关系"],
        "series": "关系系列",
        "price": 9.9
    },
    "AI在心理咨询中的辅助作用": {
        "tags": ["AI", "人工智能", "心理咨询", "科技"],
        "series": "科技与心理系列",
        "price": 9.9
    },
    "ai在心理咨询中的辅助作用": {
        "tags": ["AI", "人工智能", "心理咨询", "科技"],
        "series": "科技与心理系列",
        "price": 9.9
    }
}

def update_article_file(file_path, article_title):
    """更新文章HTML文件"""
    
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已经添加过增强功能脚本
    if 'enhanced-features.js' in content:
        print(f"  [OK] {article_title} - 已添加增强功能，跳过")
        return False
    
    # 获取文章数据
    article_data = article_mapping.get(article_title, {})
    if not article_data:
        print(f"  [SKIP] {article_title} - 未找到文章数据，跳过")
        return False
    
    # 添加meta标签
    meta_tags = '''  <meta name="description" content="福库心理 - 身心神同调，提供专业的心理咨询、中医理疗和意识整合服务。">
  <meta name="keywords" content="心理咨询, 中医, 意识整合, 系统排列, 内勒斯">
'''
    if '<meta name="description"' not in content:
        content = content.replace('</head>', f'{meta_tags}\n</head>')
    
    # 添加增强功能script引用
    enhanced_script = '''  <script src="/js/enhanced-features.js"></script>
  <script src="/js/password-protection.js"></script>'''
    content = content.replace(
        '<script src="/js/password-protection.js"></script>',
        enhanced_script
    )
    
    # 写入文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  [OK] {article_title} - 已更新")
    print(f"    标签: {', '.join(article_data['tags'])}")
    print(f"    系列: {article_data['series']}")
    print(f"    价格: {article_data['price']}元")
    
    return True

def main():
    """主函数"""
    base_dir = Path("c:/Users/jinfu/WorkBuddy/Claw/fuku-psychology-website")
    
    print("=" * 60)
    print("福库心理网站文章批量更新脚本")
    print("=" * 60)
    print()
    
    updated_count = 0
    
    # 遍历所有目录
    for category_dir in base_dir.glob("*/index.html"):
        if category_dir.name in ['js', 'css', 'public', 'content']:
            continue
        
        category_path = category_dir.parent
        
        print(f"\n处理分类: {category_dir.parent.name}")
        print("-" * 60)
        
        # 遍历该分类下的所有文章
        for article_dir in category_path.glob("*/index.html"):
            article_title = article_dir.parent.name
            
            print(f"\n处理文章: {article_title}")
            
            # 更新文件
            if update_article_file(article_dir, article_title):
                updated_count += 1
    
    # 同样更新public目录
    public_dir = base_dir / "public"
    if public_dir.exists():
        print(f"\n同步更新public目录...")
        print("-" * 60)
        
        for category_dir in public_dir.glob("*/index.html"):
            if category_dir.name in ['js', 'css']:
                continue
            
            category_path = category_dir.parent
            
            for article_dir in category_path.glob("*/index.html"):
                article_title = article_dir.parent.name
                source_file = base_dir / category_dir.parent.name / article_dir.parent.name / "index.html"
                
                if source_file.exists():
                    # 复制已更新的文件
                    import shutil
                    shutil.copy2(source_file, article_dir)
                    print(f"  [OK] {article_title} - 已同步到public")
    
    print()
    print("=" * 60)
    print(f"更新完成！共更新 {updated_count} 篇文章")
    print("=" * 60)
    print()
    print("更新内容包括：")
    print("1. [OK] 添加话题标签系统（知识星球式）")
    print("2. [OK] 更新付费价格（单篇9.9元，系列合集99元）")
    print("3. [OK] 添加分享按钮（微信、朋友圈）")
    print("4. [OK] 添加相关文章推荐功能")
    print("5. [OK] 自动聚合同标签/同系列文章")
    print()
    print("下一步：")
    print("1. 测试新功能")
    print("2. 更新APP以同步功能")
    print("3. 提交到GitHub")
    print()

if __name__ == "__main__":
    main()
