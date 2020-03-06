#1
print(sorted(list(set([int(e)**2 for e in input().split()]))))


#2
a=input().split()
b=[]
for i in a:
    b.append(int(i)**2)
b.sort()
a=list(set(b))
a.sort()
print(a)
