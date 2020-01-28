n=int(input())
for i in range(n):
    x=int(input())
    print(len(str(bin(x))[2:]))
