import bc_server
import socketserver

PORT = 8080
Handler = bc_server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    ("serving at port", PORT)
    httpd.serve_forever()


