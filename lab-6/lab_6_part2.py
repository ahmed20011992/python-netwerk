import socket


def generate_html_response(request):
    html_response = f"""
    <html>
    <head>
        <title>Your browser sent the following request</title>
    </head>
    <body>
        <h1>Your browser sent the following request:</h1>
        <pre>{request}</pre>
    </body>
    </html>
    """
    return html_response


def simple_TCP_server(port=8080):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    # sock.connect(('localhost', port))
    sock.listen(1)
    print(f"Server listening on port {port}...")

    while True:
        (sockC, addr) = sock.accept()
        print(f"connection from : {addr}")
        # shut the connection down

        data = sockC.recv(1024)
        if data:

            request_text = data.decode("ASCII")
            print(f"Received request from client:\n{request_text}")
            html_response = generate_html_response(request_text)

            sockC.sendall(bytearray("HTTP/1.1 200 OK\n", "ASCII"))
            sockC.sendall(
                bytearray("Content-Type: text/html; charset=utf-8\n", "ASCII"))
            sockC.sendall(bytearray("\n", "ASCII"))

            sockC.sendall(html_response.encode("ASCII"))

        sockC.close()
        print("Connection closed\n")


if __name__ == "__main__":
    simple_TCP_server()
