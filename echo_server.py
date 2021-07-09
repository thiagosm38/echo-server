import socket
import threading
import logging
import argparse

def on_new_connection(client):
    while True:
        data = client.recv(2048)

        if data:
            data = data.decode('utf-8')
            logging.info(f'Dado recebido do cliente: {data}')
            command = data.split(' ', 1);

            if command[0] == 'echo':
                client.send(command[1].encode('utf-8'))

            elif data == 'quit':
                break

            else:
                client.send("Formato de mensagem invalido".encode('utf-8'))

    client.close()
        

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

parser = argparse.ArgumentParser(description = "Simple echo server")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = "localhost")
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 10100)
args = parser.parse_args()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    server_socket.bind((args.host, args.port))
    server_socket.listen(50)
    logging.info(f'Escutando no endereço: {args.host}:{args.port}')

except Exception as e:
    raise SystemExit(f'Falha ao tentar escutar no endereço: {args.host}:{args.port}\n {e}')
    

while True:
    try:
        client, adress = server_socket.accept()
        threading._start_new_thread(on_new_connection, (client,))
        logging.info(f"Novo cliente: {adress}")

    except Exception as e:
        print(f"Erro: {e}")

server_socket.close()