import sys
import math


for i in range(5):
    line = input().split()
    r=''
    for j in range(len(line[0])):
        if line[0][j]=='0':
            r+=line[1][j]
        else:
            r+=line[2][j]
    print(r)
