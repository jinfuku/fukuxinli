# 社交媒体配置指南

## 概述

福库心理网站已经添加了完整的社交媒体链接区域，包括邮箱、微信公众号、微信视频号、B站、搜狐、新浪微博、豆瓣、孔夫子等平台。

---

## 一、当前支持的社交平台

| 平台 | 类型 | 状态 |
|------|------|------|
| 邮箱 | email | ✅ 已配置 |
| 微信公众号 | 二维码 | ⚠️ 需要二维码 |
| 微信视频号 | 二维码 | ⚠️ 需要二维码 |
| B站 | 外部链接 | ⚠️ 需要账号ID |
| 搜狐 | 外部链接 | ⚠️ 需要账号ID |
| 新浪微博 | 外部链接 | ⚠️ 需要账号ID |
| 豆瓣 | 外部链接 | ⚠️ 需要账号ID |
| 孔夫子 | 外部链接 | ⚠️ 需要账号ID |

---

## 二、配置步骤

### 2.1 邮箱配置

**当前配置：**
```html
<a href="mailto:contact@fukuxinli.com" class="social-card">
  <div class="social-icon email-icon"></div>
  <h3>邮箱</h3>
  <p>contact@fukuxinli.com</p>
</a>
```

**修改方法：**
如果需要更改邮箱地址，请将 `contact@fukuxinli.com` 替换为您的实际邮箱。

---

### 2.2 微信公众号配置

**配置步骤：**

1. **获取公众号二维码**
   - 登录微信公众平台
   - 进入"设置" → "公众号设置" → "二维码"
   - 下载公众号二维码图片

2. **将二维码图片放到网站目录**
   ```
   fuku-psychology-website/
   └── static/
       └── qrcodes/
           ├── wechat-official.jpg      # 微信公众号二维码
           └── wechat-video.jpg         # 微信视频号二维码
   ```

3. **修改 HTML 代码**
   找到以下代码：
   ```html
   <div class="qr-placeholder">
     <p>二维码图片</p>
     <small>请在此处放置您的二维码</small>
   </div>
   ```

   替换为：
   ```html
   <img src="/qrcodes/wechat-official.jpg" alt="微信公众号二维码" style="width: 100%; height: auto; border-radius: 12px;">
   ```

4. **配置弹窗触发**
   找到微信公众号卡片：
   ```html
   <a href="#" class="social-card" onclick="return false;">
     <div class="social-icon wechat-icon"></div>
     <h3>微信公众号</h3>
     <p>福库心理</p>
     <span class="qr-hint">扫码关注</span>
   </a>
   ```

   点击后会弹出二维码显示窗口。

---

### 2.3 微信视频号配置

**配置步骤：**

1. **获取视频号二维码**
   - 打开微信视频号
   - 进入您的视频号主页
   - 点击右上角"..." → "分享视频号" → "保存二维码"

2. **放置二维码图片**
   ```
   fuku-psychology-website/
   └── static/
       └── qrcodes/
           └── wechat-video.jpg         # 微信视频号二维码
   ```

3. **修改弹窗中的图片**
   参照微信公众号的配置方法，修改视频号二维码的显示。

---

### 2.4 B站配置

**配置步骤：**

1. **获取B站链接**
   - 登录B站账号
   - 进入个人主页
   - 复制个人主页URL，格式为：`https://space.bilibili.com/你的数字ID`

2. **修改 HTML 代码**
   找到：
   ```html
   <a href="https://space.bilibili.com/your-id" target="_blank" class="social-card">
   ```

   将 `your-id` 替换为您的实际B站用户ID。

   **示例：**
   ```html
   <a href="https://space.bilibili.com/123456789" target="_blank" class="social-card">
   ```

---

### 2.5 搜狐配置

**配置步骤：**

1. **获取搜狐链接**
   - 登录搜狐账号
   - 进入个人主页
   - 复制个人主页URL

2. **修改 HTML 代码**
   找到：
   ```html
   <a href="https://www.sohu.com/user/your-id" target="_blank" class="social-card">
   ```

   将 `your-id` 替换为您的搜狐用户ID。

---

### 2.6 新浪微博配置

**配置步骤：**

1. **获取微博链接**
   - 登录新浪微博
   - 进入个人主页
   - 复制个人主页URL，格式为：`https://weibo.com/你的用户名或ID`

2. **修改 HTML 代码**
   找到：
   ```html
   <a href="https://weibo.com/your-id" target="_blank" class="social-card">
   ```

   将 `your-id` 替换为您的微博用户名或ID。

   **示例：**
   ```html
   <a href="https://weibo.com/fukuxinli" target="_blank" class="social-card">
   ```

---

### 2.7 豆瓣配置

**配置步骤：**

1. **获取豆瓣链接**
   - 登录豆瓣
   - 进入个人主页
   - 复制个人主页URL

2. **修改 HTML 代码**
   找到：
   ```html
   <a href="https://www.douban.com/people/your-id" target="_blank" class="social-card">
   ```

   将 `your-id` 替换为您的豆瓣用户名。

---

### 2.8 孔夫子配置

**配置步骤：**

1. **获取孔夫子链接**
   - 登录孔夫子旧书网
   - 进入个人主页
   - 复制个人主页URL

2. **修改 HTML 代码**
   找到：
   ```html
   <a href="https://www.kongfz.com/user/your-id" target="_blank" class="social-card">
   ```

   将 `your-id` 替换为您的孔夫子用户ID。

---

## 三、二维码图片优化建议

### 3.1 图片尺寸

- **推荐尺寸**：500px × 500px 或更大
- **格式**：JPG 或 PNG
- **文件大小**：< 200KB

### 3.2 图片优化

```bash
# 使用 ImageOptim（Mac）或类似工具压缩图片
# 或使用在线工具：https://tinypng.com/
```

### 3.3 二维码样式

- 确保二维码清晰可扫
- 可以在二维码周围添加白色边框
- 保持二维码的中心对齐

---

## 四、自定义样式

### 4.1 修改卡片颜色

如果要修改某个社交平台的颜色，找到对应的 CSS 类：

```css
.wechat-icon {
  background: linear-gradient(135deg, #07c160 0%, #06ad56 100%);
  /* 修改这里的颜色值 */
}
```

### 4.2 添加新的社交平台

如果要添加新的社交平台，在 `.social-grid` 中添加新的卡片：

```html
<a href="your-url" class="social-card">
  <div class="social-icon new-platform-icon"></div>
  <h3>平台名称</h3>
  <p>平台描述</p>
</a>
```

然后添加对应的 CSS：

```css
.new-platform-icon {
  background: linear-gradient(135deg, #your-color 0%, #your-color 100%);
  color: white;
  box-shadow: 0 4px 12px rgba(your-color-rgb, 0.3);
}
```

---

## 五、AI 助手配置指令

使用 AI 助手快速配置社交媒体：

```
"将邮箱地址改为 myemail@example.com"
"设置B站链接为 https://space.bilibili.com/123456"
"添加微信公众号二维码 /qrcodes/wechat.jpg"
"设置微博链接为 https://weibo.com/fukuxinli"
"更新豆瓣链接"
```

---

## 六、测试清单

配置完成后，请逐项测试：

- [ ] 邮箱链接可以打开邮件客户端
- [ ] 微信公众号卡片点击弹出二维码
- [ ] 微信视频号卡片点击弹出二维码
- [ ] B站链接可以跳转到正确的个人主页
- [ ] 搜狐链接可以跳转到正确的个人主页
- [ ] 新浪微博链接可以跳转到正确的个人主页
- [ ] 豆瓣链接可以跳转到正确的个人主页
- [ ] 孔夫子链接可以跳转到正确的个人主页
- [ ] 所有链接在新标签页打开
- [ ] 悬停效果正常显示
- [ ] 移动端显示正常

---

## 七、常见问题

### Q1: 如何获取B站用户ID？

**A:** 登录B站后，进入个人主页，查看浏览器地址栏，URL 格式为 `https://space.bilibili.com/123456789`，其中的数字就是用户ID。

### Q2: 微信二维码在哪里？

**A:** 微信公众号和视频号的二维码需要从微信客户端获取：
- 公众号：在微信公众平台下载
- 视频号：在微信视频号中保存二维码

### Q3: 如何测试链接是否正确？

**A:** 在浏览器中直接打开链接，确认能够跳转到正确的页面。

### Q4: 可以添加其他社交平台吗？

**A:** 可以，参照"添加新的社交平台"部分进行配置。

---

## 八、维护建议

1. **定期检查链接** - 确保所有链接都是有效的
2. **更新二维码** - 如果更换了微信二维码，及时更新网站
3. **添加新平台** - 随着业务发展，可以添加更多社交平台
4. **用户反馈** - 收集用户对社交媒体区域的反馈，持续优化

---

## 九、联系方式

如有问题，请联系：
- 邮箱：contact@fukuxinli.com
- 文档版本：v1.0
- 最后更新：2026-03-13

---

**福库心理 - 身心神同调** © 2026
