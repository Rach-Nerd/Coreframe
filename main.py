# WSGI protocol 
# This code starts a server that will listen for HTTP requests on port 8000. When the server receives a request, it will respond with "Hello World". The server will continue to listen for requests until the process is killed.

from wsgiref.simple_server import make_server
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)

def hello_world_app(environ, start_response):
    logging.debug('Handling request...')
    status = '200 OK'  # HTTP Status
    # HTTP Headers
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    # The returned object is going to be printed
# Serve until process is killed

httpd = make_server('', 8000, app)
logging.info("Serving on port 8000...")
# Serve until process is killed
httpd.serve_forever()
