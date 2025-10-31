const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 10000;

// Serve static files from root
app.use(express.static(__dirname));

// All routes serve index.html (Single Page Application)
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
    console.log("� STATIC MASTER DASHBOARD - PORT", PORT);
    console.log("✅ Serving index.html for all routes");
    console.log("� Access: http://localhost:" + PORT);
});
