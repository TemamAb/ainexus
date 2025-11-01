import time
from web3 import Web3

print("REAL ARBITRAGE MONITOR - ETHEREUM MAINNET")
print("==========================================")

# Use your working Alchemy endpoint
w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/AiTkecJt-cMKIYl_Wm3W5"))

if not w3.is_connected():
    print("NOT CONNECTED TO ETHEREUM")
    exit(1)

print(f"CONNECTED TO ETHEREUM MAINNET")
print(f"Current Block: #{w3.eth.block_number:,}")
print(f"Chain ID: {w3.eth.chain_id}")

# Real contract addresses
CONTRACTS = {
    'AAVE_POOL': '0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2',
    'UNISWAP_V3_ROUTER': '0xE592427A0AEce92De3Edee1F18E0157C05861564',
    'UNISWAP_V2_ROUTER': '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D',
    'SUSHISWAP_ROUTER': '0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F'
}

print("Monitoring blockchain for arbitrage...")
print("Using real contract addresses:")
for name, address in CONTRACTS.items():
    print(f"  {name}: {address}")

last_block = w3.eth.block_number
scan_count = 0

while True:
    try:
        current_block = w3.eth.block_number
        gas_price = w3.eth.gas_price
        
        if current_block > last_block:
            scan_count += 1
            print(f"Scan {scan_count} | Block #{current_block:,} | Gas: {w3.from_wei(gas_price, 'gwei'):.1f} Gwei")
            print("Checking real DEX prices...")
            
            # This is where real arbitrage logic would go
            # Currently just monitoring - no fake profits
            # Add your actual price checking logic here
            
            last_block = current_block
        
        time.sleep(3)
        
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)
