__author__ = 'Lich'
p = 2053
q = 2063
z = p * q + 1
i = 1

while (1):
    if(i > z):
        break
    if z % i == 0:
        print(i)
        print(z / i)
        print(' ')
    i += 1
