import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input().lower()
text = input().lower().split(' ')
count=0
for i in text:
    if s in i:
        count+=1
print(count)

