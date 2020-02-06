m,a,n=[int(i) for i in input().split()]
b=0
for i in range(1,n+1):
    b+=m*i
print(0 if b<=a else b-a)
