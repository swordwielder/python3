a=[]
for i in range(int(input())):
    a.append(input())
print('\n'.join(a[::2]))
print('\n'.join(a[1::2]))
