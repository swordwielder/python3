import sys
import math
s = input()
x=0
y=0
a = s.split(" ")

for i in a:
    if i=="boom":
        if x!=30:
            x+=1
    if i=="ts":
        if x!=0:
            x-=1
    if i=="ding":
        if y !=0:
            y-=1
    if i=="bing":
        if y !=10:
            y+=1
print(str(x)+" "+str(y))
