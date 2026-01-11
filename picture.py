import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

class CamHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/jpeg')
        self.end_headers()
        # This grabs one high-quality 1440p frame and sends it to the browser
        cmd = ["rpicam-still", "-e", "jpg", "-n", "-t", "10", "--width", "2560", "--height", "1440", "--quality", "95", "-o", "-"]
        self.wfile.write(subprocess.check_output(cmd))

httpd = HTTPServer(('0.0.0.0', 8080), CamHandler)
httpd.serve_forever()
