# Importing the necessary modules
import socket

# Importing the request file from the controller folder
from celestis.controller import request as rq
import os
import json

# Get the method (GET or POST), route and headers from any request
def parse_request(request):
    if request == "":
        return "GET", "/", ""
    lines = request.split("\n")
    method, path, headers = lines[0].split(" ")
    headers = dict(line.split(": ") for line in lines[1:-2])
    return method, path, headers

# If form data has been sent, parse it
def parse_form(headers):
    if "Content-Type" not in headers:
        return {}
    if headers["Content-Type"] != "application/x-www-form-urlencoded":
        return {}
    return dict(pair.split("=") for pair in headers["Content-Length"].split("&"))

# Creating a socket connection to port 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 8080))
sock.listen(8080)

# Server running message
print("Celestis server is listening at port 8080...")

# Constantly check for a hit to the server
while True:
    conn, addr = sock.accept()
    request = conn.recv(1024).decode("utf-8")

    method, path, headers = parse_request(request)
    form = parse_form(headers)

    # Send a response that was retrieved from the handle_request function
    response = rq.handle_request(os.getcwd(), path, method, form)
    conn.sendall(response.encode("utf-8"))
    conn.close()