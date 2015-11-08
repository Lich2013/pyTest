#!/usr/bin/env python
#coding:utf-8
#公钥私钥选取不够合理
import base64
class RSA:
    __en = []
    __de = ''
    def __init__(self, p, q, message):
        self.p = p
        self.q = q
        self.n = self.p * self.q
        self.z = (self.p - 1) * (self.q - 1)
        self.count()
        print("公钥: " + str(self.e) + " 私钥: " + str(self.d))
        self.message = self.strSplit(message)

    def encode(self):
        for x in self.message:
            self.__en.append((ord(x) ** self.e) % self.n)
        print(self.__en)

    def decode(self):
        if self.__en is not None:
          tmp = []
          for x in self.__en:
            tmp.append(chr((x ** self.d) % self.n))
        print(base64.decodestring(self.__de.join(tmp)))

    def count(self):
        i = 1
        while (1):
            if(i < 24):
                i += 1
            if(self.verifye(i) == 1):
                self.e = i
                break
            i += 1

        k = 1
        while(1):
            if((self.e * k - 1) % self.z == 0):
                self.d = k
                break
            k += 1

    def verifye(self, n):
        m = self.z
        while n:
            m, n = n, m % n
        return m

    def strSplit(self, str):
        str = base64.encodestring(str)
        return  str

rsa = RSA(2053, 2063, '12asdjkbfdsi')
rsa.encode()
rsa.decode()
