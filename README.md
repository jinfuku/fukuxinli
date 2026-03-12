# 福库心理网站 - 身心神同调

## 网站简介

福库心理网站是一个专注于"身、心、神"同调的内容平台，分享关于推拿、艾灸、心理咨询、意识、生命整合、伴侣关系、AI应用等方面的内容。

## 技术栈

- **静态网站生成器**：Hugo
- **发布平台**：GitHub Pages
- **语言**：中文
- **架构**：纯静态网站（方案A）

## 网站功能

### 已实现
- ✅ 三栏布局（左侧导航、中间内容、右侧推荐）
- ✅ 5个分类：身、心、神、伴侣关系、AI
- ✅ 博客文章发布
- ✅ 图片展示
- ✅ 视频嵌入支持（B站、腾讯视频等）
- ✅ 语音播放支持
- ✅ 搜索功能（基础版）
- ✅ 响应式设计（手机、电脑）

### 待实现
- ⏳ 评论系统（Giscus）
- ⏳ 高级搜索（Lunr.js）
- ⏳ 相册功能

## 文章分类

- **身（推拿、艾灸）**：身体层面的疗愈方法
- **心（心理咨询）**：心理层面的成长和支持
- **神（意识、生命整合）**：意识层面的探索和整合
- **伴侣关系**：亲密关系的沟通和成长
- **AI（人工智能）**：人工智能在心理咨询中的应用

## 本地开发

### 安装 Hugo

如果您还没有安装 Hugo，请访问 [Hugo 官网](https://gohugo.io/) 下载安装。

### 启动本地服务器

```bash
# 进入项目目录
cd fuku-psychology-website

# 启动本地服务器
hugo server -D

# 在浏览器中打开
# http://localhost:1313
```

### 添加新文章

创建新的 Markdown 文件：

```bash
# 示例：在"身"分类下添加文章
hugo new body/新文章标题.md
```

文章格式（Front Matter）：

```yaml
---
title: "文章标题"
date: 2024-01-20
category: "分类名称"
---
```

### 插入视频

**B站视频：**

```html
<div class="video-container">
  <iframe src="//player.bilibili.com/player.html?bvid=BV1xx411c7mD" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>
```

**腾讯视频：**

```html
<div class="video-container">
  <iframe src="https://v.qq.com/txp/iframe/player.html?vid=YOUR_VIDEO_ID" allowFullScreen="true"></iframe>
</div>
```

### 插入音频

```html
<div class="audio-player">
  <audio controls>
    <source src="/audio/your-audio-file.mp3" type="audio/mpeg">
    您的浏览器不支持音频播放。
  </audio>
</div>
```

## 项目结构

```
fuku-psychology-website/
├── config.yaml              # 网站配置文件
├── content/                 # 内容目录
│   ├── body/                # 身（推拿、艾灸）
│   ├── mind/                # 心（心理咨询）
│   ├── spirit/              # 神（意识、生命整合）
│   ├── partnership/         # 伴侣关系
│   └── ai/                  # AI（人工智能）
├── layouts/                 # 模板目录
│   ├── index.html           # 首页模板
│   └── _default/
│       ├── single.html      # 文章详情页
│       └── list.html        # 分类列表页
├── static/                  # 静态资源
│   ├── images/              # 图片
│   └── audio/               # 语音
└── archetypes/              # 文章模板
```

## 发布到 GitHub Pages

### 快速发布（推荐）

1. 双击运行 `publish.bat` 脚本
2. 按照提示操作
3. 等待自动部署完成

### 手动发布

#### 第一步：创建 GitHub 仓库

1. 在 GitHub 上创建一个新仓库，命名为 `fuku-psychology-website`
2. 选择 Public（公开）
3. 初始化本地仓库并推送到 GitHub：

```bash
git init
git add .
git commit -m "初始提交"
git branch -M main
git remote add origin https://github.com/your-username/fuku-psychology-website.git
git push -u origin main
```

（注意：将 `your-username` 替换为您的 GitHub 用户名）

#### 第二步：配置 GitHub Pages

1. 进入仓库的 **Settings** → **Pages**
2. 在 **Source** 下选择 **Deploy from a branch**
3. 选择 **main** 分支，文件夹选择 `/ (root)`
4. 点击 **Save**

等待几分钟后，您的网站就可以通过以下地址访问：
`https://your-username.github.io/fuku-psychology-website`

### 详细发布指南

请参考：[发布网站到GitHubPages指南.md](../发布网站到GitHubPages指南.md)

## 本地预览

### 快速预览（推荐）

1. 双击运行 `preview.bat` 脚本
2. 在浏览器中打开：http://localhost:8000
3. 按 Ctrl+C 停止服务器

### 手动预览

```bash
# 使用 Python 启动服务器
cd fuku-psychology-website
python -m http.server 8000

# 在浏览器中打开
# http://localhost:8000
```

## 颜色方案

- **主色调**：绿色系 (#00c853) - 参考WorkBuddy网站风格，有朝气
- **辅助色**：蓝色系 (#2196f3) - 保持专业感
- **背景色**：浅灰色 (#f5f5f5)

## 开发者

- **作者**：靳福库
- **网站**：福库心理 - 身心神同调
- **联系方式**：（待添加）

## 许可证

（待添加）

## 更新日志

### 2024-01-20
- ✅ 创建网站基础结构
- ✅ 实现三栏布局
- ✅ 创建5个分类
- ✅ 添加6篇示例文章
- ✅ 支持视频和音频嵌入

---

**身心神同调，开启生命的新可能** 🌱
