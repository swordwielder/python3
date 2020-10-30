s=input().split()
t=0
for i in s:
 if i=='inc':t+=1
 if i=='dec':t-=1
 if i=='half':t/=2
 if i=='double':t*=2
 if i=='print':print(int(t),end='')
 if i=='exit':exit()
