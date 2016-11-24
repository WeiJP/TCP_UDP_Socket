# -*- coding:utf-8 -*-
# 2016-10-17 10:51
# auther:wjp
# TCP Socket 一个简单的客户端程序

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接：
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息：
print s.recv(1024)

for data in ['Wei Jinpeng', 'iOS 10', 'Siri']:
	# 发送数据：
	s.send(data)
	print s.recv(1024)
s.send('exit')
s.close()