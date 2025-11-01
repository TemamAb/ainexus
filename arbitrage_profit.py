import time
from web3 import Web3

print("REAL ARBITRAGE PROFIT DETECTION")
print("================================")

w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/AiTkecJt-cMKIYl_Wm3W5"))

if not w3.is_connected():
    print("NOT CONNECTED TO ETHEREUM")
    exit(1)

print(f"LIVE ON ETHEREUM MAINNET | Block: #{w3.eth.block_number:,}")

# Real DEX contracts
CONTRACTS = {
    'UNISWAP_V2': '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D',
    'SUSHISWAP': '0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F',
    'WETH': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
    'USDC': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
    'USDT': '0xdAC17F958D2ee523a2206206994597C13D831ec7'
}

# DEX Router ABIs
UNISWAP_V2_ABI = '[{"constant":true,"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"type":"function"}]'
SUSHISWAP_ABI = '[{"constant":true,"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"type":"function"}]'

uni_v2 = w3.eth.contract(address=CONTRACTS['UNISWAP_V2'], abi=UNISWAP_V2_ABI)
sushiswap = w3.eth.contract(address=CONTRACTS['SUSHISWAP'], abi=SUSHISWAP_ABI)

def get_dex_prices(router, router_name, amount_in=1*10**18):
    prices = {}
    
    try:
        # WETH to USDC
        path_weth_usdc = [CONTRACTS['WETH'], CONTRACTS['USDC']]
        amounts_usdc = router.functions.getAmountsOut(amount_in, path_weth_usdc).call()
        prices['WETH/USDC'] = amounts_usdc[1] / 10**6
        
        # WETH to USDT
        path_weth_usdt = [CONTRACTS['WETH'], CONTRACTS['USDT']]
        amounts_usdt = router.functions.getAmountsOut(amount_in, path_weth_usdt).call()
        prices['WETH/USDT'] = amounts_usdt[1] / 10**6
        
    except Exception as e:
        print(f"{router_name} price error: {e}")
    
    return prices

def calculate_arbitrage(dex1_prices, dex2_prices, dex1_name, dex2_name):
    opportunities = []
    
    for pair in ['WETH/USDC', 'WETH/USDT']:
        if pair in dex1_prices and pair in dex2_prices:
            price1 = dex1_prices[pair]
            price2 = dex2_prices[pair]
            
            if price1 > 0 and price2 > 0:
                spread = abs(price1 - price2)
                spread_percent = (spread / min(price1, price2)) * 100
                
                # Calculate potential profit for 1 ETH trade (after 0.3% fees)
                if price1 > price2:
                    buy_dex = dex2_name
                    sell_dex = dex1_name
                    profit = (price1 - price2) * 0.997  # After fees
                else:
                    buy_dex = dex1_name
                    sell_dex = dex2_name
                    profit = (price2 - price1) * 0.997  # After fees
                
                if spread_percent > 0.01:  # 0.01% minimum spread
                    opportunities.append({
                        'pair': pair,
                        'buy_dex': buy_dex,
                        'sell_dex': sell_dex,
                        'spread_percent': spread_percent,
                        'profit_per_eth': profit,
                        'dex1_price': price1,
                        'dex2_price': price2
                    })
    
    return opportunities

print("STARTING REAL ARBITRAGE DETECTION")
print("Comparing: Uniswap V2 vs Sushiswap")
print("Trade Size: 1 ETH basis")
print("Minimum Spread: 0.01%")

scan_count = 0
total_opportunities = 0

while True:
    try:
        current_block = w3.eth.block_number
        gas_price = w3.eth.gas_price
        
        scan_count += 1
        
        print(f"SCAN {scan_count} | Block #{current_block:,} | Gas: {w3.from_wei(gas_price, 'gwei'):.1f} Gwei")
        
        # Get REAL prices from both DEXs
        uni_prices = get_dex_prices(uni_v2, "UNISWAP_V2")
        sushi_prices = get_dex_prices(sushiswap, "SUSHISWAP")
        
        if uni_prices and sushi_prices:
            print("REAL DEX PRICES:")
            print(f"  Uniswap V2 - WETH/USDC: ${uni_prices.get('WETH/USDC', 0):.2f}")
            print(f"  Sushiswap  - WETH/USDC: ${sushi_prices.get('WETH/USDC', 0):.2f}")
            print(f"  Uniswap V2 - WETH/USDT: ${uni_prices.get('WETH/USDT', 0):.2f}")
            print(f"  Sushiswap  - WETH/USDT: ${sushi_prices.get('WETH/USDT', 0):.2f}")
            
            # Find arbitrage opportunities
            opportunities = calculate_arbitrage(uni_prices, sushi_prices, "UNISWAP_V2", "SUSHISWAP")
            
            if opportunities:
                total_opportunities += len(opportunities)
                print(f"REAL ARBITRAGE OPPORTUNITIES FOUND: {len(opportunities)}")
                
                for opp in opportunities:
                    print(f"OPPORTUNITY:")
                    print(f"  Pair: {opp['pair']}")
                    print(f"  Action: Buy on {opp['buy_dex']} -> Sell on {opp['sell_dex']}")
                    print(f"  Spread: {opp['spread_percent']:.4f}%")
                    print(f"  Profit per 1 ETH: ${opp['profit_per_eth']:.2f}")
                    print(f"  Gas Cost: {w3.from_wei(gas_price * 200000, 'ether'):.6f} ETH")
            else:
                print("No arbitrage opportunities above 0.01% spread")
        else:
            print("Waiting for DEX price data...")
        
        print("---")
        time.sleep(12)
        
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(30)
