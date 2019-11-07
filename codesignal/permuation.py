def mutateTheArray(n, a):
    
    
    if n<=1:
        return a;
    else:
        b = [a[0]+a[1]]
        for i in range (1,n):
            
            b.append(sum(a[i-1:i+2]))
        
        return b;
