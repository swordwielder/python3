x,y= input().split()
a=''
for i in range(len(x)):
    if x[i]=='1' or y[i]=='1':
        a+='1'
    else:
        a+='0'
print(a)
