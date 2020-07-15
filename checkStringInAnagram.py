w=input().lower()
n=int(input())
i = 0
for _ in range(n):
    s = input().lower()
    if all([s.count(c) >= w.count(c) for c in set(w)]):i += 1
print(i)


#solution 2 mine

def nd(n):
    d={}
    for i in n:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
def check(w):
    for item in w:
        if item in s:
            if s[item]<w[item]:
                return False
        else:
            return False
    return True

w=input().lower()
w=sorted(w)
w=nd(w)
n=int(input())
t=0
for i in range(n):
    s=input().lower()
    s=sorted(s)
    s=nd(s)
    if check(w):
        t+=1
print(t)

