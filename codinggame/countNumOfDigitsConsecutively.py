#my sol
c=1
p=''
a=''
n=input()
for i in n:
    if p=='':
        p=i
    elif p==i:
        c+=1
    else:
        a+=str(c)+p
        p=i
        c=1
print(a+str(c)+p)




#sol2
n = input()

r= []

for c in n:
    if r and r[-1][1]==c: r[-1][0]+=1
    else: r+=[[1,c]]

for i,v in r:
    print(end=str(i)+v)
