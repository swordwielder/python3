s = input()
out = s[::2]
if not len(s) % 2:
    out += s[::-1][::2]
else:
    out += s[::-1][1::2]
print(''.join(out))



s = input()
r=''
for i in range(0,len(s),2):
    r+=s[i]

x=1
if len(s)%2==0:
    x=0
for i in range(x,len(s),2):
    r+=s[len(s)-1-i]
print(r)
