n=int(input())
a=bin(n)
c=n+1
d=bin(c)
while d.count('1')!=a.count('1'):
    c+=1
    d=bin(c)
print(c)
