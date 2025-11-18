import socket


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sever_IP = "127.0.0.1"
sever_port = 8888

while True:
    client.sendto(input("输入").encode("utf-8"), (sever_IP, sever_port))
    recv_data, recv_info = client.recvfrom(1024)
    print(f"from serve: {recv_data.decode('utf-8')}")

socket.close()
