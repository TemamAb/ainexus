@echo off
chcp 65001 > nul
echo íº€ STARTING AINEXUS LIVE TRADING ENGINE
echo.

echo í³¦ Installing dependencies...
pip install flask

echo í¾¯ Starting Profit Dashboard...
start python profit_api.py

echo í´„ Starting Arbitrage Engine...
timeout /t 3 /nobreak > nul
python arbitrage_engine.py

pause
