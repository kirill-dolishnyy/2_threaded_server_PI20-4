import threading
import socket

n = 2**16-1

def scan_port(port):
	sock = socket.socket()
	try:
		print(port)
		sock.connect(('127.0.0.1', port))
		print("Порт", port, "открыт")
		sock.close()
	except:
		pass

for i in range(n):
	thread = threading.Thread(target=scan_port, args=(i,))
	thread.start()
