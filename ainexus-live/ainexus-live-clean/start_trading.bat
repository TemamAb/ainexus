@echo off
chcp 65001 > nul
echo � STARTING AINEXUS LIVE TRADING ENGINE
echo.

echo � Installing dependencies...
pip install flask

echo � Starting Profit Dashboard...
start python profit_api.py

echo � Starting Arbitrage Engine...
timeout /t 3 /nobreak > nul
python arbitrage_engine.py

pause
