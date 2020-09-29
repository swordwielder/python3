#sol1
from fractions import Fraction
d=float(input())
s=str(Fraction(d).limit_denominator()).split('/')
if len(s)>1:print(s[0]+' / '+s[1])
else:print(int(d))


#sol2
d = float(input())
c=1
while True:
    b=d*c
    if b.is_integer():
        break
    c+=1
if c==1:
    print(int(b))
else:
    print(int(b),'/',c)
