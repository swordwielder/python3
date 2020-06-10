def mutateTheArray(n, a):
    b=[]
    for i in range(len(a)):
        total=0
        if i!=0:
            total+=a[i-1]
        try:
            total+=a[i+1]
        except:
            total+=0
        total+=a[i]
        
        b.append(total)
    return b

