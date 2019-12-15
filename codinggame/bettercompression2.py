s=input()
c=1
a=''
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        a+=str(c)+s[i-1]
        c=1
    else:
        c+=1
print(a+str(c)+s[i])
    
