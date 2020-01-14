import math
g = input()
w = int(input())

if g=='F':
    print(math.floor((w*0.2)+w))
elif g=='M':
    print(math.floor(w/1.2))
else:
    print('UNKNOWN')
