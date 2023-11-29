import socket


def serversideGetPlaySocket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Additional server-side socket setup can be added here
    server_socket.bind(('127.0.0.1', 60003))
    server_socket.listen(1)
    print('Server socket created')
    return server_socket


def clientsideGetPlaySocket(host):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Additional client-side socket setup can be added here
    client_socket.connect((host, 60003))
    print('Client socket created')
    return client_socket


def Win(my_move, op_move):
    if (my_move == 'S' and op_move == 'P'):
        return True
    if (my_move == 'R' and op_move == 'S'):
        return True
    if (my_move == 'P' and op_move == 'R'):
        return True
    return False


def main():
    ans = "?"
    while ans not in {"C", "S"}:
        ans = input("Do you want to be server (S) or client (C): ").upper()

    if ans == "S":
        sock = serversideGetPlaySocket()
        (sock, addr) = sock.accept()
       # sock: Represents the communication channel with the connected client.
       # addr: Represents the address (IP address and port number) of the connected client.
       # Ask teacher why this method give these varibles into a Tuble not another thing like list?!!
        print(f"connection from {addr}")

    else:
        host = input("Enter the server's name or IP: ")
        sock = clientsideGetPlaySocket(host)

    my_score = 0
    op_score = 0

    while (my_score < 10 and op_score < 10):
        x = input(f"({my_score},{op_score}) your move :").upper()
        while x not in {'S', 'R', 'P'}:
            x = input('Enter one value of S, C , P  Plase!')
        # tack my move and sen it to the opponent
        sock.sendall(bytearray(x, 'ascii'))
        data = sock.recv(1024)
        if not data:
            print('opponent is offline!')
        # print('resived :', data.decode('ascii'))
        else:
            # här vi omvanlade bytes(oppoenet move) som kom till oss till string
            y = data.decode('ascii')
            print(f"opponents move:{y}")
            if (y != x):  # om de är lika varandra
                if (Win(x, y)):
                    my_score += 1
                else:
                    op_score += 1
            else:
                print('you have the same move!')
    sock.close()


if __name__ == "__main__":
    main()
