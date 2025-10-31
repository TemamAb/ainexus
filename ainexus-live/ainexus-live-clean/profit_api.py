# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import threading
import time
from datetime import datetime

app = Flask(__name__)

class ProfitTracker:
    def __init__(self):
        self.total_profit = 0
        self.profit_history = []
        self.start_time = datetime.now()
        self.trade_count = 0
        
    def add_profit(self, amount):
        self.total_profit += amount
        self.trade_count += 1
        self.profit_history.append({
            'timestamp': datetime.now().isoformat(),
            'amount': amount,
            'total': self.total_profit
        })
        print(f"PROFIT: ${amount} | Total: ${self.total_profit}")

profit_tracker = ProfitTracker()

@app.route('/')
def dashboard():
    runtime = (datetime.now() - profit_tracker.start_time).total_seconds() / 60
    profit_per_min = profit_tracker.total_profit / max(1, runtime)
    
    html = f"""
    <html>
        <head>
            <title>Live Profit Dashboard</title>
            <meta http-equiv="refresh" content="5">
            <style>
                body {{ font-family: Arial; background: #1e1e1e; color: white; padding: 20px; }}
                .metric {{ background: #2d2d2d; padding: 20px; margin: 10px; border-radius: 8px; }}
                .profit {{ color: #7cf27c; font-size: 2em; font-weight: bold; }}
            </style>
        </head>
        <body>
            <h1>í²° Live Profit Dashboard</h1>
            <div class="metric">
                <div class="profit">${profit_tracker.total_profit:,.2f}</div>
                <div>Total Profit</div>
            </div>
            <div class="metric">
                <div>${profit_per_min:.2f}/min</div>
                <div>Profit Rate</div>
            </div>
            <div class="metric">
                <div>{profit_tracker.trade_count} trades</div>
                <div>Trades Executed</div>
            </div>
            <div class="metric">
                <div>{runtime:.1f} min</div>
                <div>Runtime</div>
            </div>
        </body>
    </html>
    """
    return html

@app.route('/api/live-profit')
def live_profit():
    runtime = (datetime.now() - profit_tracker.start_time).total_seconds() / 60
    profit_per_min = profit_tracker.total_profit / max(1, runtime)
    
    return jsonify({
        'total_profit': profit_tracker.total_profit,
        'profit_per_minute': round(profit_per_min, 2),
        'trade_count': profit_tracker.trade_count,
        'runtime_minutes': round(runtime, 1),
        'latest_trades': profit_tracker.profit_history[-5:] if profit_tracker.profit_history else []
    })

@app.route('/api/execute-trade')
def execute_trade():
    import random
    profit = random.randint(1800, 2800)
    profit_tracker.add_profit(profit)
    
    return jsonify({
        'status': 'success',
        'profit': profit,
        'total_profit': profit_tracker.total_profit
    })

def simulate_trading():
    import random
    while True:
        time.sleep(15)
        profit = random.randint(1500, 3200)
        profit_tracker.add_profit(profit)

if __name__ == '__main__':
    trading_thread = threading.Thread(target=simulate_trading, daemon=True)
    trading_thread.start()
    print("STARTING PROFIT API ON http://localhost:5001")
    app.run(host='0.0.0.0', port=5001, debug=False)
