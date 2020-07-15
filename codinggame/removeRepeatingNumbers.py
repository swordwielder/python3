n=input()

l=[n[0]]
l += [n[m+1] for m in range(len(n)-1) if n[m] != n[m+1]]

print("".join(l))


#my solution 2 
n=input()
a=[]
b=n[0]
t=''
t+=b
for i in range(1,len(n)):
 if n[i]!=b:
    t+=str(n[i])
    b=n[i]
print(t)
