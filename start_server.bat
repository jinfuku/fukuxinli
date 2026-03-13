@echo off
echo Starting local server...
echo Please open your browser and visit: http://localhost:8000
echo Press Ctrl+C to stop the server
echo.
python -m http.server 8000
pause