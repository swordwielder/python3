#sol 1

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

days = ["Mo","Tu","We","Th","Fr","Sa","Su"]

A,B = input().split('-')

iA = 0
for j in range(7):
    if days[j] == A:
        iA = j
iB = 0
for j in range(7):
    if days[j] == B:
        iB = j


n = int(input())
for i in range(n):
    day = input()

    idx = 0
    for j in range(7):
        if days[j] == day:
            idx = j
    
    if iA <= iB:
        if (idx >= iA and idx <= iB) or (iA == iB):
            print("yes")
        else:
            print("no")
    else:
        if idx >= iA or idx <= iB:
            print("yes")
        else:
            print("no")

#sol2, incomplete, 60%

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = input()
s=r[:2]
e=r[-2:]
# print(s,e)
n = int(input())
a=[]
for i in range(n):
    a.append(input())
if e!=s:
    for i in range(n):
        if e==a[i]:
            print('yes')
        if s==a[i]:
            print('yes')
        else:
            print('no')
else:
    for i in range(n):
        print('yes')
