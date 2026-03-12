# 福库心理 - 文章编写规范

## 📝 格式选择：Markdown

**为什么选择Markdown？**
- ✅ AI最容易理解和处理的格式
- ✅ 图片插入语法简单：`![描述](路径)`
- ✅ 结构清晰，易于维护
- ✅ 一键转换为HTML网页
- ✅ 支持所有常见的排版需求

---

## 🎯 文章基本结构

每个文章文件夹包含：
```
文章标题/
├── index.md          # 文章正文（Markdown格式）
├── images/           # 图片文件夹
│   ├── header.jpg    # 文章头图（可选）
│   ├── fig1.png      # 正文配图
│   └── fig2.jpg
└── metadata.md       # 文章元数据（可选）
```

---

## 📄 Markdown语法指南

### 1. 文章头部元数据（必须）

在每个Markdown文章开头添加：

```markdown
---
title: 深度心理治疗案例分享
category: 心
tags: [心理治疗, 案例, 身心神同调]
date: 2024-03-12
author: 靳福库
summary: 通过真实案例展示心理咨询如何在帮助个体实现身心神同调的过程中发挥重要作用
image: images/header.jpg
---
```

### 2. 标题层级

```markdown
# 文章标题（通常不用，使用元数据title）
## 一级标题
### 二级标题
#### 三级标题
##### 四级标题
```

### 3. 段落和换行

```markdown
这是第一段文字。

空行表示新段落。

这是第二段文字。
```

### 4. 图片插入（重点）

#### 基本语法
```markdown
![图片描述](images/图片文件名.jpg)
```

#### 带尺寸的图片
```markdown
![图片描述](images/图片.jpg =600x400)
```

#### 居中显示
```markdown
<div align="center">
  ![图片描述](images/图片.jpg)
  <p style="color: #888; font-size: 14px;">图片说明文字</p>
</div>
```

#### 示例
```markdown
## 治疗过程

<div align="center">
  ![咨询室环境](images/consulting-room.jpg)
  <p style="color: #888; font-size: 14px;">图：温馨的咨询室环境</p>
</div>

在最初的几次咨询中...
```

### 5. 列表

#### 无序列表
```markdown
- 第一项
- 第二项
- 第三项
```

#### 有序列表
```markdown
1. 第一步
2. 第二步
3. 第三步
```

#### 嵌套列表
```markdown
- 主要观点
  - 子观点1
  - 子观点2
- 另一个观点
```

### 6. 强调文字

```markdown
**粗体文字**
*斜体文字*
***粗斜体文字***
`代码文字`
```

### 7. 引用

```markdown
> 这是一段引用的文字
> 可以是多行
```

### 8. 分割线

```markdown
---
```

### 9. 表格

```markdown
| 阶段 | 咨询次数 | 主要目标 |
|------|---------|---------|
| 建立信任 | 1-4次 | 建立安全关系 |
| 探索根源 | 5-10次 | 发现深层次问题 |
| 认知重构 | 11-20次 | 挑战非理性信念 |
```

### 10. 链接

```markdown
[链接文字](https://www.example.com)
```

### 11. 视频嵌入（HTML标签）

```markdown
<video controls width="100%" style="border-radius: 12px; margin: 20px 0;">
  <source src="videos/艾灸演示.mp4" type="video/mp4">
</video>

<!-- 或嵌入B站视频 -->
<div style="margin: 30px 0; text-align: center;">
  <iframe src="//player.bilibili.com/player.html?bvid=BV1xx411c7mD" 
          width="100%" height="500" frameborder="0" allowfullscreen>
  </iframe>
</div>
```

### 12. 音频嵌入

```markdown
<div style="margin: 25px 0; padding: 20px; background: #f9f9fb; border-radius: 14px;">
  <h3 style="margin-bottom: 10px;">音频标题</h3>
  <audio controls style="width: 100%;">
    <source src="audio/meditation.mp3" type="audio/mpeg">
  </audio>
</div>
```

---

## 🎨 排版建议

### 1. 段落长度
- 每段3-5句为宜
- 避免超过10句的长段落
- 适当使用图片分割文字

### 2. 标题使用
- 每个主要话题使用一个二级标题（##）
- 次要话题使用三级标题（###）
- 避免连续多个段落没有标题

### 3. 图片使用
- 每篇文章建议2-5张图片
- 图片宽度建议800-1200px
- 图片格式：JPG/PNG（建议PNG用于图表，JPG用于照片）

### 4. 列表使用
- 列表项建议3-7项
- 超过7项考虑分组或使用表格
- 使用列表让内容更易读

### 5. 重点突出
- 重要概念使用**粗体**
- 引用内容使用引用块
- 专业术语使用`代码格式`

---

## 📚 完整文章示例

```markdown
---
title: 艾灸的温暖疗愈
category: 身
tags: [艾灸, 中医, 身体调理]
date: 2024-01-20
author: 靳福库
summary: 艾灸作为中国传统医学的重要组成部分，通过艾草燃烧产生的热力和药力，达到温通经络、调和气血、扶正祛邪的作用
image: images/header.jpg
---

## 引言

艾灸，作为中国传统医学的重要组成部分，通过艾草燃烧产生的热力和药力，作用于人体的经络和穴位，达到温通经络、调和气血、扶正祛邪的作用。

<div align="center">
  ![艾灸工具](images/moxa-tools.jpg)
  <p style="color: #888; font-size: 14px;">图：传统艾灸工具</p>
</div>

## 艾灸的核心原理

### 温通经络

艾灸的温热作用能够：

- 疏通经络，促进气血运行
- 温经散寒，缓解疼痛
- 改善局部血液循环

### 常用穴位

| 穴位名称 | 位置 | 主要功效 |
|---------|------|---------|
| 足三里 | 外膝眼下三寸 | 调理脾胃，增强体质 |
| 关元 | 肚脐下三寸 | 培补元气，温肾壮阳 |
| 气海 | 肚脐下1.5寸 | 培元固本，益气固精 |

## 艾灸的操作方法

### 直接灸

<div align="center">
  ![直接灸示意图](images/direct-moxibustion.jpg)
  <p style="color: #888; font-size: 14px;">图：直接灸操作演示</p>
</div>

直接将艾柱放在穴位上燃烧：

- 疗效直接，刺激强
- 注意控制温度和距离
- 避免烫伤

> **温馨提示**：首次艾灸建议在专业人士指导下进行，确保安全。

---

## 🚀 快速发布流程

### 方式一：使用自动转换工具（推荐）

1. 在对应分类文件夹（mind/body/spirit等）下创建新文件夹
2. 创建 `index.md` 文件，按Markdown格式编写文章
3. 在文件夹内创建 `images` 文件夹，放入图片
4. 运行转换脚本：`python convert_md_to_html.py`
5. 自动生成 `index.html` 和 `index.xml`

### 方式二：使用在线工具

1. 访问 [Markdown编辑器](https://markdowneditor.app/)
2. 粘贴Markdown内容
3. 导出为HTML
4. 手动复制到 `index.html`

### 方式三：让AI直接生成

直接对AI说：
```
帮我将以下文章转换为HTML格式，并插入图片链接：
[粘贴你的Markdown文章]
```

---

## 💡 写作技巧

### 1. 从AI角度思考

AI处理文章时，特别关注：
- **结构清晰**：明确的标题层级
- **语义明确**：使用正确的Markdown语法
- **图片标注**：每个图片都有描述文字
- **元数据完整**：title, category, tags, summary等

### 2. 提升AI效率

这样做AI能更好地排版：
- ✅ 使用正确的标题层级
- ✅ 图片放在段落之间，不要在段落中间
- ✅ 长段落适当分割
- ✅ 使用列表代替长段文字
- ✅ 添加明确的图片说明

### 3. 避免的做法

- ❌ 使用HTML标签（特殊需求除外）
- ❌ 过深的标题嵌套（最多到####）
- ❌ 连续多个段落没有标题
- ❌ 图片文件名包含中文或空格

---

## 📸 图片规范

### 图片命名
```
images/
├── header.jpg          # 文章头图（推荐尺寸：1200x630）
├── section1-fig1.png   # 第一章节第一张图
├── section1-fig2.png   # 第一章节第二张图
├── section2-fig1.jpg   # 第二章节第一张图
└── gallery/            # 图库文件夹
    ├── photo1.jpg
    └── photo2.jpg
```

### 图片格式建议

| 用途 | 推荐格式 | 推荐尺寸 | 压缩率 |
|------|---------|---------|--------|
| 照片 | JPG | 800-1200px宽 | 70-80% |
| 图表/示意图 | PNG | 800-1200px宽 | 保留透明度 |
| 文章头图 | JPG | 1200x630 | 80% |
| 缩略图 | JPG | 300x200 | 60-70% |

### 图片优化

1. **压缩图片**：使用 [TinyPNG](https://tinypng.com/) 或 [Squoosh](https://squoosh.app/)
2. **响应式图片**：使用 `width="100%"` 样式
3. **Alt文本**：为每张图片添加描述，利于SEO和Accessibility

---

## 🔗 参考资源

- [Markdown官方语法](https://www.markdownguide.org/)
- [Typora编辑器](https://typora.io/) - 优秀的Markdown编辑器
- [VS Code Markdown插件](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [在线Markdown编辑器](https://markdowneditor.app/)

---

## ❓ 常见问题

**Q: 我可以用Word写文章吗？**
A: 不推荐。Word格式AI很难理解。建议使用Markdown格式，或者让AI将Word内容转换为Markdown。

**Q: 图片需要多大？**
A: 建议宽度800-1200px，文件大小控制在500KB以内。使用TinyPNG等工具压缩。

**Q: 支持视频吗？**
A: 支持。可以插入本地MP4视频或嵌入B站/腾讯视频。

**Q: 如何快速发布？**
A: 写好Markdown文章后，直接对AI说："帮我将这篇文章转换为网页格式"，AI会自动生成HTML代码。

**Q: 可以插入音频吗？**
A: 可以。使用HTML的audio标签即可插入MP3音频。

---

## ✅ 检查清单

发布文章前检查：

- [ ] 文章开头有元数据（title, category, tags, date, summary）
- [ ] 使用正确的标题层级（##, ###, ####）
- [ ] 所有图片都有alt描述
- [ ] 图片已优化（压缩、正确尺寸）
- [ ] 段落长度适中（3-5句）
- [ ] 长内容使用列表或表格
- [ ] 无连续多个段落没有标题
- [ ] 链接和图片路径正确
- [ ] 在浏览器中预览效果
- [ ] 移动端显示正常

---

**最后更新：2024年3月**
**维护者：福库心理团队**
