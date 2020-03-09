m=input()
if len(m)%2==0:
    print('Error')
else:
    a=0
    b=len(m)
    for i in range(len(m)):
        print(a*' '+m[a:b])
        if i<len(m)//2:
            a+=1
            b-=1
        else:
            a-=1
            b+=1
