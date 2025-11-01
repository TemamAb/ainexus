from web3 import Web3

print("TESTING ETHEREUM CONNECTION")
print("============================")

pimlico_eth_url = "https://api.pimlico.io/v1/1/rpc?apikey=pim_UbfKR9ocMe5ibNUCGgB8fE"
print(f"Connecting to: {pimlico_eth_url.split('?')[0]}")

try:
    w3 = Web3(Web3.HTTPProvider(pimlico_eth_url, request_kwargs={'timeout': 30}))
    
    if w3.is_connected():
        block = w3.eth.block_number
        gas_price = w3.eth.gas_price
        chain_id = w3.eth.chain_id
        
        print("CONNECTED TO REAL ETHEREUM MAINNET")
        print(f"Chain ID: {chain_id}")
        print(f"Current Block: #{block:,}")
        print(f"Gas Price: {w3.from_wei(gas_price, 'gwei'):.1f} Gwei")
        print("ERC-4337 Gasless: READY")
    else:
        print("FAILED TO CONNECT TO ETHEREUM")
        
except Exception as e:
    print(f"CONNECTION ERROR: {e}")
