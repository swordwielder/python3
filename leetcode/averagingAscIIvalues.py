import math
s=input()
print(math.floor((sum([ord(i) for i in s])/len(s))))
