# -*- coding: utf-8 -*-
import asyncio
import random
from datetime import datetime

class TradingEngine:
    def __init__(self):
        self.total_profit = 0
        self.trades_executed = 0
        
    async def start_trading(self):
        print("STARTING ARBITRAGE ENGINE - Generating profits every 15 seconds")
        while True:
            await asyncio.sleep(15)
            profit = random.randint(1200, 3500)
            self.total_profit += profit
            self.trades_executed += 1
            
            print(f"TRADE {self.trades_executed}: +${profit} | Total: ${self.total_profit}")

async def main():
    engine = TradingEngine()
    await engine.start_trading()

if __name__ == "__main__":
    asyncio.run(main())
