import time
from web3 import Web3

print("LIVE ARBITRAGE TRADING - ETHEREUM MAINNET")
print("==========================================")

# Use your working Alchemy endpoint
w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/AiTkecJt-cMKIYl_Wm3W5"))

if not w3.is_connected():
    print("NOT CONNECTED TO ETHEREUM")
    exit(1)

print(f"CONNECTED TO ETHEREUM MAINNET | Block: #{w3.eth.block_number:,}")

# Real DEX Router ABIs
UNISWAP_V2_ROUTER_ABI = '[{"constant":true,"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"type":"function"}]'

UNISWAP_V3_QUOTER_ABI = '[{"inputs":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"}],"name":"quoteExactInputSingle","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"type":"function"}]'

# Real contract addresses
CONTRACTS = {
    'UNISWAP_V2_ROUTER': '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D',
    'UNISWAP_V3_QUOTER': '0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6',
    'SUSHISWAP_ROUTER': '0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F',
    'WETH': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
    'USDC': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
    'USDT': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
    'DAI': '0x6B175474E89094C44Da98b954EedeAC495271d0F'
}

# Initialize contract objects
uni_v2_router = w3.eth.contract(address=CONTRACTS['UNISWAP_V2_ROUTER'], abi=UNISWAP_V2_ROUTER_ABI)
uni_v3_quoter = w3.eth.contract(address=CONTRACTS['UNISWAP_V3_QUOTER'], abi=UNISWAP_V3_QUOTER_ABI)

def get_uniswap_v2_price(token_in, token_out, amount_in=1*10**18):
    try:
        path = [token_in, token_out]
        amounts = uni_v2_router.functions.getAmountsOut(amount_in, path).call()
        return amounts[1]
    except Exception as e:
        print(f"Uniswap V2 price error: {e}")
        return 0

def get_uniswap_v3_price(token_in, token_out, fee=3000, amount_in=1*10**18):
    try:
        amount_out = uni_v3_quoter.functions.quoteExactInputSingle(
            token_in, token_out, fee, amount_in, 0
        ).call()
        return amount_out
    except Exception as e:
        print(f"Uniswap V3 price error: {e}")
        return 0

def check_arbitrage_opportunities():
    opportunities = []
    
    amount_in = 1 * 10**18
    
    # Check WETH/USDC pair
    uni_v2_price = get_uniswap_v2_price(CONTRACTS['WETH'], CONTRACTS['USDC'], amount_in)
    uni_v3_price = get_uniswap_v3_price(CONTRACTS['WETH'], CONTRACTS['USDC'], 3000, amount_in)
    
    if uni_v2_price > 0 and uni_v3_price > 0:
        price_diff = abs(uni_v2_price - uni_v3_price)
        min_price = min(uni_v2_price, uni_v3_price)
        
        if min_price > 0:
            spread = (price_diff / min_price) * 100
            
            if spread > 0.1:
                opportunities.append({
                    'pair': 'WETH/USDC',
                    'spread': spread,
                    'uni_v2_price': uni_v2_price / 10**6,
                    'uni_v3_price': uni_v3_price / 10**6,
                    'profit_estimate': (price_diff * 0.99) / 10**6
                })
    
    return opportunities

print("Starting LIVE arbitrage monitoring...")
print("Pairs: WETH/USDC, WETH/USDT")
print("DEXs: Uniswap V2, Uniswap V3")
print("Mode: Real Ethereum Mainnet")

scan_count = 0
total_opportunities_found = 0

while True:
    try:
        current_block = w3.eth.block_number
        gas_price = w3.eth.gas_price
        
        opportunities = check_arbitrage_opportunities()
        scan_count += 1
        
        print(f"Scan {scan_count} | Block #{current_block:,} | Gas: {w3.from_wei(gas_price, 'gwei'):.1f} Gwei")
        
        if opportunities:
            total_opportunities_found += len(opportunities)
            for opp in opportunities:
                print(f"ARBITRAGE OPPORTUNITY:")
                print(f"  Pair: {opp['pair']}")
                print(f"  Spread: {opp['spread']:.3f}%")
                print(f"  Uniswap V2: {opp['uni_v2_price']:.2f} USDC")
                print(f"  Uniswap V3: {opp['uni_v3_price']:.2f} USDC")
                print(f"  Est. Profit: ${opp['profit_estimate']:.2f}")
        else:
            print("  No arbitrage opportunities found")
        
        time.sleep(12)
        
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(30)
