s=input()
a=''
for i in s:
    a+=s[i]
    if s[i] in 'aeiouAEIOU':
        a+='p'+s[i]
print(a)
