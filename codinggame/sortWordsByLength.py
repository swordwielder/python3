#my solution
n=int(input())
b={}
for i in range(n):
 w=input()
 b[w]=len(w)
s=sorted(b.items(),key=lambda x:x[1])
for i in s:print(i[0])



#solution 2
print(*sorted([input() for i in range(int(input()))],key=len),sep='\n')

#Solution 3
for w in sorted([input()for _ in range(int(input()))],key=len):print(w)
