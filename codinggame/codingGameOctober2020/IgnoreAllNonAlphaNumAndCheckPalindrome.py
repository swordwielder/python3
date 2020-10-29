t=input().split()
a=''.join(t).lower()
b=''
for i in a:
 if i.isalnum():b+=i
print('YES' if b==b[::-1] else 'NO')
