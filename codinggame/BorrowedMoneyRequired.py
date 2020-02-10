m,a,n=[int(i) for i in input().split()]
b=0
for i in range(1,n+1):
    b+=m*i
print(max(0,b-a))


def Solution():
	m,a,n=map(int,input().split())
	n=m*n*-~n//2
	print([n-a,0][n<a])
