# -*- coding:utf-8 -*-
import socket
import re
import hashlib
import random
HOST='114.215.113.76'
PORT=8899
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
s.connect((HOST,PORT))
while 1:

	try:
		data=s.recv(1024)
	except Exception, e:
		s.close()
		print 'restart'
		HOST='114.215.113.76'
		PORT=8899
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
		s.connect((HOST,PORT))
		continue

	if not data:
		s.close()
		print 'restart'
		HOST='114.215.113.76'
		PORT=8899
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
		s.connect((HOST,PORT))
		continue
	print data

	result = re.findall(r"with (.*)", data)
	ran = ''.join(random.sample('!@#$%^&*()_+-<>/,.{}[]\|;"\':~`QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456879',5))

	try:	
		if result[0]:
			str = hashlib.sha1(ran).hexdigest()
			print str[:16]
	except Exception, e:
		continue

	try:
		s.sendall(str[:16])
	except Exception, e:
		s.close()
		print 'restart'
		HOST='114.215.113.76'
		PORT=8899
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
		s.connect((HOST,PORT))
		continue

	

s.close()