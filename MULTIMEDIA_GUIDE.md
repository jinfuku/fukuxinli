# 多媒体内容使用指南

## 概述

福库心理网站支持在文章中插入图片、视频和音频内容，以丰富阅读体验，提供更全面的信息传达。

---

## 一、图片插入

### 1.1 基础图片

在 Markdown 文章中插入图片：

```html
<img src="/images/example.jpg" alt="示例图片">
```

**参数说明：**
- `src`: 图片路径（相对于网站根目录）
- `alt`: 图片描述（用于辅助功能和 SEO）

### 1.2 带标题的图片

```html
<div class="image-container">
  <img src="/images/example.jpg" alt="示例图片">
  <p class="image-caption">图1：示例图片说明</p>
</div>
```

### 1.3 图片路径建议

```
fuku-psychology-website/
├── static/
│   └── images/
│       ├── articles/          # 文章图片
│       ├── books/            # 书籍封面
│       ├── gallery/          # 图片画廊
│       └── icons/            # 图标
└── content/
    └── posts/
        └── article.md        # 文章内容
```

**使用示例：**
```html
<img src="/images/articles/breathing-exercise.jpg" alt="呼吸练习示意图">
```

---

## 二、视频插入

### 2.1 本地视频

```html
<div class="video-container">
  <video controls>
    <source src="/videos/introduction.mp4" type="video/mp4">
    您的浏览器不支持视频播放。
  </video>
</div>
```

### 2.2 在线视频（YouTube/Bilibili）

**YouTube:**
```html
<div class="video-container">
  <iframe
    src="https://www.youtube.com/embed/VIDEO_ID"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
  </iframe>
</div>
```

**Bilibili:**
```html
<div class="video-container">
  <iframe
    src="//player.bilibili.com/player.html?aid=VIDEO_ID&page=1"
    scrolling="no"
    border="0"
    frameborder="no"
    framespacing="0"
    allowfullscreen="true">
  </iframe>
</div>
```

### 2.3 视频预览卡片

```html
<div class="video-preview-card">
  <img src="/images/video-thumbnail.jpg" alt="视频缩略图">
  <div class="play-icon"></div>
</div>
```

### 2.4 视频文件路径建议

```
fuku-psychology-website/
├── static/
│   └── videos/
│       ├── lectures/         # 讲座视频
│       ├── exercises/        # 练习视频
│       └── interviews/       # 访谈视频
```

---

## 三、音频插入

### 3.1 基础音频播放器

```html
<div class="audio-container">
  <p class="audio-title">呼吸引导练习 - 10分钟</p>
  <audio controls>
    <source src="/audio/breathing.mp3" type="audio/mpeg">
    <source src="/audio/breathing.ogg" type="audio/ogg">
    您的浏览器不支持音频播放。
  </audio>
</div>
```

### 3.2 音频文件路径建议

```
fuku-psychology-website/
├── static/
│   └── audio/
│       ├── meditations/      # 冥想音频
│       ├── lectures/         # 讲座音频
│       └── music/            # 背景音乐
```

### 3.3 支持的音频格式

- **MP3** - 通用格式，兼容性最好
- **OGG** - 开源格式
- **WAV** - 无损格式（文件较大）

---

## 四、完整示例

### 4.1 文章中的多媒体内容

```markdown
# 呼吸练习指南

## 引言

呼吸是身心连接的重要桥梁。以下是一个完整的呼吸练习教程。

## 视频教程

<div class="video-container">
  <video controls>
    <source src="/videos/breathing-exercise.mp4" type="video/mp4">
    您的浏览器不支持视频播放。
  </video>
</div>

## 步骤说明

### 准备姿势

<div class="image-container">
  <img src="/images/articles/sitting-posture.jpg" alt="正确坐姿示意图">
  <p class="image-caption">图1：正确的坐姿</p>
</div>

保持脊柱挺直，肩膀放松。

### 呼吸练习

跟随以下音频进行练习：

<div class="audio-container">
  <p class="audio-title">10分钟呼吸引导练习</p>
  <audio controls>
    <source src="/audio/meditations/breathing-10min.mp3" type="audio/mpeg">
    您的浏览器不支持音频播放。
  </audio>
</div>

## 注意事项

- 选择安静的环境
- 练习时保持专注
- 初学者可以从5分钟开始
```

### 4.2 书籍推荐配图

```html
<div class="article">
  <h3>《爱情刽子手》</h3>
  <div class="image-container">
    <img src="/images/books/love-executioner.jpg" alt="《爱情刽子手》封面">
    <p class="image-caption">图：《爱情刽子手》封面</p>
  </div>
  <p>欧文·亚隆的经典著作...</p>
</div>
```

---

## 五、最佳实践

### 5.1 图片优化

- **尺寸**：建议宽度不超过 1200px
- **格式**：
  - 照片使用 JPEG（质量 80-85%）
  - 图标、图表使用 PNG 或 SVG
  - 现代浏览器支持 WebP（更小体积）
- **大小**：单个图片不超过 500KB

### 5.2 视频优化

- **分辨率**：1080p（1920x1080）或 720p（1280x720）
- **格式**：MP4（H.264 编码）
- **大小**：单段视频不超过 200MB
- **时长**：建议不超过 30 分钟

### 5.3 音频优化

- **格式**：MP3（128kbps 或 192kbps）
- **大小**：单段音频不超过 20MB
- **时长**：建议不超过 60 分钟

### 5.4 无障碍访问

- 所有图片必须添加 `alt` 描述
- 视频提供字幕（如可能）
- 音频提供文字版内容

---

## 六、样式类说明

### 6.1 图片相关

| 类名 | 用途 |
|------|------|
| `image-container` | 图片容器，居中显示 |
| `image-caption` | 图片说明文字 |

### 6.2 视频相关

| 类名 | 用途 |
|------|------|
| `video-container` | 视频容器，自适应宽度 |
| `video-preview-card` | 视频预览卡片 |
| `play-icon` | 播放图标 |

### 6.3 音频相关

| 类名 | 用途 |
|------|------|
| `audio-container` | 音频容器，带背景 |
| `audio-title` | 音频标题 |

---

## 七、故障排查

### 7.1 图片不显示

**问题：** 图片显示为破损图标

**解决方法：**
1. 检查路径是否正确
2. 确认文件扩展名大小写
3. 验证文件是否存在

### 7.2 视频无法播放

**问题：** 视频显示无法播放

**解决方法：**
1. 检查视频格式是否支持（推荐 MP4）
2. 确认视频编码（推荐 H.264）
3. 检查文件大小是否过大

### 7.3 音频没有声音

**问题：** 音频播放但没有声音

**解决方法：**
1. 检查系统音量
2. 确认音频文件是否完整
3. 尝试其他格式

---

## 八、AI 助手使用指令

使用 AI 助手添加多媒体内容：

```
"在文章《呼吸练习指南》中插入一张坐姿示意图"
"为《心理治疗案例》添加视频教程链接"
"在文章开头添加背景音乐"
```

---

## 九、更新日志

| 日期 | 更新内容 |
|------|---------|
| 2026-03-13 | 创建多媒体使用指南 |
| 2026-03-13 | 添加图片、视频、音频样式支持 |
| 2026-03-13 | 添加响应式布局优化 |

---

## 十、联系方式

如有问题或建议，请联系：
- 邮箱：support@fukuxinli.com
- 文档版本：v1.0

---

**福库心理 - 身心神同调** © 2026
