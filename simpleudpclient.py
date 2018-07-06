import socket
udp_ip_address = "127.0.0.1"
udp_port_no = 6799
Message = "Hello World"
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(Message, (udp_ip_address, udp_port_no))
