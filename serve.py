#!/usr/bin/env python3
"""
Simple HTTP server for serving the slides locally.
"""
import os
import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8000

def serve_slides():
    """Start a local server to serve the slides."""
    # Change to the site directory
    site_dir = Path(__file__).parent / "site"
    os.chdir(site_dir)
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving slides at http://localhost:{PORT}")
        webbrowser.open(f"http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    serve_slides()
