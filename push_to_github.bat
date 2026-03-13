@echo off
chcp 65001 > nul
echo ========================================
echo 推送到 GitHub Pages
echo ========================================
echo.

cd /d "%~dp0"
git push origin gh-pages

echo.
echo ========================================
echo 推送完成!
echo ========================================
echo.
echo 您的网站将会在几分钟内更新:
echo https://jinfu-fuku.github.io/fukuxinli/
echo.
pause
