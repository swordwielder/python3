x=int(input())
n=int(input())
t=int(input())
if t==0:
    print(x)
else:
    b=t*60//n
    print(x-b if x-b>0 else 0)
