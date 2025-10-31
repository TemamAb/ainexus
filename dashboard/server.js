const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send(`
    <html>
      <head><title>Quantum Dashboard</title></head>
      <body>
        <h1>� Quantum Dashboard</h1>
        <p>Real-time monitoring: ACTIVE</p>
        <p>Profit Engine: RUNNING</p>
      </body>
    </html>
  `);
});

app.listen(PORT, () => {
  console.log('� Dashboard running on port', PORT);
});
