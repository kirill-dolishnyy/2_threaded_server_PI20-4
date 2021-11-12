import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setblocking(1)
print('Соединение с сервером')
client.connect(('',9090))
msg =''
while msg != 'exit':
	msg = input('Enter your message \n')
	print('Отправка данных серверу')
	client.send(msg.encode())
	print('Прием данных от сервера')
	data = client.recv(1024)
	print(data)
client.close()


