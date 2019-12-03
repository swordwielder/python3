a = input()
b = input()
alph=list(string.ascii_uppercase)*2
diff=abs(alph.index(a[0])-alph.index(b[0]))
good='true'
for i in range(1,len(a)):
    if diff != abs(alph.index(a[i])-alph.index(b[i])):
        good='false'
        break

print(good)

def distance (a,b):
    d = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dist = 0
    aPlace = 0
    for i in range(26):
        if d[i]==a:
            aPlace = i
            break
    i = aPlace    
    while d[i] != b:
        i+=1
        if i > 25:
            i=0
        dist+=1
    return dist

a = input()
b = input()
bool = True
dist = distance(a[0],b[0])


for i in range(len(a)):
    if distance(a[i],b[i]) != dist:
        bool = False

print(str(bool).lower())



l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a = input()
b = input()
d=0
flag=True
for i in range(len(b)):
    if i==0:
        d = l.index(b[i])-l.index(a[i])
    if d != l.index(b[i])-l.index(a[i]):
        flag=False
        break
if flag:
    print("true")
else:
    print('false')
