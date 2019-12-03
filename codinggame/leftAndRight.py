#Add left then add right
a = input()
l=0
r=len(a)-1
b=""
while l<r:
    b+=a[l]
    b+=a[r]
    l+=1
    r-=1
if len(a)%2==1:
    b+=a[l]
print(b)
