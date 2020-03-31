import socket

address_of_server = ('localhost', 8686)
while True:
    st = input('Введите данные о спортсмене: ')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(address_of_server)
    client.send(bytes(st, encoding='UTF-8'))
    client.close()
