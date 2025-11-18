import socket

# 创建socket对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口号
sk.bind(("0.0.0.0", 8995))
# 设置监听
sk.listen(5)
# 等待客户端连接
conn, addr = sk.accept()  # 等待链接，链接之前不会往下执行

print(f"客户端连接成功，地址：{addr}")


while True:
    # 接收数据
    data = conn.recv(1024)
    if not data:
        print("客户端已断开连接")
        break  # 如果没有数据，退出循环
    print(f"接收到数据：{data.decode('utf-8')}")

    # 发送数据
    send_data = input("请输入要发送的数据：")
    if send_data.lower() == "exit":
        print("退出连接")
        break  # 如果输入exit，退出循环
    conn.send(send_data.encode("utf-8"))
