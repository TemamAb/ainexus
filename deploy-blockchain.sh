#!/bin/bash

echo "=== AINEXUS BLOCKCHAIN DEPLOYMENT ==="
echo "Ì∫Ä Starting MetaMask Integration..."

# Kill any processes on port 10000
echo "Ìªë Clearing port 10000..."
npx kill-port 10000 2>/dev/null || true

# Update dashboard server with blockchain features
echo "Ì¥ó Updating server with blockchain integration..."
cat > dashboard/server.js << 'SERVER_EOF'
const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 10000;

app.use(express.json());
app.use(express.static(path.join(__dirname)));

// Main Engine
app.get('/', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html>
        <head><title>Ainexus Quantum Engine</title>
        <style>body { font-family: monospace; background: #0f0f0f; color: #00ff00; padding: 40px; }</style>
        </head>
        <body>
            <h1>‚ö° Ainexus Quantum Arbitrage Engine</h1>
            <p><strong>Status:</strong> ACTIVE</p>
            <p><strong>Blockchain:</strong> METAMASK INTEGRATION READY</p>
            <p><a href="/withdrawal">Ì≤∞ Profit Withdrawal</a></p>
        </body>
        </html>
    `);
});

// Profit Withdrawal Dashboard
app.get('/withdrawal', (req, res) => {
    res.sendFile(path.join(__dirname, 'profit-withdrawal-enhanced.html'));
});

app.listen(PORT, () => {
    console.log("Ì∫Ä AINEXUS Blockchain Server running on port", PORT);
});
SERVER_EOF

echo "‚úÖ Server updated"

# Start the server
echo "Ì∫Ä Starting server..."
cd dashboard
node server.js &

echo "Ìæâ Deployment complete!"
echo "Ìºê Access: http://localhost:10000/withdrawal"
echo "Ì≤° Connect MetaMask to test blockchain integration"
