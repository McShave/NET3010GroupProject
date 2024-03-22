
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging


def run (server_class = HTTPServer, handler_class = BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

