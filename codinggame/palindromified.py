n=input()
r=n[::-1]
e=''
for i in range(len(n)):
 e+=n[i]+r[i]
print(e)



N=input()
J=''.join
print(J(map(J,zip(N,N[::-1]))))


a=input()
print(''.join(x+y for x,y in zip(a,a[::-1])))
