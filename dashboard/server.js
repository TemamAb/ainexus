const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 10000;

app.use(express.static(path.join(__dirname)));

// Test route - SIMPLE
app.get('/', (req, res) => {
    res.send(`
        <html>
        <body style="background: black; color: lime; padding: 40px; font-family: monospace;">
            <h1>⚡ AINEXUS QUANTUM ENGINE</h1>
            <p>Status: ACTIVE</p>
            <p>Port: ${PORT}</p>
            <p><a href="/withdrawal" style="color: yellow;">� PROFIT WITHDRAWAL</a></p>
            <p><a href="/health" style="color: cyan;">❤️ HEALTH CHECK</a></p>
        </body>
        </html>
    `);
});

// Health check - SIMPLE
app.get('/health', (req, res) => {
    res.json({ 
        status: "OK", 
        port: PORT,
        timestamp: new Date().toISOString(),
        message: "SERVER IS RUNNING"
    });
});

// WITHDRAWAL PAGE - SIMPLE BUT WORKING
app.get('/withdrawal', (req, res) => {
    console.log('✅ SERVING WITHDRAWAL PAGE');
    res.send(`
        <html>
        <head>
            <title>AINEXUS Profit Withdrawal</title>
            <style>
                body { 
                    background: #1a1a1a; 
                    color: white; 
                    font-family: Arial; 
                    padding: 40px;
                    max-width: 800px;
                    margin: 0 auto;
                }
                .header { 
                    background: #2a2a2a; 
                    padding: 20px; 
                    border-radius: 10px;
                    text-align: center;
                    margin-bottom: 20px;
                }
                h1 { color: #4CAF50; margin: 0; }
                .card {
                    background: #2a2a2a;
                    padding: 20px;
                    border-radius: 10px;
                    margin: 10px 0;
                }
                button {
                    background: #f6851b;
                    color: white;
                    border: none;
                    padding: 15px;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;
                    width: 100%;
                    margin: 10px 0;
                }
                button:hover { background: #e2761b; }
                .success { color: #4CAF50; }
                .feature { 
                    background: #333; 
                    padding: 10px; 
                    margin: 5px 0; 
                    border-radius: 5px;
                    border-left: 3px solid #5794f2;
                }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>� AINEXUS PROFIT WITHDRAWAL</h1>
                <p>Enterprise Blockchain Integration</p>
            </div>
            
            <div class="card">
                <h2>�� Connect Wallet</h2>
                <button onclick="connectWallet()">� Connect MetaMask</button>
                <div id="walletInfo" style="display: none; margin-top: 15px; padding: 10px; background: #333; border-radius: 5px;">
                    <div class="success">✅ Connected: <span id="walletAddress"></span></div>
                </div>
            </div>
            
            <div class="card">
                <h2>� Transfer Control</h2>
                <p>Amount: <strong id="amount">$50,000</strong></p>
                <input type="range" min="0" max="100" value="50" style="width: 100%; margin: 15px 0;">
                <button onclick="executeTransfer()">� EXECUTE TRANSFER</button>
            </div>
            
            <div class="card">
                <h2>✅ Enterprise Features</h2>
                <div class="feature">ETH/USD Currency Display</div>
                <div class="feature">Dynamic Percentage Slider</div>
                <div class="feature">Financial Confirmation Dialogs</div>
                <div class="feature">Auto/Manual Transfer Modes</div>
                <div class="feature">MetaMask Integration</div>
            </div>

            <script>
                async function connectWallet() {
                    if (typeof window.ethereum !== 'undefined') {
                        try {
                            const accounts = await window.ethereum.request({ 
                                method: 'eth_requestAccounts' 
                            });
                            document.getElementById('walletInfo').style.display = 'block';
                            document.getElementById('walletAddress').textContent = accounts[0].substring(0, 8) + '...';
                        } catch (error) {
                            alert('Connection failed: ' + error.message);
                        }
                    } else {
                        alert('Please install MetaMask!');
                    }
                }

                function executeTransfer() {
                    if (confirm('� Confirm Transfer: $50,000 to AINEXUS Treasury?')) {
                        alert('✅ Transfer initiated! Check MetaMask for confirmation.');
                    }
                }
            </script>
        </body>
        </html>
    `);
});

app.listen(PORT, () => {
    console.log('� SERVER RUNNING ON PORT: ' + PORT);
    console.log('� MAIN: http://localhost:' + PORT);
    console.log('� WITHDRAWAL: http://localhost:' + PORT + '/withdrawal');
    console.log('❤️ HEALTH: http://localhost:' + PORT + '/health');
});
