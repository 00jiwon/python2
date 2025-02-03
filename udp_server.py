import socket

# UDP 서버
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind(('localhost', 9090))
print("UDP 서버 시작. 데이터 수신 대기 중...")
data, addr = udp_server_socket.recvfrom(1024)
print(f"받은 데이터: {data} from {addr}")
udp_server_socket.sendto(b'Hello, UDP Client!', addr)
udp_server_socket.close()