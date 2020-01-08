def solution(x):
    a=[]
    
    for i in range(len(x)):
        for j in range(len(x[i])):
            a.append(x[i][j])    
    a.sort()
    print(a)
    cv=a[0][1]
    b=[]
    for i in range(1,len(a)):
        if cv<a[i][0]:
            b.append([cv,a[i][0]])
            cv=a[i][1]
        elif cv<a[i][1]:
            cv=a[i][1]
    return b
print(solution(meetings))
