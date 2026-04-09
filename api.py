from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class APIHandler(BaseHTTPRequestHandler):
    blockchain = None

    def do_GET(self):
        if self.path == '/chain':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            chain_data = [block.to_dict() for block in self.blockchain.chain]
            self.wfile
