import socket
import time

host = ('localhost', 8686)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(host)
server_socket.listen(10)
print('server is running, please, press ctrl+c to stop')

with open('log.txt', 'a') as file:
    file.write('-----server started at ' + time.strftime('%Y-%m-%d %H:%M:%S') + '-----' + '\n')
while True:
    connection, address = server_socket.accept()
    print("new connection from {address}".format(address=address))
    data = connection.recv(50).decode('UTF-8')
    number = data[0:4]
    track = data[5:7]
    hours = data[8:10]
    minutes = data[11:13]
    seconds = data[14:18]
    log_sec = data[14:20]
    group = data[21:23]
    if group == '00':
        print('Спортсмен, нагрудный номер ' + str(number) + ' прошёл отсечку ' + str(track) + ' в ' + str(
            hours) + ' часов ' + str(minutes) + ' минут ' + str(seconds) + ' секунд')

    with open('log.txt', 'a') as file:
        file.write('спортсмен, нагрудный номер ' + str(number) + ' прошёл отсечку ' + str(track) + ' в ' + str(
            hours) + ' часов ' + str(minutes) + ' минут ' + str(log_sec) + ' секунд, ' + 'группа: ' + str(group) + '\n')

    connection.close()
