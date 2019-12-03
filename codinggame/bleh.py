m = int(input())
i = list(map(int,input().split()))
n=0
arr=[]
for x in range(1,m):
    if x**2>m:
        break
    n=x**2
    if n not in i:
        arr.append(n)

if len(arr) == 0:
    print ('None')
else:
    print(' '.join(list(map(str,arr))))
