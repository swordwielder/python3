n = int(input())
newdict = {}
for i in range(n):
    item, distance = input().split()
    distance = float(distance)
    newdict[distance]=item
a=""
for i in reversed(sorted(newdict.keys())):
    a += str(newdict[i])+" ";
print (a[:-1])

