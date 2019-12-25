n=int(input())
for i in range(n):
    w=input()
    a=0
    s=''
    for j in range(1,len(w)):
        if w[j]=='r':
            a+=4
        if w[j]=='w':
            a+=2
        if w[j]=='x':
            a+=1
        if j%3==0:
            s+=str(a)
            a=0
    print(s)
