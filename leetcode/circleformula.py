a, b = [int(i) for i in input().split()]
n = int(input())
total=0
for i in range(n):
    x, y, r = [int(j) for j in input().split()]
    if (x-a)**2+(y-b)**2<=r**2:
        total+=1
print(total)
