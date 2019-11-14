n,k=int(input()),input()
d,c={'XOOOO':'A','OXOOO':'B','OOXOO':'C','OOOXO':'D','OOOOX':'E'},0
for i in range(n):
    a=input()
    if a in d and d[a]==k[i]:
        c+=1
print(round(c/n*100))


n = int(input())
k = input()
correct=0
for i in range(n):
    a = input()
    counter = a.count('X')
    if counter==1:
        correct+=1
    

print( int(correct/n*100) )

