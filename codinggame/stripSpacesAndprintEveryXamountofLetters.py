s= input()
sentence="".join(s.split())
col = int(input())
c=0
for i in sentence:
    print(i,end='')
    c+=1
    if c==col:
        print()
        c=0
