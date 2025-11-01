import os
from web3 import Web3

print("Ì¥ó CHECKING REAL ETHEREUM MAINNET CONNECTION")
print("=============================================")

# Use your real Infura endpoint
w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{os.getenv('INFURA_API_KEY')}"))

if w3.is_connected():
    print(f"‚úÖ CONNECTED TO REAL ETHEREUM MAINNET")
    print(f"Ì≥¶ Current Block: #{w3.eth.block_number:,}")
    print(f"‚õΩ Gas Price: {w3.from_wei(w3.eth.gas_price, 'gwei'):.1f} Gwei")
    print(f"Ìµí Network Status: LIVE")
    
    # Check account balance if private key is configured
    if os.getenv('DEPLOYER_PRIVATE_KEY'):
        account = w3.eth.account.from_key(os.getenv('DEPLOYER_PRIVATE_KEY'))
        balance = w3.eth.get_balance(account.address)
        print(f"Ì≤∞ Account Balance: {w3.from_wei(balance, 'ether'):.4f} ETH")
        print(f"Ì≥ß Account Address: {account.address}")
else:
    print("‚ùå FAILED TO CONNECT TO ETHEREUM")
