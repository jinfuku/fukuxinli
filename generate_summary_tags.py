# -*- coding: utf-8 -*-
"""
文章自动摘要和标签生成工具
自动为网站文章生成200字以内内容简介和4个话题标签
"""

import os
import re
import sys
import io
from pathlib import Path

# 设置输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from bs4 import BeautifulSoup
import jieba
import jieba.analyse

# 网站根目录
WEBSITE_ROOT = Path(__file__).parent

# 文章分类目录
CATEGORIES = ['mind', 'body', 'spirit', 'partnership', 'ai']

# 标签关键词映射 - 帮助生成更准确的标签
TAG_KEYWORDS = {
    # 心理咨询相关
    '心理咨询': ['#心理咨询', '#心理健康'],
    '心理治疗': ['#心理治疗', '#心理咨询'],
    '案例': ['#案例分享', '#心理实务'],
    '焦虑': ['#焦虑', '#心理健康'],
    '抑郁': ['#抑郁', '#心理健康'],
    '存在主义': ['#存在主义', '#欧文亚隆'],
    '亚隆': ['#欧文亚隆', '#存在主义'],
    
    # 身体疗愈相关
    '艾灸': ['#艾灸', '#中医养生'],
    '推拿': ['#推拿按摩', '#身体疗愈'],
    '按摩': ['#推拿按摩', '#身体疗愈'],
    '经络': ['#经络养生', '#中医'],
    '中医': ['#中医养生', '#传统文化'],
    
    # 意识与精神相关
    '意识': ['#意识探索', '#心灵成长'],
    '生命整合': ['#生命整合', '#内勒斯'],
    '内勒斯': ['#威尔菲德内勒斯', '#生命整合'],
    '海灵格': ['#海灵格', '#系统排列'],
    '系统排列': ['#系统排列', '#家庭系统'],
    
    # 伴侣关系相关
    '伴侣': ['#伴侣关系', '#亲密关系'],
    '婚姻': ['#婚姻家庭', '#伴侣关系'],
    '沟通': ['#沟通艺术', '#人际关系'],
    '亲密': ['#亲密关系', '#伴侣'],
    
    # AI相关
    'AI': ['#AI人工智能', '#科技心理'],
    '人工智能': ['#人工智能', '#AI'],
}

def extract_text_from_html(html_content):
    """从HTML中提取纯文本内容"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 获取主要内容区域
    article_content = soup.find('main', class_='article-content')
    if not article_content:
        article_content = soup.find('div', class_='article-content')
    if not article_content:
        article_content = soup.find('article')
    
    if article_content:
        # 移除脚本和样式
        for script in article_content(['script', 'style', 'nav', 'header', 'footer']):
            script.decompose()
        
        # 获取标题
        title = ''
        h1 = article_content.find('h1')
        if h1:
            title = h1.get_text(strip=True)
            h1.decompose()  # 移除标题，避免重复
        
        # 获取文本
        text = article_content.get_text(separator=' ', strip=True)
        return title, text
    
    return '', ''

def generate_summary(text, max_length=200):
    """
    生成文章摘要
    优先使用文章开头的引言部分，提取关键句子
    """
    # 清理文本
    text = re.sub(r'\s+', ' ', text)
    
    # 尝试找到引言或第一段重要内容
    intro_patterns = [
        r'引言[：:]?\s*(.*?)(?=\n\n|##|一、|二、|1\.|第一节|$)',
        r'摘要[：:]?\s*(.*?)(?=\n\n|##|$)',
        r'^(.*?)(?=\n\n|##|$)',
    ]
    
    intro_text = ''
    for pattern in intro_patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            intro_text = match.group(1).strip()
            break
    
    if not intro_text:
        intro_text = text[:500]  # 取前500字符
    
    # 分句
    sentences = re.split(r'[。！？\.\!\?]', intro_text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # 组合句子到接近max_length
    summary = ''
    for sentence in sentences:
        if len(summary) + len(sentence) + 1 <= max_length:
            summary += sentence + '。'
        else:
            break
    
    # 如果摘要太短，添加更多内容
    if len(summary) < 50 and len(text) > 50:
        remaining = text[len(summary):max_length+100]
        remaining_sentences = re.split(r'[。！？\.\!\?]', remaining)
        for sentence in remaining_sentences[:2]:
            if sentence.strip() and len(summary) + len(sentence) < max_length:
                summary += sentence.strip() + '。'
    
    return summary.strip()

def generate_tags(text, title='', count=4):
    """
    生成文章标签
    结合关键词映射和TF-IDF算法
    """
    tags = set()
    
    # 1. 从标题和关键词映射中提取标签
    full_text = title + ' ' + text
    
    for keyword, related_tags in TAG_KEYWORDS.items():
        if keyword in full_text:
            for tag in related_tags:
                tags.add(tag)
    
    # 2. 使用jieba的TF-IDF提取关键词
    keywords = jieba.analyse.extract_tags(full_text, topK=10, withWeight=False)
    
    # 关键词到标签的映射
    keyword_tag_map = {
        '心理': '#心理学',
        '治疗': '#心理治疗',
        '疗愈': '#身心疗愈',
        '健康': '#心理健康',
        '关系': '#人际关系',
        '家庭': '#家庭关系',
        '情绪': '#情绪管理',
        '成长': '#个人成长',
        '中医': '#中医养生',
        '养生': '#养生保健',
        '身体': '#身体健康',
        '心灵': '#心灵成长',
        '精神': '#精神健康',
        '意识': '#意识探索',
        '生命': '#生命意义',
        '存在': '#存在主义',
        '沟通': '#沟通技巧',
        '伴侣': '#伴侣关系',
        '婚姻': '#婚姻关系',
        '艾灸': '#艾灸养生',
        '推拿': '#推拿按摩',
    }
    
    for keyword in keywords:
        if keyword in keyword_tag_map:
            tags.add(keyword_tag_map[keyword])
        elif len(keyword) >= 2:
            # 对于其他关键词，创建通用标签
            if keyword not in ['我们', '可以', '能够', '这是', '通过', '进行', '一个', '这种', '这些']:
                tags.add('#' + keyword)
    
    # 返回前count个标签
    tag_list = list(tags)[:count]
    
    # 如果标签不足4个，添加默认标签
    default_tags = ['#心理学', '#身心健康', '#生命成长', '#福库心理']
    while len(tag_list) < count:
        for dt in default_tags:
            if dt not in tag_list:
                tag_list.append(dt)
                if len(tag_list) >= count:
                    break
    
    return tag_list[:count]

def update_article_html(html_path, summary, tags):
    """更新文章HTML，添加摘要和标签"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # 查找文章标题位置
    h1 = soup.find('h1')
    if not h1:
        return False
    
    # 查找article-meta
    article_meta = soup.find('div', class_='article-meta')
    
    # 创建摘要和标签区域
    summary_div = soup.new_tag('div', attrs={'class': 'article-summary-auto'})
    summary_div['style'] = '''
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-left: 4px solid #00c853;
        border-radius: 12px;
        padding: 20px;
        margin: 20px 0;
        font-size: 15px;
        line-height: 1.8;
        color: #424245;
    '''
    
    # 摘要标题
    summary_title = soup.new_tag('div')
    summary_title['style'] = 'font-weight: 600; color: #00c853; margin-bottom: 10px; font-size: 14px;'
    summary_title.string = '📝 内容简介'
    summary_div.append(summary_title)
    
    # 摘要内容
    summary_content = soup.new_tag('div')
    summary_content.string = summary
    summary_div.append(summary_content)
    
    # 标签区域
    tags_div = soup.new_tag('div', attrs={'class': 'article-tags-auto'})
    tags_div['style'] = '''
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px dashed #dee2e6;
    '''
    
    for tag in tags:
        tag_span = soup.new_tag('span', attrs={'class': 'auto-tag'})
        tag_span['style'] = '''
            background: linear-gradient(135deg, #00c853 0%, #2196f3 100%);
            color: white;
            padding: 5px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s;
        '''
        tag_span.string = tag
        tags_div.append(tag_span)
    
    summary_div.append(tags_div)
    
    # 插入到合适位置（在article-meta之后）
    if article_meta:
        article_meta.insert_after(summary_div)
    else:
        h1.insert_after(summary_div)
    
    # 写入文件
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
    
    return True

def process_all_articles():
    """处理所有文章"""
    print("=" * 50)
    print("文章摘要和标签自动生成工具")
    print("=" * 50)
    
    processed_count = 0
    
    for category in CATEGORIES:
        category_path = WEBSITE_ROOT / category
        if not category_path.exists():
            continue
        
        print(f"\n📁 处理分类: {category}")
        
        # 遍历该分类下的所有文章目录
        for article_dir in category_path.iterdir():
            if not article_dir.is_dir():
                continue
            
            index_file = article_dir / 'index.html'
            if not index_file.exists():
                continue
            
            # 检查是否已经处理过
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'article-summary-auto' in content:
                    print(f"  ⏭️  {article_dir.name} - 已有摘要，跳过")
                    continue
            
            print(f"  📄 处理: {article_dir.name}")
            
            # 提取文本
            title, text = extract_text_from_html(content)
            
            if not text:
                print(f"    ⚠️  无法提取文本内容")
                continue
            
            # 生成摘要和标签
            summary = generate_summary(text)
            tags = generate_tags(text, title)
            
            print(f"    📝 摘要: {summary[:50]}...")
            print(f"    🏷️  标签: {', '.join(tags)}")
            
            # 更新HTML
            if update_article_html(index_file, summary, tags):
                processed_count += 1
                print(f"    ✅ 更新成功")
            else:
                print(f"    ❌ 更新失败")
    
    print(f"\n{'=' * 50}")
    print(f"处理完成！共更新 {processed_count} 篇文章")
    print("=" * 50)
    
    return processed_count

def process_single_article(article_path):
    """处理单篇文章"""
    article_path = Path(article_path)
    
    if not article_path.exists():
        print(f"❌ 文件不存在: {article_path}")
        return False
    
    with open(article_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取文本
    title, text = extract_text_from_html(content)
    
    if not text:
        print("❌ 无法提取文本内容")
        return False
    
    # 生成摘要和标签
    summary = generate_summary(text)
    tags = generate_tags(text, title)
    
    print(f"\n📄 文章: {title}")
    print(f"📝 摘要: {summary}")
    print(f"🏷️  标签: {', '.join(tags)}")
    
    # 更新HTML
    if update_article_html(article_path, summary, tags):
        print("✅ 更新成功")
        return True
    else:
        print("❌ 更新失败")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 处理指定文章
        article_path = sys.argv[1]
        process_single_article(article_path)
    else:
        # 处理所有文章
        process_all_articles()
