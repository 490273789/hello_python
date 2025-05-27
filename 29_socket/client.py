import socket
# 创建socket对象
sk = socket.socket()
# 连接服务器
sk.connect(("127.0.0.1", 8995))

while True:
    send_data = input("请输入要发送的数据：")
    if send_data.lower() == 'exit':
        print("退出连接")
        break  # 如果输入exit，退出循环
    # 发送数据
    sk.send(send_data.encode('utf-8'))
    # conn.sendall(send_data.encode('utf-8'))
    # 接收数据
    data = sk.recv(1024)
    if not data:
        break  # 如果没有数据，退出循环
    print(f"接收到数据：{data.decode('utf-8')}")