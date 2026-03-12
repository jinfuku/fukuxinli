@echo off
chcp 65001 > nul
echo ========================================
echo 福库心理网站 - 快速更新
echo ========================================
echo.

cd /d %~dp0

echo 第一步：构建网站...
hugo
if %errorlevel% neq 0 (
    echo 构建失败！
    pause
    exit /b 1
)
echo 构建成功！
echo.

echo 第二步：提交源代码...
git add .
git commit -m "更新网站内容"
git push origin main
if %errorlevel% neq 0 (
    echo 推送源代码失败！
    pause
    exit /b 1
)
echo 源代码推送成功！
echo.

echo 第三步：部署到 GitHub Pages...
git checkout --orphan gh-pages-temp
git rm -rf .
xcopy /E /I /Y public\* .
git add .
git commit -m "Deploy to GitHub Pages"
git push origin gh-pages-temp:gh-pages --force
if %errorlevel% neq 0 (
    echo 部署失败！
    git checkout main
    git branch -D gh-pages-temp
    pause
    exit /b 1
)
echo 部署成功！
echo.

echo 第四步：清理临时分支...
git checkout main
git branch -D gh-pages-temp
echo 清理完成！
echo.

echo ========================================
echo 更新完成！
echo 网站地址：https://jinfuku.github.io/fukuxinli/
echo ========================================
echo.

echo 等待 1-3 分钟，网站将自动更新...
pause
