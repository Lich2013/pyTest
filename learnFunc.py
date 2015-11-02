#coding:utf-8
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
TrsMsg = [12, 15, 22, 5]

for x in range(4):
    en.append(TrsMsg[x] ** e)
    SecCode.append(en[x] % n)
    print("origin:" + str(TrsMsg[x]) + " encode " + str(en[x]) + " Secencode " + str(SecCode[x]))

print('------------------')

for x in range(4):
    de.append(SecCode[x] ** d)
    DeMsg.append(de[x] % n)
    print("Secencode:" + str(SecCode[x]) + " origin " + str(DeMsg[x]))

print('success, let me have a seat!')