n = int(input())
a1={}
for i in range(n):
    item, distance = input().split()
    distance = float(distance)
    if item not in a1:
        a1[item]=distance
    
a1_sorted_keys = sorted(a1, key=a1.get, reverse=True)
new=[]
for r in a1_sorted_keys:
    new.append(r)
print(' '.join(new))    


#solution 2
n=int(input())
r=[x[1]for x in sorted([[float(x[1]),x[0]]for x in[input().split()for i in range(n)]],reverse=True)]
print(*r)
