n=input()
x=input()
r=''
for i in range(len(n)):
 if n[i]=='1' and x[i]=='1':r+='1'
 else:r+='0'
print(r)
