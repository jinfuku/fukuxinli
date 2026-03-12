@echo off
chcp 65001 > nul
echo ========================================
echo 福库心理网站 - 本地预览脚本
echo ========================================
echo.

echo 📝 启动本地服务器...
echo.

REM 检查 Python 是否已安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 错误：未检测到 Python
    echo 请先安装 Python：https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python 已安装
echo.

REM 启动 Python HTTP 服务器
echo 🚀 启动服务器在端口 8000...
echo.
echo 网站地址：http://localhost:8000
echo.
echo 按 Ctrl+C 停止服务器
echo.
echo ========================================
echo.

python -m http.server 8000
