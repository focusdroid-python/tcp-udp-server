import socket

def main():
    # 创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定端口
    tcp_server.bind(('', 8081))

    # 监听端口
    tcp_server.listen(128)

    # 循环为一个客户端服务
    while True:
        # 等待客户端链接 // 获取ip和内容  程序卡在这里等待客户端连接
        new_client_socket, client_addr = tcp_server.accept()

        # 一些链接信息
        print(new_client_socket)
        print('一个客户端连接成功')
        # 客户端的信息（ip, 端口）
        print(client_addr)

        # 循环为一个客户端服务多次
        while True:
            # 接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)

            print('客户端发送的内容：%s'% recv_data.decode('gbk'))
            # 只要
            if recv_data:
                new_client_socket.send('hahhahah'.encode('gbk'))
            else:
                new_client_socket.close()
                break
        print('一个客户端关闭了')
        new_client_socket.close()
    tcp_server.close()


if __name__ == '__main__':
    main()