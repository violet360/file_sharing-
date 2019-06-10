import socket
import os
import sys
from _thread import start_new_thread

'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
clientsocket, address = s.accept()

while True:
	msg = clientsocket.recv(1024)
	msg = msg.decode('utf-8')
	print(address,">>",msg)
	msg2 = input("server>>")
	clientsocket.send(bytes(msg2,'utf-8'))
'''

header = 10


'''
def receive(sock):
	f_len = sock.recv(header)
	f_len = int(f_len)
	f_name = sock.recv(f_len)
	f_name = f_name.decode('utf-8')
	return f_name


'''

def send_stuff(clientsocket, address):
	f_name = clientsocket.recv(1024).decode('utf-8')
	if os.path.isfile(f_name):
		clientsocket.send(bytes("exists"+str(os.path.getsize(f_name)),'utf-8'))
		u_res = clientsocket.recv(1024).decode('utf-8')
		if u_res[:2] == 'OK':
			with open(f_name, 'rb') as f:
				# bytestosend = f.read(1024)
				# clientsocket.send(bytestosend)
				while True:
					bytestosend = f.read(1024)
					clientsocket.send(bytestosend)
					if sys.getsizeof(bytestosend) < 1024:
						break
					# print(sys.getsizeof(bytestosend))
					
				# while var!=int(int(os.path.getsize(f_name))//1024):
				# 	print(var)
				# 	bytestosend = f.read(1024)
				# 	clientsocket.send(bytestosend)
				# 	var+=1
				# print("____________________________")

	else:
		clientsocket.send(bytes("err",'utf-8'))

	clientsocket.close()




def Main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((socket.gethostname(), 1234))
	s.listen(5)
	while True:
		# print("___%$^#%&^%#^&%^&%^__________")
		clientsocket, address = s.accept()
		print(f"connection with {address} has been established \n")
		start_new_thread(send_stuff, (clientsocket,address,))

	s.close()


if __name__ == '__main__':
	Main()

