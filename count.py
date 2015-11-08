__author__ = 'Lich'
#tmp
p = 2053
q = 2063
z = (p-1)*(q-1)
n = 25
m = z

while n:
        m, n = n, m % n
        print(m , n)
print(m)
exit(0)
i = 1
# (e * d + 1) % z == 0
print((25*169249)%((p-1)*(q-1)))
while (1):
    if(i > z/2):
        break
    # if i *  % i == 1:
        print(i)
        print(z / i)
        print(' ')
    i += 1
