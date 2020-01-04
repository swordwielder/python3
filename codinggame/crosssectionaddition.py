n = int(input())
sums=0
for i in range(n):
    arr=[int(i) for i in input().split()]
    back=len(arr)-1-i
    if i!=back:
        sums+=(arr[i] +arr[back])
    else:
        sums+=arr[i]
print(sums)
