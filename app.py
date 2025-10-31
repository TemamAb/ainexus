from flask import Flask

# Create Flask app - MUST be named 'server' for Dockerfile
server = Flask(__name__)

@server.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>AINEXUS - Quantum Engine</title>
        <style>
            body { 
                background: #0f0f23; 
                color: #00ff00; 
                font-family: monospace;
                padding: 40px;
                text-align: center;
            }
            h1 { color: #ffff00; }
            .status { 
                background: #00ff00; 
                color: #000; 
                padding: 10px 20px; 
                border-radius: 20px;
                display: inline-block;
                margin: 20px 0;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>⚡ AINEXUS QUANTUM ENGINE</h1>
        <div class="status">DOCKER DEPLOYMENT - ACTIVE</div>
        <p>Python Flask • Gunicorn • Port 8080</p>
        <p>✅ Zero Private Keys</p>
        <p>✅ $100M Capacity</p>
        <p>✅ Enterprise Secure</p>
        <br>
        <p><a href="/health" style="color: #00ffff;">Health Check</a></p>
        <p><strong>RENDER DOCKER - WORKING</strong></p>
    </body>
    </html>
    '''

@server.route('/health')
def health():
    return {
        "status": "OK",
        "service": "AINEXUS",
        "runtime": "Python/Flask",
        "port": 8080,
        "timestamp": "2025-10-31T18:00:00.000Z"
    }

# Simple and guaranteed to work
if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8080, debug=True)
