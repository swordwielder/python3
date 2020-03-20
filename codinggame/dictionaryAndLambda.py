d={}
for i in range(10):
    row=input().split()
    t=0
    for i in range(1,len(row)):
        t+=float(row[i])
    t=t/(len(row)-2)
    d[row[0]]=t
sortedD=sorted(d.items(),key=lambda kv:kv[1])
for i in sortedD:
    print(i[0])
