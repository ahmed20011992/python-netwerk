# import socket


# def simple_TCP_server(port=8080):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind(('localhost', port))
#     # sock.connect(('localhost', port))
#     sock.listen(1)
#     print(f"Server listening on port {port}...")

#     while True:
#         (sockC, addr) = sock.accept()
#         print(f"connection from : {addr}")
#         # shut the connection down
#         while True:
#             data = sockC.recv(1024)
#             if not data:
#                 break
#             request_text = data.decode("ASCII")
#             print(f"Received request from client:\n{request_text}")

#         sockC.close()
#         print("Connection closed\n")
#         ## det som jag inte exakt fattat var jag printer client request on the comand line


# if __name__ == "__main__":
#     simple_TCP_server()
