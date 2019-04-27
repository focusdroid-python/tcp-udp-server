import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        send_data = input('请输入您要发送的内容: ')

        udp_socket.sendto(send_data.encode('utf-8'), ('192.168.43.84', 8080))

    udp_socket.close()


if __name__ == '__main__':
    main()