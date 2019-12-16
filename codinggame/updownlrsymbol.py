d = dict(zip("up right up right down left".split(), "^>^>v<"))

for k, g in itertools.groupby(input().split()):
    c = len(list(g))
    print(d[k] + (str(c) if c>1 else ""), end="")






a=input().split()
b=''
c=1
if a[0]=='up':
    b+='^'
elif a[0]=='down':
    b+='v'
elif a[0]=='left':
    b+='<'
else:
    b+='>'

for i in range(1,len(a)):
    #print(a[i])
    if a[i]==a[i-1]:
        c+=1
    else:
        if c>1:
            b+=str(c)
        c=1
        if a[i]=='up':
            b+='^'
        elif a[i]=='down':
            b+='v'
        elif a[i]=='left':
            b+='<'
        else:
            b+='>'
if c >1:
    print(b+str(c))
else:
    print(b)
