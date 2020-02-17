source=input()
target=input()
a=''
for i in range(len(source)):
    if target[i]==source[i]:
        continue
    a=target[:i]+source[i:]
    print(a)
print(target)
