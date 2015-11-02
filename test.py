# -*- coding:utf-8 -*-
import socket
import re
import hashlib
str = {
'1':' _\n/ |\n| |\n| |\n|_|',
'2':' ____\n|___ \\\\\n  __) |\n / __/\n|_____|',
'3':' _____\n|___ /\n  |_ \\\n ___) |\n|____/',
'4':' _  _\n| || |\n| || |_\n|__   _|\n   |_|',
'5':' ____\n| ___|\n|___ \\\n ___) |\n|____/',
'6':"  __\n / /_\n| '_ \\\n| (_) |\n \\___/",
'7':' _____\n|___  |\n   / /\n  / /\n /_/',
'8':'  ___\n ( _ )\n / _ \\\n| (_) |\n \\___/',
'9':'  ___\n / _ \\\n| (_) |\n \\__, |\n   /_/',
'0':'  ___\n / _ \\\n| | | |\n| |_| |\n \\___/',
'a':'  __ _\n / _` |\n| (_| |\n \\__,_|',
'b':" _\n| |__\n| '_ \\\n| |_) |\n|_.__/",
'c':'  ___\n / __|\n| (__\n \\___|',
'd':'     _\n  __| |\n / _` |\n| (_| |\n \\__,_|',
'e':'  ___\n / _ \\\n|  __/\n \\___|',
'f':'  __\n / _|\n| |_\n|  _|\n|_|',
'g':'  __ _\n / _` |\n| (_| |\n \\__, |\n |___/',
'h':" _\n| |__\n| '_ \\\n| | | |\n|_| |_|",
'i':' _\n(_)\n| |\n| |\n|_|',
'j':'   _\n  (_)\n  | |\n  | |\n _/ |\n|__/',
'k':' _\n| | __\n| |/ /\n|   <\n|_|\\_\\',
'l':' _\n| |\n| |\n| |\n|_|',
'm':" _ __ ___\n| '_ ` _ \\\n| | | | | |\n|_| |_| |_|",
'n':" _ __\n| '_ \\\n| | | |\n|_| |_|",
'o':'  ___\n / _ \\\n| (_) |\n \\___/',
'p':" _ __\n| '_ \\\n| |_) |\n| .__/\n|_|",
'q':'  __ _\n / _` |\n| (_| |\n \\__, |\n    |_|',
'r':" _ __\n| '__|\n| |\n|_|",
's':' ___\n/ __|\n\\__ \\\n|___/',
't':' _\n| |_\n| __|\n| |_\n \\__|',
'u':' _   _\n| | | |\n| |_| |\n \\__,_|',
'v':'__   __\n\\ \\ / /\n \\ V /\n  \\_/',
'w':'__      __\n\\ \\ /\\ / /\n \\ V  V /\n  \\_/\\_/',
'x':'__  __\n\\ \\/ /\n >  <\n/_/\\_\\',
'y':' _   _\n| | | |\n| |_| |\n \\__, |\n |___/',
'z':' ____\n|_  /\n / /\n/___|'
}
i=1
HOST='114.215.113.76'
PORT=9900
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
s.connect((HOST,PORT))       #要连接的IP与端口
while 1:
	if i == 103:
		break
	data=s.recv(10240)     #把接收的数据定义为变量
	result = re.findall(r"\n(.*)\n", data, re.S)
	if data != ' ':
		print data
	if result:
		string = result[0]
		# cut = "Just follow me, i'll give you flag."
		if i == 1:
			i+=1
			continue
		else:
			i+=1
			print i
			#print string
			print result
			for x in str:
				if string == str[x]:
					print(string == str[x])
			# print string
			# print data
					s.sendall(x)
			continue
			# for i in range(100):
				#s.send(string)

	if data is None:
            break

s.close()   #关闭连接
