#solution 1
n = int(input())
m = int(input())
w = [ [int(j) for j in input().split()] for i in range(n)]

z = [sum((x-sum(t) / len(t))**2 for x in t) / len(t) for t in w]


print(w, file=sys.stderr, flush=True)
print(z, file=sys.stderr, flush=True)
print(z.index(min(z))+1)




#Solution 2
cmin = None
cmin_idx = -1

n = int(input())
m = int(input())
for i in range(n):
    w = [int(j) for j in input().split()]
    mean = sum(w)/len(w)
    var = sum((load-mean)**2 for load in w)/len(w)
    if cmin is None or var < cmin:
        cmin = var
        cmin_idx = i
print(cmin_idx+1)


#solution 3

n = int(input())
m = int(input())
h=[]
for i in range(n):
    a = [int(j) for j in input().split()]
    s=sum(a)/len(a)
    v=0
    for j in a:
        v+=(j-s)**2
    k=v/len(a)
    h+=[k]
    #print(v)

print(h.index(min(h))+1)
