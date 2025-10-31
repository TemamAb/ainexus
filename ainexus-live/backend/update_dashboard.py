import requests
import time
import json
from datetime import datetime

def update_dashboard_with_live_profit():
    """Update the main dashboard with live profit data"""
    try:
        # Get live profit data
        response = requests.get('http://localhost:5001/api/live-profit')
        profit_data = response.json()
        
        # Format for dashboard display
        dashboard_update = {
            'live_metrics': {
                'total_profit_usd': profit_data['total_profit'],
                'profit_per_minute': round(profit_data['profit_per_minute'], 2),
                'active_trades': profit_data['trade_count'],
                'runtime_minutes': round(profit_data['runtime_minutes'], 1)
            },
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"í³ˆ LIVE PROFIT UPDATE:")
        print(f"   Total Profit: ${profit_data['total_profit']:,.2f}")
        print(f"   Profit/Minute: ${profit_data['profit_per_minute']:.2f}")
        print(f"   Trades Executed: {profit_data['trade_count']}")
        print(f"   Runtime: {profit_data['runtime_minutes']:.1f} minutes")
        print("-" * 50)
        
        return dashboard_update
        
    except Exception as e:
        print(f"Error updating dashboard: {e}")
        return None

# Continuous dashboard updates
if __name__ == "__main__":
    while True:
        update_dashboard_with_live_profit()
        time.sleep(10)  # Update every 10 seconds
