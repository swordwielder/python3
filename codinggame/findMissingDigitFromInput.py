n=int(input())
for i in range(n):
    a='0123456789'
    line = input()
    for i in line:
        if i in a:
            a=a.replace(i,'')
    print(a)
