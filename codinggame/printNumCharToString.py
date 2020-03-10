print(*[int(a[:-1])*a[-1]for a in input().split()],sep="")

x=""
for i in input().split():
  x+=int(i[0:len(i)-1])*str(i[len(i)-1])
print(x)


d=input().split()
a=''
b=''
r=''
for i in d:
    for j in i:
        if j.isnumeric():a+=j
        else:b+=j
    r+=int(a)*b
    a=''
    b=''
print(r)

