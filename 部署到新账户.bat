@echo off
chcp 65001 > nul
echo ========================================
echo 福库心理网站 - 部署到新账户
echo ========================================
echo.
echo 目标仓库：https://github.com/jinfuku/fukuxinli
echo.

cd /d %~dp0

echo 第一步：提交更改到 main 分支...
git add .
git commit -m "更新配置，切换到新账户"
echo 提交完成！
echo.

echo 第二步：推送 main 分支到 GitHub...
git push -u origin main
if %errorlevel% neq 0 (
    echo 推送失败！请检查：
    echo 1. 网络连接是否正常
    echo 2. GitHub 账户认证信息
    echo.
    pause
    exit /b 1
)
echo 推送成功！
echo.

echo 第三步：创建并推送 gh-pages 分支...
git checkout --orphan gh-pages
git rm -rf .
xcopy /E /I /Y public\* .
git add .
git commit -m "Deploy to GitHub Pages"
git push origin gh-pages
if %errorlevel% neq 0 (
    echo 推送 gh-pages 分支失败！
    git checkout main
    pause
    exit /b 1
)
echo 推送成功！
echo.

echo 第四步：切换回 main 分支...
git checkout main
echo.

echo ========================================
echo 部署成功！
echo ========================================
echo.
echo 下一步操作：
echo 1. 访问 https://github.com/jinfuku/fukuxinli/settings/pages
echo 2. 在 Branch 下拉菜单中选择 "gh-pages" 分支
echo 3. 点击 Save 按钮
echo 4. 等待 1-3 分钟
echo.
echo 网站地址：https://jinfuku.github.io/fukuxinli/
echo ========================================

pause
