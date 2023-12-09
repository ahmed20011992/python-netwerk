import socket
import select
port = 60003
sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(("", port))
sockL.listen(1)
listOfSockets = [sockL]
print("Listening on port {}".format(port))
while True:
    # blocks the program until any of the sockets in the list has incoming data
    # tup = select.select(listOfSockets, [], [])
    # sock = tup[0][0]

    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]

    if sock == sockL:
        (sockClient, addr) = sockL.accept()
        print("New client connected from {}".format(addr))
        for cSoketX in listOfSockets[1:]:
            cSoketX.sendall(
                bytearray(f"{sockClient.getpeername()} entered the chatroom.".encode("ascii")))
        listOfSockets.append(sockClient)
        # sock.getpeername()  # ???
        # listOfSockets += [sockClient]

        # [IP-addr:60003] (connected)# it should send this message
        # Notify all other clients about the new client

    # TODO: A new clients connects.
    # call (sockClient, addr) = sockL.accept() and take care of the new client
    # add the new socket to listOfSockets
    # notify all other clients about the new client
    else:
        # Connected clients send data or are disconnecting...
        # print("client is offline!")
        data = sock.recv(2048)
        client_name = sock.getpeername()
        if not data:

            # A client disconnects
            if not data:
                for client_socket in listOfSockets:
                    if client_socket != sockL:
                        client_socket.sendall(bytearray(f"{client_name} is disconnected.".encode(
                            "ascii")))  # notify all other clients about the disconnected client
                # close the socket object and remove from listOfSockets
                sock.close()
                # or remove which is more correct?! ASK!!!!!!!!
                # det merea rätt och använda remov istället
                listOfSockets.pop(sock)

        #     # TODO: A client disconnects
        #     # close the socket object and remove from listOfSockets
        #     addr = sock.getpeername()
        #     print("Client disconnected from {}".format(addr))
        #     sock.close()
        #     listOfSockets.remove(sock)
        #     # sockL.close()
        #     # listOfSockets.pop()
        # # notify all other clients about the disconnected client
        #     message = "[{}:{}] (disconnected)".format(*addr)
        #     for client in listOfSockets:
        #         if client != sock:
        #             try:
        #                 client.sendall(message.encode())
        #             except OSError as e:
        #                 # Handle the exception (e.g., client disconnected)
        #                 print(f"Error sending message to client: {e}")

        else:
            message = data.decode("ascii")
            print(message)
            for client_socket in listOfSockets:
                if client_socket != sockL:
                    # send the data to all client
                    client_socket.sendall(
                        bytearray(f"{client_name}: {message}", "ascii"))

        # TODO: A client sends a message
        # data is a message from a client
        # send the data to all clients
        # Send the data to all clients
