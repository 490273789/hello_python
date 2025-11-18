import socket

# 创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sk.bind(("127.0.0.1", 8888))

# 循环
while True:
    recv_data, recv_info = sk.recvfrom(1024)
    print(f"recv_data: {recv_data.decode('utf-8')}; recv_info: {recv_info}")
    sk.sendto("Hello".encode("utf-8"), recv_info)

socket.close()
