import socket

def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定一个本地信息
    localaddr = ("", 8888)
    udp_socket.bind(localaddr)

    # 3.接收数据
    recv_data = udp_socket.recvfrom(1024)

    # 存储接收的数据
    recv_msg = recv_data[0]
    # 存储发送方的地址信息
    send_addr = recv_data[1]

    print("%s:%s" % (str(send_addr[0]), recv_msg.decode('gbk')))


    # 4.打印收到的数据
    # print(recv_data)

    # 5.关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()