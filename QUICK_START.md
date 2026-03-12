# 🚀 快速开始 - 使用Markdown编写文章

## ✅ 推荐格式：Markdown

**为什么选择Markdown？**
- ✅ **AI最容易理解**：结构清晰，语义明确
- ✅ **图片插入超简单**：`![图片描述](images/图片.jpg)`
- ✅ **一键生成网页**：使用Python脚本自动转换
- ✅ **学习成本低**：10分钟即可掌握
- ✅ **支持所有多媒体**：图片、视频、音频、表格

---

## 📝 三步发布文章

### 第一步：编写Markdown文章

在对应分类文件夹下创建新文件夹：

```
fuku-psychology-website/
└── mind/                          # 分类文件夹（心）
    └── 你的新文章标题/
        ├── index.md              # Markdown文章（这里写内容）
        ├── images/               # 图片文件夹
        │   ├── header.jpg        # 文章头图（可选）
        │   ├── fig1.png          # 正文配图1
        │   └── fig2.jpg          # 正文配图2
        └── index.html            # 自动生成（不用管）
```

**index.md 示例：**

```markdown
---
title: 文章标题
category: 心
tags: [心理, 咨询, 案例]
date: 2024-03-13
author: 靳福库
summary: 文章摘要，会在列表页显示
image: images/header.jpg
---

## 引言

这是文章引言...

<div align="center">
  ![图片说明](images/fig1.jpg)
  <p style="color: #888; font-size: 14px;">图：图片说明文字</p>
</div>

## 正文内容

这里是正文内容...

- 列表项1
- 列表项2

> 这是一段引用文字

| 列1 | 列2 |
|-----|-----|
| 内容 | 内容 |

## 结语

总结...
```

---

### 第二步：插入图片

**图片插入语法：**

```markdown
![图片描述](images/图片文件名.jpg)
```

**带说明的居中图片：**

```markdown
<div align="center">
  ![图片描述](images/图片.jpg)
  <p style="color: #888; font-size: 14px;">图片说明文字</p>
</div>
```

**图片命名规范：**
- ✅ `fig1.jpg`, `fig2.png`（英文+数字）
- ❌ `图片1.jpg`（中文不推荐）
- ✅ 宽度800-1200px
- ✅ 文件大小500KB以内

---

### 第三步：转换发布

#### 方式一：自动转换（推荐）

1. 确保已安装Python
2. 安装依赖：
   ```bash
   pip install markdown pyyaml
   ```
3. 运行转换脚本：
   ```bash
   python convert_md_to_html.py
   ```
4. 自动生成 `index.html` 和 `index.xml`

#### 方式二：让AI转换（最简单）

直接对AI说：
```
我写好了一篇Markdown文章，帮我转换成HTML网页格式。
文章路径是：c:\Users\jinfu\WorkBuddy\Claw\fuku-psychology-website\mind\新文章\index.md
```

AI会自动：
- ✅ 读取Markdown文件
- ✅ 生成完整的HTML网页
- ✅ 应用网站样式
- ✅ 插入图片和链接

---

## 🎯 Markdown速查表

| 功能 | 语法 | 示例 |
|------|------|------|
| 一级标题 | `# ` | `# 标题` |
| 二级标题 | `## ` | `## 章节` |
| 三级标题 | `### ` | `### 小节` |
| 粗体 | `**文字**` | `**重点**` |
| 斜体 | `*文字*` | `*强调*` |
| 代码 | `` `代码` `` | `` `关键词` `` |
| 链接 | `[文字](URL)` | `[百度](https://baidu.com)` |
| 图片 | `![描述](路径)` | `![图](images/fig.jpg)` |
| 引用 | `> 文字` | `> 这是一段引用` |
| 分割线 | `---` | 水平线 |
| 无序列表 | `- 项` | - 第一项 |
| 有序列表 | `1. 项` | 1. 第一项 |

---

## 📸 图片插入完整示例

### 示例1：基本图片

```markdown
![心理咨询](images/consulting-room.jpg)
```

### 示例2：带说明的图片

```markdown
<div align="center">
  ![咨询室环境](images/room.jpg)
  <p style="color: #888; font-size: 14px;">图：温馨的咨询室环境</p>
</div>
```

### 示例3：多张图片

```markdown
## 治疗过程

<div align="center">
  ![初次咨询](images/session1.jpg)
  <p style="color: #888; font-size: 14px;">图1：初次咨询</p>
</div>

在初次咨询中...

<div align="center">
  ![深度沟通](images/session2.jpg)
  <p style="color: #888; font-size: 14px;">图2：深度沟通</p>
</div>

在后续咨询中...
```

---

## 🎬 视频/音频插入

### 视频嵌入（B站）

```markdown
<div style="margin: 30px 0; text-align: center;">
  <iframe src="//player.bilibili.com/player.html?bvid=BV1xx411c7mD" 
          width="100%" height="500" frameborder="0" allowfullscreen>
  </iframe>
</div>
```

### 本地视频

```markdown
<video controls width="100%" style="border-radius: 12px; margin: 20px 0;">
  <source src="videos/艾灸演示.mp4" type="video/mp4">
</video>
```

### 音频嵌入

```markdown
<div style="margin: 25px 0; padding: 20px; background: #f9f9fb; border-radius: 14px;">
  <h3 style="margin-bottom: 10px;">冥想引导</h3>
  <audio controls style="width: 100%;">
    <source src="audio/meditation.mp3" type="audio/mpeg">
  </audio>
</div>
```

---

## 💡 写作技巧

### 1. 对AI友好

AI能最好地处理：

- ✅ **清晰的标题层级**：## → ### → ####
- ✅ **明确的元数据**：title, category, tags, date
- ✅ **每张图片都有alt描述**
- ✅ **段落长度适中**（3-5句）
- ✅ **使用列表代替长段落**

### 2. 快速写文章的流程

```
1. 创建文件夹
   ↓
2. 编写Markdown（复制模板）
   ↓
3. 插入图片（images文件夹）
   ↓
4. 对AI说：转换这篇文章
   ↓
5. 自动生成HTML
   ↓
6. 完成！
```

---

## 🔧 工具推荐

### Markdown编辑器

| 工具 | 平台 | 特点 |
|------|------|------|
| **Typora** | Win/Mac/Linux | 所见即所得，推荐⭐⭐⭐⭐⭐ |
| VS Code | Win/Mac/Linux | 免费，插件丰富 |
| Obsidian | Win/Mac/Linux | 知识库工具 |
| 在线编辑器 | Web | 无需安装 |

### 图片压缩工具

- [TinyPNG](https://tinypng.com/) - 免费，效果好
- [Squoosh](https://squoosh.app/) - 谷歌出品

---

## ❓ 常见问题

**Q: 必须使用Markdown吗？**
A: 不是必须，但强烈推荐。AI处理Markdown效率最高。

**Q: 我可以用Word写吗？**
A: 可以，但需要让AI转换。不如直接用Markdown简单。

**Q: 图片必须放在images文件夹吗？**
A: 建议放images文件夹，方便管理。

**Q: 如何快速发布？**
A: 写好Markdown后，直接对AI说："帮我转换这篇文章"即可。

**Q: 支持视频吗？**
A: 支持。可以插入本地视频或嵌入B站/腾讯视频。

---

## 📚 模板文件

所有模板都在这里：
- `ARTICLE_WRITING_GUIDE.md` - 详细编写规范
- `convert_md_to_html.py` - 自动转换脚本
- `示例文章/index.md` - 示例Markdown文章
- `QUICK_START.md` - 本文档（快速开始）

---

## ✨ 总结

**推荐工作流程：**

1. ✅ 使用Markdown格式编写
2. ✅ 图片放在 `images/` 文件夹
3. ✅ 使用 `![描述](路径)` 插入图片
4. ✅ 对AI说："转换这篇文章"
5. ✅ 自动生成HTML网页

**就这么简单！**

---

**需要帮助？**
- 查看完整规范：`ARTICLE_WRITING_GUIDE.md`
- 查看示例文章：`示例文章/index.md`
- 运行转换脚本：`python convert_md_to_html.py`

**开始创作吧！** 🎉
