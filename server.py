import socket

# TCP 소켓 서버 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))  # 'localhost'와 포트 8080에 바인딩
server_socket.listen(1)  # 클라이언트의 연결을 1개 대기
print("서버가 시작되었습니다. 연결 대기 중...")

# 클라이언트 연결 수락
conn, addr = server_socket.accept()
print(f"연결됨: {addr}")

# 클라이언트에 메시지 전송 및 데이터 수신
conn.sendall(b'Hello, Client!')  # 클라이언트에게 메시지 전송
data = conn.recv(1024)  # 클라이언트로부터 데이터 수신 (최대 1024 바이트)
print(f"받은 데이터: {data.decode()}")

# 연결 종료
conn.close()
server_socket.close()