a=int(input())
for i in range(a):
    n=input().split(',')
    if len(n)==2:
        print(n[1][1:])
    else:
        print('N/A')
