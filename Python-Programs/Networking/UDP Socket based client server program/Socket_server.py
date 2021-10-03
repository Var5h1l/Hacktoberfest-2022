import socket

from socket_client import udp_host

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_port = 12345

sock.bind((udp_host,udp_port))
while True:
 print ("Waiting for client...")
data,addr = sock.recvfrom(1024)
