#sol 1
p = input()
while True:
    n = int(p[:4],2)
    s=""
    for i in range(n):
        s+=chr(int(p[4+i*8:12+i*8],2))
    print(end=s)
    p=p[15*8+4:]



#only working 50% for some reason 

p = input()
a=p[:4]
b=p[4:]
while len(b)>0:
    c=int(b[:8],2)
    print(chr(c),end='')
    b=b[8:]
