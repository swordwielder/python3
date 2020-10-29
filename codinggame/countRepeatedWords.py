n = int(input())
a=[]
t=0
for word in input().split():
    a.append(word)
b=' '.join(a)
c=[]
for i in a:
    if a.count(i)>1 and i not in c:
        c.append(i)
        t+=1
print(t)


