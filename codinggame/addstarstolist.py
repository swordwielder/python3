n=int(input())
a=[]
for i in input().split():a.append(int(i))
for i in range(1,10):print(str(i)+':'+a.count(i)*'*')
