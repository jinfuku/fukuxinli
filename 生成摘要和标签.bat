@echo off
chcp 65001 > nul
echo ========================================
echo 福库心理网站 - 自动生成摘要和标签
echo ========================================
echo.

cd /d %~dp0

echo 正在为所有文章生成摘要和标签...
echo.

python generate_summary_tags.py

echo.
echo ========================================
echo 处理完成！
echo ========================================
echo.

echo 提示：现在可以运行"快速更新网站.bat"来部署更新
echo.
pause
