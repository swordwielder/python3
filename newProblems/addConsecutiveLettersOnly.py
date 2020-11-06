#sol1
s=input()
d={}
for i in range(len(s)-1):
 if s[i]==s[i+1]:d[s[i]]=s[i]
for i in s:
 if i in d or i==' ':print(i,end='')


#not working
