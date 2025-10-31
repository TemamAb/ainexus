#!/bin/bash
echo "� STARTING AINEXUS LIVE TRADING ENGINE"
echo ""

echo "� Installing dependencies..."
pip install flask

echo "� Starting Profit Dashboard..."
python profit_api.py &

echo "� Starting Arbitrage Engine..."
sleep 3
python arbitrage_engine.py
