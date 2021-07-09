# echo-server
Servidor de eco simples para aula de Redes de Computadores

# Requisitos
Os scripts foram desenvolvidos na versão do python 3.8.5, sendo assim é recomendado que você use um interpretador com a mesma versão ou superior

# Execução
Primeiro rode o script do servidor com o seguinte comando:
```
python3 echo_server.py
```
Por padrão o servidor irá escutar no endereço: localhost:10100, você pode indicar o endereço ip e a porta desejados utilizando as opções '--host' e '--port' respequitivamente.
```
python3 echo_server.py --host localhost --port 5532
```
Agora rode o script do cliente:
```
python3 echo_client.py
```
Novamente, o endereço do servidor ao qual o cliente irá se conectar é o mesmo: localhost:10100 e também pode ser alterado da mesma maneira:
```
python3 echo_client.py --host localhost --port 5532
```
Quando a conexão for estabelecida, basta utilizar um dos dois comando no lado do cliente:
```
echo [palavra a ser ecoada]
```
ou, para fechar o cliente e a conexão:
```
quit
```