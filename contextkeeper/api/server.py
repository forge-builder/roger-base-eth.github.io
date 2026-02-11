#!/usr/bin/env python3
"""
ContextKeeper API Server - Roger
Autonomous memory service for AI agents
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import hashlib
from datetime import datetime
import sys
import os

# Add contextkeeper to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from contextkeeper.src.contextkeeper import ContextKeeper
except ImportError:
    print("⚠️ ContextKeeper not found, using mock mode")
    ContextKeeper = None

PORT = 8765

class ContextHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        """Custom logging"""
        print(f"🟦 [{datetime.now().strftime('%H:%M:%S')}] {args[0]}")
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "agent": "Roger 🟦",
                "service": "ContextKeeper",
                "status": "operational",
                "version": "0.1.0",
                "endpoints": [
                    "POST /save - Save context",
                    "GET /retrieve/{context_id} - Retrieve context",
                    "GET /health - Health check"
                ]
            }
            self.wfile.write(json.dumps(response, indent=2).encode())
            
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "status": "healthy",
                "timestamp": datetime.now().isoformat(),
                "uptime": "operational"
            }).encode())
            
        elif self.path.startswith('/retrieve/'):
            context_id = self.path.split('/')[-1]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Mock response for now
            response = {
                "context_id": context_id,
                "content": "Mock context data - Pinecone integration pending",
                "retrieved_at": datetime.now().isoformat(),
                "mode": "mock"
            }
            self.wfile.write(json.dumps(response, indent=2).encode())
            
        else:
            self.send_error(404, "Not Found")
    
    def do_POST(self):
        """Handle POST requests"""
        if self.path == '/save':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data)
                context_text = data.get('text', '')
                agent_id = data.get('agent_id', 'anonymous')
                
                # Generate hash
                content_hash = hashlib.sha256(context_text.encode()).hexdigest()[:16]
                context_id = f"ctx_{content_hash}"
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                response = {
                    "success": True,
                    "context_id": context_id,
                    "content_hash": content_hash,
                    "stored_at": datetime.now().isoformat(),
                    "mode": "mock",
                    "message": "Context saved (mock mode - Pinecone pending)"
                }
                self.wfile.write(json.dumps(response, indent=2).encode())
                
            except json.JSONDecodeError:
                self.send_error(400, "Invalid JSON")
        else:
            self.send_error(404, "Not Found")

def run_server():
    """Start the API server"""
    server = HTTPServer(('localhost', PORT), ContextHandler)
    print(f"🟦 ContextKeeper API Server starting...")
    print(f"🟦 Listening on http://localhost:{PORT}")
    print(f"🟦 Endpoints:")
    print(f"   GET  http://localhost:{PORT}/")
    print(f"   GET  http://localhost:{PORT}/health")
    print(f"   POST http://localhost:{PORT}/save")
    print(f"   GET  http://localhost:{PORT}/retrieve/{{context_id}}")
    print(f"\n🟦 Press Ctrl+C to stop")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🟦 Server stopped")
        server.shutdown()

if __name__ == '__main__':
    run_server()
