# -*- coding:utf-8 -*-
# 2016-10-17 10:34
# auther:wjp
# TCP Socket 一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。

import socket
import threading, time

def tcplink(sock, addr):
	print 'Acccept new connection from %s:%s...' %addr
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send('Hello, %s' % data)
	sock.close()
	print 'Connection from %s:%s closed.' % addr

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口：
s.bind(('127.0.0.1', 9999))

s.listen(5)
print 'Waiting for connection...'

# accept()会等待并返回一个客户端的连接:
while True:
	# 接受一个新连接：
	sock, addr = s.accept()
	# 创建新线程来处理TCP连接：
	t = threading.Thread(target = tcplink, args = (sock, addr))
	t.start()