from flask import Flask, request, jsonify
import os
from live_data_engine import LiveArbitrageEngine
from blockchain_integration import BlockchainOrchestrator
from arbitrage_detector import ArbitrageDetector

app = Flask(__name__)
trading_engine = LiveArbitrageEngine()
blockchain = BlockchainOrchestrator()
arbitrage = ArbitrageDetector()

@app.route('/live-status')
def live_status():
    return {
        "status": "QUANTUM ENGINE - LIVE TRADING",
        "live_metrics": {
            "opportunities_scanned": 0,
            "active_trades": 0,
            "total_profit": 0,
            "success_rate": "0%"
        },
        "blockchain_connectivity": "CONNECTING",
        "timestamp": "2024-01-15T00:00:00Z"
    }

@app.route('/start-trading', methods=['POST'])
def start_trading():
    user_wallet = request.json.get('wallet_address')
    capital_amount = request.json.get('capital')
    return {"status": "TRADING_ACTIVE", "wallet": user_wallet, "capital": capital_amount}

@app.route('/scan-opportunities')
def scan_opportunities():
    opportunities = arbitrage.find_triangular_opportunities()
    return jsonify({"opportunities": opportunities})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
