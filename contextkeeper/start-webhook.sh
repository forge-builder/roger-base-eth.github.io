#!/bin/bash
# ContextKeeper Webhook Endpoint
# Einfacher HTTP Endpoint zum Empfangen von Context-Daten

echo "ContextKeeper v0.1 Starting..."
echo "Port: 8080"
echo ""
echo "Waiting for context data..."

# Starte einfachen Python HTTP Server
python3 << 'PYEOF'
import http.server
import socketserver
import json
import os

PORT = 8080
CONTEXT_DIR = "/Users/roger.base.eth/.openclaw/workspace/contextkeeper/data"

class ContextHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/context':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            # Speichere Context
            timestamp = str(int(time.time()))
            filename = f"{CONTEXT_DIR}/context_{timestamp}.json"
            
            with open(filename, 'w') as f:
                f.write(post_data.decode('utf-8'))
            
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"status": "saved"}')
            print(f"✅ Context saved: {filename}")

os.makedirs(CONTEXT_DIR, exist_ok=True)

with socketserver.TCPServer(("", PORT), ContextHandler) as httpd:
    print(f"🟦 ContextKeeper listening on port {PORT}")
    httpd.serve_forever()
PYEOF
