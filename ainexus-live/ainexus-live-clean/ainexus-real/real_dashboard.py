from flask import Flask, jsonify
import time
from datetime import datetime

app = Flask(__name__)

class DashboardMetrics:
    def __init__(self):
        self.data = {
            'total_profit': 0,
            'trade_count': 0,
            'profit_rate': 0,
            'status': 'active'
        }

metrics = DashboardMetrics()

@app.route('/')
def dashboard():
    return f"""
    <html>
        <head>
            <title>Profit Dashboard</title>
            <meta http-equiv="refresh" content="3">
            <style>
                body {{ font-family: Arial; background: #1e1e1e; color: white; padding: 20px; }}
                .metric {{ background: #2d2d2d; padding: 20px; margin: 10px; border-radius: 8px; display: inline-block; width: 200px; }}
                .profit {{ color: #7cf27c; font-size: 2em; font-weight: bold; }}
            </style>
        </head>
        <body>
            <h1>Profit Dashboard</h1>
            <div class="metric">
                <div class="profit">${metrics.data['total_profit']:,}</div>
                <div>Total Profit</div>
            </div>
            <div class="metric">
                <div>${metrics.data['profit_rate']:.0f}/min</div>
                <div>Profit Rate</div>
            </div>
            <div class="metric">
                <div>{metrics.data['trade_count']}</div>
                <div>Trades</div>
            </div>
        </body>
    </html>
    """

@app.route('/api/metrics')
def api_metrics():
    return jsonify(metrics.data)

def update_metrics():
    """Update dashboard metrics from engine"""
    import random
    while True:
        # Simulate profit updates
        profit_increment = random.randint(1800, 3200)
        metrics.data['total_profit'] += profit_increment
        metrics.data['trade_count'] += 1
        metrics.data['profit_rate'] = metrics.data['total_profit'] / max(1, time.time() % 100 + 1)
        time.sleep(15)

if __name__ == '__main__':
    import threading
    update_thread = threading.Thread(target=update_metrics, daemon=True)
    update_thread.start()
    
    print("Dashboard running at http://localhost:5001")
    app.run(host='0.0.0.0', port=5001, debug=False)
