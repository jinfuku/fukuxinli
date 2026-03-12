@echo off
chcp 65001 > nul
echo ========================================
echo 福库心理网站 - GitHub Pages 发布脚本
echo ========================================
echo.

REM 检查是否在正确的目录
if not exist "config.yaml" (
    echo ❌ 错误：未在正确的目录中运行此脚本
    echo 请在 fuku-psychology-website 目录中运行
    pause
    exit /b 1
)

echo ✅ 检测到网站项目
echo.

REM 检查 Git 是否已安装
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 错误：未检测到 Git
    echo 请先安装 Git：https://git-scm.com/downloads
    pause
    exit /b 1
)

echo ✅ Git 已安装
echo.

REM 检查是否已初始化 Git 仓库
if not exist ".git" (
    echo 📝 初始化 Git 仓库...
    git init
    echo ✅ Git 仓库已初始化
) else (
    echo ✅ Git 仓库已存在
)

echo.

REM 添加所有文件
echo 📝 添加文件到暂存区...
git add .
echo ✅ 文件已添加
echo.

REM 检查是否有更改需要提交
git diff --cached --quiet
if %errorlevel% equ 0 (
    echo ℹ️ 没有新的更改需要提交
    echo.
    set NO_CHANGES=1
) else (
    echo 📝 提交文件...
    git commit -m "更新福库心理网站内容"
    echo ✅ 文件已提交
    set NO_CHANGES=0
)

echo.

REM 检查是否已配置远程仓库
git remote get-url origin >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️ 未配置 GitHub 远程仓库
    echo.
    echo 请按照以下步骤操作：
    echo.
    echo 1. 访问 https://github.com/new 创建新仓库
    echo 2. 仓库名称：fuku-psychology-website
    echo 3. 选择 Public（公开）
    echo 4. 创建仓库后，将下面的命令中的 your-username 替换为您的 GitHub 用户名
    echo 5. 然后在当前目录运行：
    echo.
    echo    git remote add origin https://github.com/your-username/fuku-psychology-website.git
    echo    git branch -M main
    echo    git push -u origin main
    echo.
    pause
    exit /b 1
)

echo ✅ 远程仓库已配置
echo.

REM 推送到 GitHub
if "%NO_CHANGES%"=="0" (
    echo 📝 推送到 GitHub...
    git push -u origin main
    echo.
    echo ✅ 推送成功！
) else (
    echo ℹ️ 跳过推送（没有新的更改）
)

echo.
echo ========================================
echo 🎉 发布流程完成！
echo ========================================
echo.
echo 下一步：
echo 1. 访问您的 GitHub 仓库
echo 2. 点击 Settings → Pages
echo 3. 确保 Source 设置为：Deploy from a branch
echo 4. 确保 Branch 设置为：main
echo 5. 等待 1-5 分钟，网站将自动部署
echo.
echo 网站地址：
echo https://your-username.github.io/fuku-psychology-website
echo （请将 your-username 替换为您的 GitHub 用户名）
echo.
pause
