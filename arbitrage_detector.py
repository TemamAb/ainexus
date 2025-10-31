class ArbitrageDetector:
    def find_triangular_opportunities(self):
        opportunities = []
        for token_pair in self.monitored_pairs:
            dex1_price = self.get_dex_price('uniswap', token_pair)
            dex2_price = self.get_dex_price('pancakeswap', token_pair)
            spread = abs(dex1_price - dex2_price) / min(dex1_price, dex2_price)
            if spread > 0.02:
                opportunities.append({
                    'pair': token_pair,
                    'spread': spread,
                    'estimated_profit': self.calculate_profit(spread)
                })
        return opportunities
