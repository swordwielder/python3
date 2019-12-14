# n = int(input())

# array=[]
# for i in range(n):
#     s, p, x, y = input().split()
#     p = int(p)
#     x = int(x)
#     y = int(y)
#     array.append([s,p,x,y])
# array= sorted(array, key=lambda x: (x[1], (x[2]-x[3],x[2])),reverse=True)
# print(array[0][0])

# a[s]=p+x+y
    
dic= {k:(10-k) for k in range(10)}

print(dic)



n = int(input())

array=[]
for i in range(n):
    s, p, x, y = input().split()
    p = int(p)
    x = int(x)
    y = int(y)
    array.append([s,p,x,y])
array= sorted(array, key=lambda x: (x[1], (x[2]-x[3],x[2])),reverse=True)
print(array[0][0])
