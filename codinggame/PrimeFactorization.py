n=int(input())
i=2
f=[]
while i*i<=n:
 if n%i:i+=1
 else:n//=i;f.append(i)
if n>1:f.append(n)
print(sum(f))
