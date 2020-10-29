input()
r=''
a=input().split()
for i in range(len(a)):
 r+=a[i]
 if i!=len(a)-1:r+=int(a[i])*'.'
print(r)
