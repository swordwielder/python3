n = int(input())
print(n*'#')
for i in range(1, (2*n+1)//2 + 1):
    for j in range((2*n+1)//2 - i):
        print(" ", end = "")
    for k in range((i*2)-1):
        print("#", end = "")
    print()

for i in range((2*n+1)//2 + 1, 2*n + 1):
    for j in range(i - (2*n+1)//2 -1):
        print(" ", end = "")
    for k in range((2*n+1 - i)*2 - 1):
        print("#", end = "")
    print()
