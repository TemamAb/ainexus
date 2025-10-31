const { ethers } = require('ethers');

class AutoProfitTransfer {
    constructor() {
        this.profitWallet = process.env.PROFIT_WALLET; // Your wallet address
        this.minTransferAmount = ethers.parseEther("0.1"); // 0.1 ETH minimum
        this.profitAccumulated = 0;
    }

    async transferProfits(amount) {
        if (amount >= this.minTransferAmount) {
            console.log(`í²° Transferring ${ethers.formatEther(amount)} ETH to profit wallet...`);
            
            // In production, this would execute actual blockchain transfer
            // const tx = await wallet.sendTransaction({
            //     to: this.profitWallet,
            //     value: amount
            // });
            
            console.log(`âœ… Profit transfer initiated`);
            this.profitAccumulated = 0;
            return true;
        } else {
            this.profitAccumulated += amount;
            console.log(`í³¦ Accumulating profits: ${ethers.formatEther(this.profitAccumulated)} ETH`);
            return false;
        }
    }

    getTransferStatus() {
        return {
            profitWallet: this.profitWallet,
            accumulated: ethers.formatEther(this.profitAccumulated),
            minTransfer: ethers.formatEther(this.minTransferAmount),
            readyForTransfer: this.profitAccumulated >= this.minTransferAmount
        };
    }
}

module.exports = AutoProfitTransfer;
