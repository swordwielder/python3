#two types of blocks, get to the height of H by different addition
n = int(input())
p, q = [int(i) for i in input().split()]
b = int(n/p)
a = 0
while b>=0:
    if (n-b*p)%q == 0:
        a = b + (n-b*p)/q
        break
    else:
        b -= 1

print(int(a))

