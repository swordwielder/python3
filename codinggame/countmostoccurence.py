words=input()
c=1
for i in words:
    if i!=' ':
        if words.count(i)>c:
            c=words.count(i)
print(c)


