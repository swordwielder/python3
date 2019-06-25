import collections
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    array = list(arr)
    maximum = min(array)
    max2= min(array)
    for c in array:
        if maximum < c:
            #print(c)
            max2 = maximum
            maximum = c
        else:
            if c > max2 and maximum>c:
                max2=c
    print (max2)

    

i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print max(lis)
N=int(input())
s=list(set(map(int , input().split(' '))))
s.remove(max(s))
print(max(s))
