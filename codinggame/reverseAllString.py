a=[]
s=input().split()
for i in s:a.append(i[::-1])
print(' '.join(a))


s=input().split()
print(" ".join(["".join(reversed(i)) for i in s]))
