import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
h = []
for i in range(n):
    start, end = [int(j) for j in input().split()]
    h += [i for i in range(start, end)]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(len(set(h)))



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
h = [0]*24
for i in range(n):
    start, end = [int(j) for j in input().split()]
    for j in range(start, end):h[j] = 1

print(sum(h))

