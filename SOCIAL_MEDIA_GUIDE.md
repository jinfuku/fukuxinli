# 社交媒体配置指南

## 概述

福库身心同调网站已经添加了完整的社交媒体链接区域,支持13个主流社交平台,包括国内平台、国际平台和即时通讯工具。

---

## 一、当前支持的社交平台

### 国内主流平台
| 平台 | 类型 | 状态 | 账号名称 |
|------|------|------|----------|
| 微信公众号 | 二维码 | ⚠️ 需要二维码 | 福库身心同调 |
| 微信视频号 | 二维码 | ⚠️ 需要二维码 | 福库身心同调 |
| B站 | 外部链接 | ⚠️ 需要账号ID | 福库身心同调 |
| 小红书 | 外部链接 | ⚠️ 需要账号ID | 福库身心同调 |
| 抖音 | 外部链接 | ⚠️ 需要账号ID | 福库身心同调 |
| 今日头条 | 外部链接 | ⚠️ 需要账号ID | 福库身心同调 |
| 新浪微博 | 外部链接 | ⚠️ 需要账号ID | 福库身心同调 |
| 豆瓣 | 外部链接 | ⚠️ 需要账号ID | 福库身心同调 |
| 知识星球 | 外部链接 | ⚠️ 需要账号ID | 福库身心同调 |

### 国际主流平台 🆕
| 平台 | 类型 | 状态 | 账号名称 |
|------|------|------|----------|
| WhatsApp | 即时通讯 | ⚠️ 需要号码 | 福库身心同调 |
| Telegram | 即时通讯 | ⚠️ 需要用户名 | 福库身心同调 |
| Messenger | 社交链接 | ⚠️ 需要页面ID | 福库身心同调 |

### 即时通讯工具 🆕
| 平台 | 类型 | 状态 | 账号信息 |
|------|------|------|----------|
| QQ | 即时通讯 | ✅ 已配置 | 304269115 |
| 微信 | 即时通讯 | ✅ 已配置 | 16602677594 |

### 联系方式 🆕
| 方式 | 信息 | 状态 |
|------|------|------|
| 邮箱 | jinfuku@outlook.com | ✅ 已配置 |
| 微信 | 16602677594 | ✅ 已配置 |
| QQ | 304269115 | ✅ 已配置 |

---

## 二、配置步骤

### 2.1 邮箱配置

**当前配置：**
```html
<a href="mailto:jinfuku@outlook.com" style="color: #a1a1a6; text-decoration: none;">jinfuku@outlook.com</a>
```

**修改方法：**
如果需要更改邮箱地址,请将 `jinfuku@outlook.com` 替换为您的实际邮箱。

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

### 2.8 知识星球配置 🆕

**配置步骤：**

1. **获取知识星球链接**
   - 登录知识星球
   - 进入您的星球主页
   - 复制星球URL,格式为：`https://wx.zsxq.com/dweb2/index/group/星球ID`

2. **修改 HTML 代码**
   找到：
   ```html
   <a href="https://www.zsxq.com/your-id" target="_blank" class="social-card">
   ```

   将 `your-id` 替换为您的知识星球ID。

**示例：**
```html
<a href="https://wx.zsxq.com/dweb2/index/group/12345678" target="_blank" class="social-card">
```

---

### 2.9 WhatsApp配置 🆕

**配置步骤：**

1. **获取WhatsApp链接**
   - 格式为：`https://wa.me/国家代码+手机号`
   - 中国号码示例：`https://wa.me/8616602677594`

2. **修改 HTML 代码**
   找到：
   ```html
   <a href="https://wa.me/YOUR_PHONE_NUMBER" target="_blank" class="social-card">
   ```

   将 `YOUR_PHONE_NUMBER` 替换为您的手机号码(不含+号)。

**示例：**
```html
<a href="https://wa.me/8616602677594" target="_blank" class="social-card">
```

---

### 2.10 Telegram配置 🆕

**配置步骤：**

1. **获取Telegram链接**
   - 格式为：`https://t.me/用户名`
   - 不包含@符号

2. **修改 HTML 代码**
   找到：
   ```html
   <a href="https://t.me/YOUR_USERNAME" target="_blank" class="social-card">
   ```

   将 `YOUR_USERNAME` 替换为您的Telegram用户名。

**示例：**
```html
<a href="https://t.me/fukuxinli" target="_blank" class="social-card">
```

---

### 2.11 Messenger配置 🆕

**配置步骤：**

1. **获取Messenger链接**
   - 格式为：`https://m.me/页面ID`
   - 在Facebook主页或页面设置中获取页面ID

2. **修改 HTML 代码**
   找到：
   ```html
   <a href="https://m.me/YOUR_PAGE_ID" target="_blank" class="social-card">
   ```

   将 `YOUR_PAGE_ID` 替换为您的Facebook页面ID。

**示例：**
```html
<a href="https://m.me/123456789" target="_blank" class="social-card">
```

---

### 2.12 QQ配置 🆕

**配置步骤：**

1. **获取QQ链接**
   - 方式1: 直接打开聊天窗口 `tencent://message/?uin=QQ号`
   - 方式2: 打开资料页 `http://wpa.qq.com/msgrd?v=3&uin=QQ号&site=qq&menu=yes`

2. **修改 HTML 代码**
   找到：
   ```html
   <a href="tencent://message/?uin=QQ_NUMBER" target="_blank" class="social-card">
   ```

   将 `QQ_NUMBER` 替换为您的QQ号码。

**示例：**
```html
<a href="tencent://message/?uin=304269115" target="_blank" class="social-card">
```

---

## 三、品牌名称统一更新 🆕

### 3.1 需要更新的位置

**必须更新的位置：**
- ✅ 页面标题 (<title>)
- ✅ 页眉标题 (<h1>)
- ✅ 社交媒体区域标题和副标题
- ✅ 页脚品牌名称
- ✅ 版权声明
- ✅ 所有社交媒体卡片 (<p>标签)
- ✅ 导航菜单品牌名
- ✅ 联系方式中的品牌名

### 3.2 品牌信息配置

```markdown
品牌名称: 福库身心同调
核心概念: 身心神同调
Slogan: 开启生命的新可能
```

### 3.3 统一更新流程

使用AI助手执行以下指令：

```
"将所有'福库心理'替换为'福库身心同调'"
"更新所有社交媒体卡片的品牌名称"
"更新页眉、页脚的品牌名称"
"更新联系方式中的品牌名称"
```

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

配置完成后,请逐项测试：

### 国内平台测试
- [ ] 微信公众号卡片点击弹出二维码
- [ ] 微信视频号卡片点击弹出二维码
- [ ] B站链接可以跳转到正确的个人主页
- [ ] 小红书链接可以跳转到正确的个人主页
- [ ] 抖音链接可以跳转到正确的个人主页
- [ ] 今日头条链接可以跳转到正确的个人主页
- [ ] 新浪微博链接可以跳转到正确的个人主页
- [ ] 豆瓣链接可以跳转到正确的个人主页
- [ ] 知识星球链接可以跳转到正确的星球页面

### 国际平台测试 🆕
- [ ] WhatsApp链接可以打开WhatsApp应用
- [ ] Telegram链接可以打开Telegram应用
- [ ] Messenger链接可以打开Messenger应用

### 即时通讯测试 🆕
- [ ] QQ链接可以打开QQ聊天窗口
- [ ] 邮箱链接可以打开邮件客户端

### 通用测试
- [ ] 所有链接在新标签页打开(除即时通讯外)
- [ ] 悬停效果正常显示
- [ ] 移动端显示正常
- [ ] 所有平台账号名称统一为"福库身心同调" 🆕
- [ ] 联系信息准确无误 🆕

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
- 邮箱：jinfuku@outlook.com
- 微信：16602677594
- QQ：304269115
- 文档版本：v2.0
- 最后更新：2026-03-13

---

**福库身心同调 - 身心神同调** © 2026
