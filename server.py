from http.server import HTTPServer, BaseHTTPRequestHandler
import logging

# Configure logging
logging.basicConfig(filename='server.log', level=logging.INFO)

class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Log the request details
        logging.info(f"Request from {self.client_address} for {self.path}")

        # Respond to the request
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, world!")

if __name__ == "__main__":
    server_address = ('', 8080)  # Serve on port 8080
    httpd = HTTPServer(server_address, CustomHandler)
    print("Server started on port 8080...")
    httpd.serve_forever()

