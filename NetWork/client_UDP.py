# -*- coding:utf-8 -*-
# 2016-10-17 15:40
# auther:wjp
# UDP Socket 一个简单的客户端程序

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in ['Wei Jinpeng', 'iOS 10', 'Siri']:
	# 发送数据：
	s.sendto(data, ('127.0.0.1', 9999))
	print s.recv(1024)

s.close()