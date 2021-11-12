import socket
import threading
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Запуск сервера...')
server.bind(('127.0.0.1',9090))
print('Начало прослушивания порта...')
server.listen(5)
msg = ''
def make_conn(conn):
	while True:
		print('Прием данных')
		data = conn.recv(1024)
		if not data:
			break
		msg = data.decode()
		print(msg)
		print('Отправка данных')
		conn.send(data.upper())
	print('Отключение клиента')
	conn.close()
	print('Соединение остановлено')
while True:
	conn, addr = server.accept()
	print(addr)
	t=threading.Thread(target=make_conn,args =(conn,))
	t.start()

server.close()
print('Сервер остановлен')
