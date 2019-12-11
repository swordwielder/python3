s=input()
if len(s)==1:
    print(s)
else:
    a=''
    b=s[::-1]
    if len(s)%2==0:
        a+=b[::2]
        a+=s[::2]
        print(a)
    else:
        a+=b[1::2]
        a+=s[::2]
        print(a)
