# www.theforage.com - Telstra Cyber Task 3
# Firewall Server Handler


from http.server import BaseHTTPRequestHandler, HTTPServer
import json

host = "localhost"
port = 8000

#########
#List of blocked Ip address
blocked_ips = ["attacker.ip.address.network1", "attacker.ip.address.network2", "attacker.ip.address.network3", "attacker.ip.address.network4"]

# Handle the response here 
def block_request(self):
    print("Blocking request")
    print(f"Blocking request from {self.client_address[0]}")
    self.send_response(403)  # Forbidden response
    self.send_header("content-type", "application/json")
    self.end_headers()
    response = {"message": "Request blocked by firewall"}
    self.wfile.write(json.dumps(response).encode())


def handle_request(self):
    self.send_response(200)
    self.send_header("content-type", "application/json")
    self.end_headers()
    response = {"message": "Request handled successfully"}
    self.wfile.write(json.dumps(response).encode())

#########

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.client_address[0] in blocked_ips:
            block_request(self)
        else:
            handle_request(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Get the size of data
        post_data = self.rfile.read(content_length)  # Read the posted data
        try:
            # Try to parse incoming JSON data (if required for blocking criteria)
            data = json.loads(post_data)
        except json.JSONDecodeError:
            data = {}

        if self.client_address[0] in blocked_ips:
            block_request(self)
        else:
            # You could add additional checks here based on the request data
            handle_request(self)


if __name__ == "__main__":        
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    print("[+] HTTP Web Server running on: %s:%s" % (host, port))


    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


    server.server_close()
    print("[+] Server terminated. Exiting...")
    exit(0)