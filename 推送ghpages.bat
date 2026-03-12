@echo off
chcp 65001 > nul
echo ========================================
echo 推送 gh-pages 分支到 GitHub
echo ========================================
echo.

cd /d %~dp0
git checkout gh-pages-temp

echo 正在推送到 GitHub...
git push origin gh-pages-temp:gh-pages --force

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo 推送成功！
    echo ========================================
    echo.
    echo 下一步：
    echo 1. 访问 https://github.com/jinfuku28/fukuxinli/settings/pages
    echo 2. 在 Branch 下拉菜单中选择 "gh-pages" 分支
    echo 3. 点击 Save 按钮
    echo 4. 等待 1-3 分钟，网站将自动部署
    echo.
    echo 网站地址：https://jinfuku28.github.io/fukuxinli/
    echo ========================================
) else (
    echo.
    echo ========================================
    echo 推送失败，请检查：
    echo 1. 网络连接是否正常
    echo 2. GitHub 账户是否正常
    echo 3. 是否需要输入认证信息
    echo ========================================
)

echo.
echo 按任意键关闭窗口...
pause > nul
