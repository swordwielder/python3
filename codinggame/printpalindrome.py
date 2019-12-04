import sys
import math

s=input().lower()
l=len(s)
first=0
end=l-1
toreturn=''
while first<end:
    if s[first]==s[end]:
        toreturn+=s[first]
        first+=1
        end-=1
    else:
        break
if toreturn:
    print(toreturn)
else:
    print('Nothing')




s = input().lower()
t = ''
i = 0
while i < len(s)//2 and s[i] == s[len(s)-1-i]:
    t += s[i]
    i+=1
print(t or "Nothing")  #print t or nothing
