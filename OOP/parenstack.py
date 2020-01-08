
def solution(x):
    a=[]
    for i in range(len(x)):
        if x[i]=='(':
            a.append(x[i])
        if x[i]==')':
            if !a.empty():
                a.pop()
            else:
                print('error')
    if !a.empty():
        print('error')
        
    b=[]
    for i in range(len(x)):
        if x[i]!=')'
