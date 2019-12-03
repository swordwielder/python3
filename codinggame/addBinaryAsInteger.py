#Adding two numbers as Binary as Integers numbers
n = int(input())
for i in range(n):
    p, q = [int(j) for j in input().split()]
    f = int(str(bin(p))[2:])
    s = int(str(bin(q))[2:])
    print(f+s)
