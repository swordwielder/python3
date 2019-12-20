c = input()
l = int(input())
a=l-len(c)
b=a//2
d=a-b
if b!=d:
    print("CAN'T")
else:
    print(b*'*'+c+d*'*')
