# original code from Python in a Nutshell 2nd Ed. page 526

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8881))
sock.listen(5)

# loop waiting for connections
# terminate with Ctrl-Break on Win32, Ctrl-C on Unix
try:
	while True:
		newSocket, address = sock.accept( )
		print "Connected from", address
		while True:
			receivedData = newSocket.recv(8192)
			if not receivedData: break
			newSocket.sendall(receivedData)
		newSocket.close( )
		print "Disconnected from", address
finally:
	sock.close( )