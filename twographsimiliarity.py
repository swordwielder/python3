n=int(input())
a=[]
b=[]
c=''
d=[]
for i in range(n):
    a.append(input())
e=input()
for i in range(n):
    b.append(input())
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]==b[i][j]:
            c+=a[i][j]
        elif a[i][j]=='.':
            c+=b[i][j]
        elif b[i][j]=='.':
            c+=a[i][j]
        else:
            c+='X'
    d.append(c)
    c=''
for i in d:
    print(i)
