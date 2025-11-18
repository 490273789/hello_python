import socket
import threading


def func(socket_client, client_info):
    try:
        while True:
            print("One Thread")
            data = socket_client.recv(1024)  # 在这里回等待监听
            if not data:
                break

            print(f"收到客户端（{client_info[0]}）信息:{data}")

            socket_client.send(input(f"To {client_info[0]}:").encode("utf-8"))
    except Exception as e:
        print(f"发生异常：{e}")
    finally:
        socket_client.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8889))
    server.listen(10)

    while True:
        print("Threading1")
        socket_client, client_info = server.accept()  # 在这里回等待，下一个链接
        print("Threading2")
        threading.Thread(target=func, args=(socket_client, client_info)).start()
        print("Threading3")


if __name__ == "__main__":
    main()
