import socket
import argparse

parser = argparse.ArgumentParser(description = "Simple echo client")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = "localhost")
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 10100)
args = parser.parse_args()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f'Conectado no servidor: {args.host}:{args.port}')

try:
    client_socket.connect((args.host, args.port))

    msg = input()

    while True:
        client_socket.sendall(msg.encode('utf-8'))
        data = client_socket.recv(2048)
        print(data.decode('utf-8'))
        if msg == 'quit':
            break
        msg = input()

except socket.gaierror as e:
    print(f'Erro no socket: {str(e)}')

except Exception as e:
    print(e)

finally:
    client_socket.close()
