#/usr/bin/python3

import socket

recv_ip"127.0.0.1"

recv_port=4444 # 0-1024 --you can check free UDP port netstat -nulp

#creating udp socket
#		ip type v4 , udp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 4 > 2:
	msg=raw_input("please enter your message ")
	#sending data to receiver
	s.sendto(msg,(recv_ip,recv_port))




