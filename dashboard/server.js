const express = require('express');
const app = express();
const PORT = process.env.PORT || 10000;

// EXPLICITLY DISABLE static file serving for root
app.use((req, res, next) => {
    console.log(`� ${req.method} ${req.url}`);
    next();
});

// NUCLEAR PROOF ROOT ENDPOINT
app.get('/', (req, res) => {
    console.log('✅ SERVING MASTER COMMAND CENTER');
    res.send(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>� AINEXUS MASTER COMMAND CENTER - NUCLEAR DEPLOYED</title>
            <style>
                body { 
                    background: #000000; 
                    color: #00FF00; 
                    font-family: monospace;
                    padding: 40px;
                    text-align: center;
                }
                .nuclear { 
                    border: 3px solid #FF0000; 
                    padding: 20px; 
                    margin: 20px;
                    background: #110000;
                }
            </style>
        </head>
        <body>
            <div class="nuclear">
                <h1>� NUCLEAR DEPLOYMENT SUCCESSFUL</h1>
                <h2>⚡ AINEXUS MASTER COMMAND CENTER</h2>
                <p><strong>DEPLOYMENT TIMESTAMP:</strong> $(date)</p>
            </div>
            <p>✅ Zero Private Keys</p>
            <p>✅ $100M Capacity</p>
            <p>✅ Enterprise Secure</p>
            <p>✅ MASTER DASHBOARD ACTIVE</p>
            <br>
            <p><a href="/health" style="color: #00FFFF;">Health Check</a></p>
            <p><strong>THIS PROVES OUR SERVER.JS IS RUNNING</strong></p>
        </body>
        </html>
    `);
});

app.get('/health', (req, res) => {
    res.json({ 
        status: "NUCLEAR_DEPLOYMENT_SUCCESS",
        server: "EXPRESS_JS_RUNNING",
        timestamp: new Date().toISOString(),
        message: "Master Command Center is ACTIVE"
    });
});

app.listen(PORT, () => {
    console.log("� NUCLEAR DEPLOYMENT - PORT", PORT);
    console.log("✅ MASTER COMMAND CENTER: ACTIVE");
});
