import math
import statistics
a=[int(i) for i in input().split(' ')]
if len(a)%2==0:
    print(math.ceil(sum(a)/len(a)))
else:
    print(statistics.median(a))

