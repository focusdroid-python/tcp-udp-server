import socket


def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本地信息
    tcp_server_socket.bind(('', 8090))

    # 3. 让默认套接字由主动变为被动(listen) //  负责等待新的客户端进行连接,
    tcp_server_socket.listen(128)

    print('-------------1----------------------')
    # 4. 等待客户端链接 // 产生新的套接字用来为客户端服务
    new_clicent_socket, client_addr = tcp_server_socket.accept()
    print('-------------2----------------------')

    print(client_addr)

    # 接受客户端发送过来的请求
    recv_data = new_clicent_socket.recv(1024)
    print(recv_data)

    send_datas = '王旭通过tcp服务器发送数据'

    new_clicent_socket.send(send_datas.encode('utf-8'))

    # 关闭套接字
    new_clicent_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()