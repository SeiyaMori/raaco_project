# main.py

from http.server import BaseHTTPRequestHandler, HTTPServer
from routes import Mapper

hostName = "localhost"
serverPort = 8080


class Router:
    """Hold URL routing mapping information."""
    router_map = Mapper()
    router_map.connect("/c/{action}/{height}", controller="error")

    @classmethod
    def match(cls, request_path):
        """Match request path to an existing mapping."""
        return cls.router_map.match(cls.clean_path(request_path))

    @classmethod
    def clean_path(cls, request_path):
        """Clean up the url path."""

        # Remove last "/" if exists
        if request_path[-1] == "/":
            return request_path[:-1]
        return request_path


class BasicController:
    """Base class for controllers."""

    def __init__(self, server):
        """Initialise instance."""
        self.server = server
        pass
    
    def execute(self):
        """Execute controller actions."""
        
        # Send response ----
        self.server.send_response(200)
        self.server.send_header("Content-type", "text/html")
        self.server.end_headers()
        self.server.send_html_message("Controller")
        


class MyServer(BaseHTTPRequestHandler):
    """Main server class."""


    # GET
    def do_GET(self):
        router_result = Router.match(self.path)
        print(router_result)

        # Create a new controller
        c = BasicController(self)

        # Execute controller
        c.execute()

        

    # POST


    # Other http methods ----

    def send_html_message(self, message):
        self.wfile.write(bytes("<html><head><title>Raaco Project</title></head>", "utf-8"))
        self.wfile.write(bytes(f"<p>Request: {self.path}</p>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes(f"<p>Message: {message}</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
