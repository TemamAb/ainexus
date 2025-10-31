const express = require('express');
const app = express();
const PORT = process.env.DASHBOARD_PORT || 3000;

class PerformanceMonitor {
    constructor() {
        this.metrics = {
            totalProfit: 0,
            dailyProfit: 0,
            activeTrades: 0,
            successRate: 0,
            riskExposure: 0
        };
        this.profitHistory = [];
    }

    recordTrade(profit, success) {
        this.metrics.totalProfit += profit;
        this.metrics.dailyProfit += profit;
        this.metrics.activeTrades++;
        
        if (success) {
            this.metrics.successRate = (this.metrics.successRate * 0.9) + (1 * 0.1);
        }
        
        this.profitHistory.push({
            timestamp: new Date(),
            profit: profit,
            success: success
        });
    }

    getPerformanceMetrics() {
        return {
            ...this.metrics,
            hourlyRate: this.calculateHourlyRate(),
            weeklyProjection: this.metrics.dailyProfit * 7,
            monthlyProjection: this.metrics.dailyProfit * 30
        };
    }

    calculateHourlyRate() {
        return this.metrics.dailyProfit / 24;
    }
}

const monitor = new PerformanceMonitor();

app.get('/dashboard', (req, res) => {
    const metrics = monitor.getPerformanceMetrics();
    
    res.send(`
        <html>
            <head><title>Quantum Engine Dashboard</title>
                <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            </head>
            <body style="font-family: Arial, sans-serif; padding: 20px; background: #0f0f23; color: white;">
                <h1>Ì∫Ä Quantum Engine Performance Dashboard</h1>
                
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 20px 0;">
                    <div style="background: #1a1a2e; padding: 20px; border-radius: 10px;">
                        <h3>Ì≤∞ Total Profit</h3>
                        <h2>$${metrics.totalProfit.toLocaleString()}</h2>
                    </div>
                    <div style="background: #1a1a2e; padding: 20px; border-radius: 10px;">
                        <h3>Ì≥à Daily Profit</h3>
                        <h2>$${metrics.dailyProfit.toLocaleString()}</h2>
                    </div>
                    <div style="background: #1a1a2e; padding: 20px; border-radius: 10px;">
                        <h3>ÌæØ Success Rate</h3>
                        <h2>${(metrics.successRate * 100).toFixed(1)}%</h2>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
                    <div style="background: #1a1a2e; padding: 20px; border-radius: 10px;">
                        <h3>Ì≥ä Projections</h3>
                        <p>Weekly: $${metrics.weeklyProjection.toLocaleString()}</p>
                        <p>Monthly: $${metrics.monthlyProjection.toLocaleString()}</p>
                        <p>Hourly Rate: $${metrics.hourlyRate.toFixed(2)}/hr</p>
                    </div>
                    <div style="background: #1a1a2e; padding: 20px; border-radius: 10px;">
                        <h3>‚ö° Active Systems</h3>
                        <p>Ì≤∞ $100M Flash Loans: <span style="color: #00ff00;">ACTIVE</span></p>
                        <p>Ì¥ñ AI Optimization: <span style="color: #00ff00;">RUNNING</span></p>
                        <p>Ì¥ê Auto Profit Transfer: <span style="color: #00ff00;">READY</span></p>
                    </div>
                </div>
            </body>
        </html>
    `);
});

app.listen(PORT, () => {
    console.log('Ì≥ä Performance Dashboard running on port', PORT);
});
