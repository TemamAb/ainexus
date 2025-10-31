#!/bin/bash
echo "íº€ STARTING AINEXUS LIVE TRADING ENGINE"
echo ""

echo "í³¦ Installing dependencies..."
pip install flask

echo "í¾¯ Starting Profit Dashboard..."
python profit_api.py &

echo "í´„ Starting Arbitrage Engine..."
sleep 3
python arbitrage_engine.py
