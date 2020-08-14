#sol 1 40%
import sys
import math


s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]
s3=[]
for i in range(len(s1)):
    if s2[i]:
        s3.append(s1[i]+s2[i])
    else:
        print('Invalid')
        sys.exit(0)
s3=[str(i) for i in s3]
print(' '.join(s3))
