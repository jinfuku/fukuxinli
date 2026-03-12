---
title: 示例文章 - 如何使用Markdown格式
category: 示例
tags: [Markdown, 文章写作, 示例]
date: 2024-03-13
author: 靳福库
summary: 这是一篇示例文章，展示如何使用Markdown格式编写福库心理网站文章
image: images/header.jpg
---

## 引言

本文展示了如何在福库心理网站使用Markdown格式编写文章。Markdown是一种轻量级的标记语言，非常适合AI处理和排版。

<div align="center">
  ![示例图片](images/fig1.jpg)
  <p style="color: #888; font-size: 14px;">图：这是一个示例图片的展示效果</p>
</div>

## Markdown基本语法

### 标题层级

使用井号（#）来标记标题：

```markdown
# 一级标题
## 二级标题
### 三级标题
```

### 文字强调

- **粗体文字**：使用两个星号包围
- *斜体文字*：使用一个星号包围
- `代码文字`：使用反引号包围

### 列表

#### 无序列表

- 第一项
- 第二项
- 第三项

#### 有序列表

1. 第一步
2. 第二步
3. 第三步

## 图片插入技巧

### 基本图片插入

直接使用Markdown语法插入图片：

```markdown
![图片描述](images/图片文件名.jpg)
```

<div align="center">
  ![心理咨询](images/consulting.jpg)
  <p style="color: #888; font-size: 14px;">图：心理咨询场景</p>
</div>

### 带说明的图片

在上面的示例中，我们使用了HTML标签来让图片居中并添加说明文字：

```markdown
<div align="center">
  ![图片描述](images/图片.jpg)
  <p style="color: #888; font-size: 14px;">图片说明文字</p>
</div>
```

## 表格使用

表格可以清晰地展示对比信息：

| 特性 | Markdown | Word | HTML |
|------|---------|------|------|
| AI友好度 | ⭐⭐⭐⭐⭐ | ⭐ | ⭐⭐⭐ |
| 学习难度 | 简单 | 难 | 中等 |
| 图片插入 | 简单 | 简单 | 中等 |
| 代码支持 | 优秀 | 差 | 优秀 |
| 转换HTML | 自动 | 手动 | - |

## 引用和强调

> "心理咨询不仅是一门技术，更是一种艺术。"
> 
> — 欧文·亚隆

重点内容可以使用**粗体**强调，专业术语可以使用`代码格式`标记。

## 视频和音频

### 视频嵌入

<div style="margin: 30px 0; text-align: center;">
  <iframe src="//player.bilibili.com/player.html?bvid=BV1xx411c7mD" 
          width="100%" height="500" frameborder="0" allowfullscreen>
  </iframe>
</div>

### 音频嵌入

<div style="margin: 25px 0; padding: 20px; background: #f9f9fb; border-radius: 14px;">
  <h3 style="margin-bottom: 10px;">冥想引导音频</h3>
  <audio controls style="width: 100%;">
    <source src="audio/meditation.mp3" type="audio/mpeg">
  </audio>
</div>

## 写作建议

### 1. 结构清晰

每个主要话题使用一个二级标题（##），让文章层次分明。

### 2. 适当使用图片

建议每篇文章插入2-5张图片，图片要放在段落之间，不要放在段落中间。

### 3. 列表比长段落好

如果内容较多，尽量使用列表代替长段落，让读者更容易阅读。

### 4. 图片命名规范

```
images/
├── header.jpg          # 文章头图
├── section1-fig1.png   # 第一章节第一张图
├── section1-fig2.png   # 第一章节第二张图
└── section2-fig1.jpg   # 第二章节第一张图
```

## 常见问题

**Q: 图片需要多大？**
A: 建议宽度800-1200px，文件大小控制在500KB以内。

**Q: 如何快速发布？**
A: 写好Markdown文章后，直接对AI说："帮我将这篇文章转换为网页格式"。

**Q: 支持视频吗？**
A: 支持。可以插入本地MP4视频或嵌入B站/腾讯视频。

---

## 总结

Markdown格式最适合AI排版，具有以下优势：

1. **AI友好**：结构清晰，易于理解
2. **语法简单**：容易学习和使用
3. **图片插入方便**：`![描述](路径)`
4. **自动转换**：可以一键转换为HTML
5. **支持丰富**：图片、视频、音频、表格等

**开始使用Markdown，让你的文章发布更高效！**

---

<div align="center">
  ![写作工具](images/writing.jpg)
  <p style="color: #888; font-size: 14px;">图：推荐使用Typora编辑器编写Markdown</p>
</div>
