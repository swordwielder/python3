#sol1
n=int(input())
s=ord(input())
y=65+32*(s>96)
for i in range(n):print(end=chr((s+i-y)%26+y))

#sol2
n=int(input())
s=input()
r=""
x=ord("a")if s.islower()else ord("A")
for i in range(n):r+=chr((ord(s)+i-x)%26+x)
print(r)


#mine, not complete 85%
a='abcdefghijklmnopqrstuvwxyz'
n=int(input())
s=input()
if s.isupper():
    a=a.upper()
b=a.index(s)
print(a[b:b+n],end='')
if b+n>26:
    print(a[:(b+n)%26])

