import socket

# UDP 클라이언트
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client_socket.sendto(b'Hello, UDP Server!', ('localhost', 9090))
data, addr = udp_client_socket.recvfrom(1024)
print(f"받은 데이터: {data} from {addr}")
udp_client_socket.close()