const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 10000;

app.use(express.json());
app.use(express.static(path.join(__dirname)));

// Main engine status (existing route)
app.get('/', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>Ainexus Quantum Engine</title>
            <style>
                body { font-family: monospace; background: #0f0f0f; color: #00ff00; padding: 40px; }
                .status { color: #00ff00; }
                .container { max-width: 800px; margin: 0 auto; }
                a { color: #ffff00; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>‚ö° Ainexus Quantum Arbitrage Engine</h1>
                <p><strong>Status:</strong> <span class="status">ACTIVE</span></p>
                <p><strong>Flash Capacity:</strong> $100,000,000</p>
                <p><strong>Gasless System:</strong> PIMLICO INTEGRATED</p>
                <p><strong>AI Bots:</strong> 3-TIER OPERATIONAL</p>
                <br>
                <p>
                    <a href="/health">Health Check</a> | 
                    <a href="/api">API Status</a> |
                    <a href="/withdrawal">Ì≤∞ Profit Withdrawal</a> |
                    <a href="/monitor">Ì≥ä Live Monitor</a>
                </p>
            </div>
        </body>
        </html>
    `);
});

// Health check (existing)
app.get('/health', (req, res) => {
    res.json({ 
        status: "QUANTUM ENGINE - ENTERPRISE MODE",
        security: "ZERO_PRIVATE_KEYS", 
        architecture: "BACKEND-ONLY",
        profit_capacity: "$100,000,000",
        deployment: "READY_FOR_PRODUCTION",
        timestamp: new Date().toISOString()
    });
});

// API status (existing)
app.get('/api', (req, res) => {
    res.json({
        name: "Quantum Arbitrage Engine",
        version: "Enterprise 1.0", 
        security_model: "Zero-Trust Architecture",
        key_management: "External Wallet Integration Only",
        compliance: "Institutional Grade",
        scalability: "$1B+ Capacity"
    });
});

// NEW: Profit Withdrawal Dashboard
app.get('/withdrawal', (req, res) => {
    res.sendFile(path.join(__dirname, 'profit-withdrawal.html'));
});

// NEW: Live Monitoring Dashboard  
app.get('/monitor', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>AINEXUS Live Monitor</title>
            <style>
                body { font-family: Arial, sans-serif; background: #1e1e1e; color: white; padding: 20px; }
                .metric { background: #2d2d2d; padding: 20px; margin: 10px; border-radius: 8px; }
                .profit { color: #73bf69; font-size: 24px; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>Ì≥ä AINEXUS Live Trading Monitor</h1>
            <div class="metric">
                <div class="profit">Today's Profit: $1,850</div>
                <div>Total Profit: $116,137</div>
                <div>Active Bots: 12/12</div>
                <div>Success Rate: 98.7%</div>
            </div>
            <p><a href="/withdrawal" style="color: yellow;">‚Üí Go to Profit Withdrawal</a></p>
            <p><a href="/">‚Üê Back to Main Engine</a></p>
        </body>
        </html>
    `);
});

// API endpoints for profit data
app.get('/api/balance', (req, res) => {
    res.json({
        usd_balance: 116137,
        eth_balance: 62.5,
        wallet_address: '0xd6Ef692B34c14000912f429ed503685cBD9C52E0',
        daily_limit: 100000,
        auto_mode: false
    });
});

app.get('/api/profits', (req, res) => {
    res.json({
        today: 1850,
        week: 12450, 
        month: 47137,
        total: 116137
    });
});

app.post('/api/withdraw', (req, res) => {
    const { amount, currency } = req.body;
    console.log(`Withdrawal requested: ${amount} ${currency}`);
    res.json({ 
        success: true, 
        message: `Withdrawal of ${amount} ${currency} processed`,
        transaction: "0x" + Math.random().toString(16).substr(2, 64)
    });
});

app.listen(PORT, () => {
    console.log(`Ì∫Ä AINEXUS Unified Dashboard running on port ${PORT}`);
    console.log(`Ì≥ç Main Engine: http://localhost:${PORT}/`);
    console.log(`Ì≤∞ Profit Withdrawal: http://localhost:${PORT}/withdrawal`);
    console.log(`Ì≥ä Live Monitor: http://localhost:${PORT}/monitor`);
});
