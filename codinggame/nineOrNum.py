n = input()
r=''
for i in n:
    if 9-int(i)<int(i):
        r+=str(9-int(i))
    else:
        r+=i
print(r)
