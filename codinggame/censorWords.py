import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

c = int(input())
f = [i.lower() for i in input().split()]
n = int(input())
for i in range(n):
    report = input().split()
    for j, k in enumerate(report):
        if k.lower() in f:
            report[j] = f"{k[0]}{'*'*(len(k)-2)}{k[-1]}"
    print(' '.join(report))








c = int(input())
_list = input()
n = int(input())
for i in range(n):
    r=''
    report = input().split()
    for j in report:
        if _list.lower() == j.lower():
            r+=j[0]
            for k in range(1,len(j)-1):
                r+='*'
            r+=j[len(j)-1]+' '
        else:
            r+=j+' ' 
    print(r[:-1])

