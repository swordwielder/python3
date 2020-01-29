n,d,e=input().split()
n=int(n)
a=[]
b=0
c=0
for i in range(n):
    x=int(input())
    a.append(str(bin(x))[2:])
    c=len(str(bin(x))[2:])
    if b<c:
        b=c

for i in a:
    for j in i:
        if j=='0':
            print('B',end='')
        else:
            print('A',end='')
    print('')


str.zfill(min_length)


#Solution 1
n,p,q=input().split()
b=[bin(int(input()))[2:]for i in[1]*int(n)]
for i in[i.zfill(len(max(b,key=len)))for i in b]:print(''.join([q,p][j<'1']for j in i))


#Solution 2
n,q,w=input().split()
a=[bin(int(input()))[2:]for i in[0]*int(n)]
m=len(max(a,key=len))
print("\n".join(('0'*m+i)[-m:].replace('0',q).replace('1',w)for i in a))



#Solution 3
n,c,d=input().split()
a=[]
for i in range(int(n)):
 a.append(bin(int(input()))[2:])
for x in a:
 print(('0'*(len(max(a,key=len))-len(x))+x).replace('0',c).replace('1',d))
