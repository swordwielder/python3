n=int(input())
for i in range(n):
    b,t=[int(j) for j in input().split()]
    c=(b-32)*5/9
    if c>t:
        print("Higher")
    elif c==t:
        print("Same")
    else:
        print("Lower")
