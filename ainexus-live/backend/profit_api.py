from flask import Flask, jsonify
import threading
import time
import json
from datetime import datetime

app = Flask(__name__)

class ProfitTracker:
    def __init__(self):
        self.total_profit = 0
        self.profit_history = []
        self.start_time = datetime.now()
        
    def add_profit(self, amount):
        self.total_profit += amount
        self.profit_history.append({
            'timestamp': datetime.now().isoformat(),
            'amount': amount,
            'total': self.total_profit
        })
        print(f"í²° Profit recorded: ${amount} | Total: ${self.total_profit}")

profit_tracker = ProfitTracker()

@app.route('/api/live-profit')
def live_profit():
    return jsonify({
        'total_profit': profit_tracker.total_profit,
        'runtime_minutes': (datetime.now() - profit_tracker.start_time).total_seconds() / 60,
        'profit_per_minute': profit_tracker.total_profit / max(1, (datetime.now() - profit_tracker.start_time).total_seconds() / 60),
        'trade_count': len(profit_tracker.profit_history),
        'latest_trades': profit_tracker.profit_history[-10:] if profit_tracker.profit_history else []
    })

@app.route('/api/execute-trade')
def execute_trade():
    # Simulate profitable trade
    profit = 2100  # $2,100 profit per trade
    profit_tracker.add_profit(profit)
    
    return jsonify({
        'status': 'success',
        'profit': profit,
        'total_profit': profit_tracker.total_profit
    })

def simulate_trading():
    """Simulate continuous profitable trading"""
    while True:
        time.sleep(30)  # Execute trade every 30 seconds
        profit = 1800 + (time.time() % 1000)  # $1,800 - $2,800 profit range
        profit_tracker.add_profit(profit)

if __name__ == '__main__':
    # Start simulated trading in background
    trading_thread = threading.Thread(target=simulate_trading, daemon=True)
    trading_thread.start()
    
    app.run(host='0.0.0.0', port=5001, debug=False)
