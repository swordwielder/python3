import sys
import math
s = input()
t=0
if s.isnumeric():
    
    for i in range(1,len(s)):
        t+=int(s[i])
    t*=int(s[0])
    print(t)
else:
    if s[0]=='-':
        for i in range(2,len(s)):
            t+=int(s[i])
        t*=int(s[1])
        print('-'+str(t))
    else:
        print('INVALID')
