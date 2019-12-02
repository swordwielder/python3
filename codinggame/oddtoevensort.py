#odd on left least to greatest, even on right greatest to least
s = [int(j) for j in input().split()]
s.sort()
n=""
for i in s:
    if i%2==1:
        n+=str(i)+" "
s.sort(reverse=True)
for i in s:
    if i%2==0:
        n+=str(i)+" "
print(n[:-1])

