# original code from Python in a Nutshell 2nd Ed. page 527
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8881))
print "Connected to server"
data = """A few lines of data
to test the operation
of both server and client."""
for line in data.splitlines( ):
	sock.sendall(line)
	print "Sent:", line
	response = sock.recv(8192)
	print "Received:", response
sock.close( )