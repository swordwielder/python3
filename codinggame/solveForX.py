#sol1
s = input().split()
t=int(s[len(s)-1])
if '-' in s:
    t+=int(s[s.index('-')+1])
if '+' in s:
    t-=int(s[s.index('+')+1])
if '*' in s:
    t/=int(s[s.index('*')-1])
if '/' in s:
    t*=int(s[s.index('/')-1])
print(int(t))


#sol 2
from re import findall
a,b,y = list(map(int,findall(r'\d+', input())))
print(round((y-b)/a))
