# -*- coding:utf-8 -*-
# 2016-10-17 15:34
# auther:wjp
# UDP 一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))

print 'Bind UDP on 9999'
while True:
	data, addr = s.recvfrom(1024)
	print 'Received from %s:%s.' % addr
	s.sendto('Hello, %s!' % data, addr)
