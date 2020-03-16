a={}
for i in range(int(input())):
 c,p=input().split()
 a[c]=int(p)
s=input()
t=0
for k in a:
 if s in k:t+=a[k]
print(t)
