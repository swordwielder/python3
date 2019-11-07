def alternatingSort(a):
    b=[]
    length = len(a)-1
    count=0
    i=1
    flag=False;
    if len(a)<=1:
        return True;
    else:
        if len(a)%2==1:
            flag=True;
        while count < length:
            b.append(a[count])
            b.append(a[length])
            count+=1
            length-=1
        if flag:
            b.append(a[count])
        print(b)
        for i in range(1,len(b)):
            if b[i]<=b[i-1]:
                return False;
        
        return True;
