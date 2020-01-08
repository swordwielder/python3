import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())
store=[]
print("ROWS:")
for i in range(n):
    s=input()
    print(s.count('*'))
    store.append(s)
print("COLUMNS:")

for index in range(m):
    count=0
    for line in store:

        if line[index] == '*':
            count+=1
    print(count)
