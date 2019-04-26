import socket

def main():
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	# 使用字符串发送数据要加 b
	udp_socket.sendto(b"Hello python",("192.168.1.109", 8080))

	udp_socket.sendto(b"hekkk", ("192.168.1.109", 8080))


	# 关闭套接字
	udp_socket.close()



if __name__ == '__main__':
	main() 
