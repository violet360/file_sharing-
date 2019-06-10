import socket
import os
import sys

header = 10
'''
def receive(sock):
	f_len = sock.recv(header)
	f_len = int(f_len)
	f_name = sock.recv(f_len)
	f_name = f_name.decode('utf-8')
	return f_name

'''


def d_file(s, filename):
	if filename != 'q':
		s.send(bytes(filename,'utf-8'))
		data = s.recv(1024).decode('utf-8')
		if data[:6]=="exists":
			filesize = int(data[6:])
			message = input("file exists, "+str(filesize)+"Bytes, download? (Y/N) -> ")
			if message == 'Y':
				s.send(bytes('OK', 'utf-8'))
				var =filename.split('.')
				filename1 = var[0]+'1.'+var[1]
				f = open(filename1, 'wb')

				while True:
					data = s.recv(1024)
					f.write(data)
					if sys.getsizeof(data)<1024:
						break
					# print(sys.getsizeof(data),"\n")
						
						
				# while it!= int(int(filesize)//1024)-1:
				# 	data = s.recv(1024) 
				# 	f.write(data)
				# 	it+=1
				# 	print(it, " ", int(int(filesize)//1024))

				print("download complete")


		else:
			print("file does not exist!")

	elif filename == 'q':
		s.close()




def Main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((socket.gethostname(), 1234))
	while True:
		x = input("filename? -> ")
		d_file(s,x)
	


if __name__ == '__main__':
	Main()


