import re
n = int(input())
s = input()
s=re.sub(r'[^A-Za-z]', '', s).lower()
l=[]
for i in s:
    l.append(i)
l.sort()
c=l[0]
for i in l:
    if i==c:
        print(i,end="")
    else:
        c=i
        print()
        print(i,end="")
