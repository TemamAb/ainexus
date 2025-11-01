from web3 import Web3
import asyncio
import time
from datetime import datetime

class LiveEthereumMonitor:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))
        self.connected = False
        
    async def start_live_monitoring(self):
        """Start real-time Ethereum monitoring"""
        print("Ì¥ó STARTING LIVE ETHEREUM MONITOR")
        print("Ì≥° Monitoring: Blocks, Gas Prices, Transactions")
        print("=" * 60)
        
        if not self.w3.is_connected():
            print("‚ùå Cannot connect to Ethereum")
            return
            
        self.connected = True
        last_block = self.w3.eth.block_number
        
        while self.connected:
            try:
                # Get current block
                current_block = self.w3.eth.block_number
                
                if current_block > last_block:
                    # New block mined
                    block = self.w3.eth.get_block(current_block)
                    
                    print(f"Ì∂ï BLOCK #{current_block:,} MINED")
                    print(f"   Time: {datetime.fromtimestamp(block.timestamp)}")
                    print(f"   Transactions: {len(block.transactions)}")
                    print(f"   Gas Used: {block.gas_used:,}")
                    print(f"   Miner: {block.miner}")
                    
                    # Get current gas prices
                    gas_price = self.w3.eth.gas_price
                    print(f"   Gas Price: {self.w3.from_wei(gas_price, 'gwei'):.1f} Gwei")
                    
                    last_block = current_block
                    print("-" * 50)
                
                await asyncio.sleep(2)  # Check every 2 seconds
                
            except Exception as e:
                print(f"‚ùå Monitoring error: {e}")
                await asyncio.sleep(5)

# Start live monitoring
async def main():
    monitor = LiveEthereumMonitor()
    await monitor.start_live_monitoring()

print("Ì∫Ä CONNECTING TO LIVE ETHEREUM MAINNET...")
asyncio.run(main())
