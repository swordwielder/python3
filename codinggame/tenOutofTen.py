m=input()
c=len(m)
t=0
b=[]
for i in m:
 if i.isalpha():
  if i not in b:
   b.append(i)
   t+=ord(i)
print(str(t%c)+'/10' if t%c<=10 else '10/10')



m=input()
print(f'{min(10,sum({s.isalnum()*ord(s)for s in m})%len(m))}/10')

