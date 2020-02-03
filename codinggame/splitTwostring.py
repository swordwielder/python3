s=input()
a=0
if len(s)%2==0:
    a=len(s)//2
else:
    a=len(s)//2+1
b=s[:a]
c=s[a:]
d=''
for i in range(len(b)):
    d+=b[i]
    if i<len(c):
        d+=c[i]
print(d)
