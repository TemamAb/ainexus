from web3 import Web3
import time

print("VERIFYING ETHEREUM NETWORK CONNECTION")
print("======================================")

w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/AiTkecJt-cMKIYl_Wm3W5"))

if not w3.is_connected():
    print("NOT CONNECTED")
    exit(1)

print(f"Chain ID: {w3.eth.chain_id}")
print(f"Current Block: #{w3.eth.block_number:,}")
print(f"Gas Price: {w3.from_wei(w3.eth.gas_price, 'gwei'):.1f} Gwei")
print(f"Client: {w3.client_version}")

# Check block timing
print("\nCHECKING BLOCK TIMING...")
block1 = w3.eth.block_number
time1 = w3.eth.get_block(block1)['timestamp']
print(f"Block #{block1:,} timestamp: {time1}")

time.sleep(15)  # Wait 15 seconds

block2 = w3.eth.block_number  
time2 = w3.eth.get_block(block2)['timestamp']
print(f"Block #{block2:,} timestamp: {time2}")

if block2 > block1:
    time_diff = time2 - time1
    block_diff = block2 - block1
    print(f"Time between blocks: {time_diff} seconds")
    print(f"Blocks mined: {block_diff}")
    
    if time_diff < 10 and block_diff > 1:
        print("❌ SUSPICIOUS: Blocks are too close together")
        print("   This might be a testnet or RPC issue")
    else:
        print("✅ Block timing looks normal")
else:
    print("No new blocks mined")
