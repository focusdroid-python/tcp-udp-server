### socket发送数据和接收数据过程
> 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
> 2. 使用套接字收发数据
    udp_socket.sendto('xxxx', (ip, 端口))
    udp_socket.recvfrom(1024)
> 3. 关闭套接字
    udp_socket.close()