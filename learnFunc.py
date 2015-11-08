#coding:utf-8

# RSA
import base64

p = 2053
q = 2063
n = p*q
z = (p - 1) * (p - 1)

e = 25  #encode 公钥

d = 169249  #decode 私钥
en = []
SecCode = []
de = []
DeMsg = []
TrsMsg = ['asdf4', 'f32sa我', 'sadfv', 'asdf']
print(base64.encodestring(TrsMsg[1]))
exit(0)
for x in range(4):
    en.append(base64.encodestring(TrsMsg[x]) ** e)
    SecCode.append(en[x] % n)
    print("origin:" + str(TrsMsg[x]) + " encode " + str(en[x]) + " Secencode " + str(SecCode[x]))

print('------------------')

for x in range(4):
    de.append(SecCode[x] ** d)
    DeMsg.append(de[x] % n)
    print("Secencode:" + str(SecCode[x]) + " origin " + str(DeMsg[x]))

print('success, let me have a seat!')


