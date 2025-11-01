import os
from web3 import Web3

print("� CHECKING REAL ETHEREUM MAINNET CONNECTION")
print("=============================================")

# Use your real Infura endpoint
w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{os.getenv('INFURA_API_KEY')}"))

if w3.is_connected():
    print(f"✅ CONNECTED TO REAL ETHEREUM MAINNET")
    print(f"� Current Block: #{w3.eth.block_number:,}")
    print(f"⛽ Gas Price: {w3.from_wei(w3.eth.gas_price, 'gwei'):.1f} Gwei")
    print(f"� Network Status: LIVE")
    
    # Check account balance if private key is configured
    if os.getenv('DEPLOYER_PRIVATE_KEY'):
        account = w3.eth.account.from_key(os.getenv('DEPLOYER_PRIVATE_KEY'))
        balance = w3.eth.get_balance(account.address)
        print(f"� Account Balance: {w3.from_wei(balance, 'ether'):.4f} ETH")
        print(f"� Account Address: {account.address}")
else:
    print("❌ FAILED TO CONNECT TO ETHEREUM")
