s=input()
cur=s[0]
c=1
d=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        d+=1
    if s[i]!=s[i-1]:
        d=1
    if c<d:
        c=d
        cur=s[i]
print(cur,c)
