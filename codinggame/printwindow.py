n=int(input())
for i in range(n*2+3):
    if i==0 or i==n*2+2:
        print((n*2+3)*'-',end='')
    elif i==n+1:
        print('|',n*'-','+',n*'-','|',sep='',end='')
    else:
        print('|',n*'.','|',n*'.','|',sep='',end='')
    print()
