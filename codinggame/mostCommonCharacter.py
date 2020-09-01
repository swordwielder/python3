w=input()
c=0
for i in w:
 if w.count(i)>c and i!=' ':c=w.count(i)
print(c)


#2
from collections import Counter
print(Counter("".join([x for x in input() if x.isalpha()])).most_common(1)[0][1])
