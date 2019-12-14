s=[*input()][::-1]
print(*[s.pop().lower()if x=='x'else(s.pop().upper()if x=='X' else x)for x in input()],sep="")


s=input()
i,r=0,""
for c in input():
    if c=='x':r+=s[i].lower()
    elif c=='X':r+=s[i].upper()
    else:i,r=i-1,r+c
    i+=1
print(r)


s=input()
f=input()
e=''
c=0
for i in range(len(f)):
    if f[i]=='X':e+=s[i-c].upper()
    elif f[i]=='x':e+=s[i-c].lower()
    else:
        e+=f[i]
        c+=1
print(e)



s=input()
f=input()
a=''
j=0
for i in f:
    if i.isalpha() and i.islower():
        a+=s[j].lower()
        j+=1
    elif i.isalpha() and i.isupper():
        a+=s[j].upper()
        j+=1
    else:
        a+=i
print(a)
