n=int(input())
for i in range(1,n+1):
    if i%7==0 and i%5==0:
        print('FooBar')
    elif i%7==0:
        print('Bar')
    elif i%5==0:
        print('Foo')
    else:
        print(i)
