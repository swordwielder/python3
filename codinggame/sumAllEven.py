print(sum([i for i in range(2,int(input())+1) if i%2==0]))


t=0
n=int(input())+1
for i in range(n):
 if i%2==0:t+=i
print(t)
