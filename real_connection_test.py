import os
from web3 import Web3

print("REAL ETHEREUM MAINNET CONNECTION TEST")
print("======================================")

# Test with your Infura key
infura_url = f"https://mainnet.infura.io/v3/{os.getenv('INFURA_API_KEY')}"
print(f"Connecting to: {infura_url}")

try:
    w3 = Web3(Web3.HTTPProvider(infura_url, request_kwargs={'timeout': 30}))
    
    if w3.is_connected():
        block = w3.eth.block_number
        gas_price = w3.eth.gas_price
        chain_id = w3.eth.chain_id
        
        print("✅ CONNECTED TO REAL ETHEREUM MAINNET")
        print(f"   Chain ID: {chain_id}")
        print(f"   Current Block: #{block:,}")
        print(f"   Gas Price: {w3.from_wei(gas_price, 'gwei'):.1f} Gwei")
        print(f"   Client: {w3.client_version}")
        
        # Test real contract interaction
        print(f"   Network: LIVE MAINNET")
    else:
        print("❌ FAILED TO CONNECT TO ETHEREUM")
        
except Exception as e:
    print(f"❌ CONNECTION ERROR: {e}")
