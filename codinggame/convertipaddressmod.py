w=input()
a=0
b=''
for i in w:
    a+=ord(i)
j=2
c=a
while j<6:
    b+=str(c%256)+'.'
    c=(a%256)*j
    j+=1
print(b[:-1])
