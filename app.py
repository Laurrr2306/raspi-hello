from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"ia-l de jos :X 2")
        except Exception as e:
            print(f"Error handling GET request: {e}")

    def handle_one_request(self):
        try:
            super().handle_one_request()
        except Exception as e:
            print(f"Exception during request handling: {e}")

def run(server_class=HTTPServer, handler_class=HelloHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting server on port 8000...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Server stopped by user')
    except Exception as e:
        print(f"Server error: {e}")

if __name__ == '__main__':
    run()
