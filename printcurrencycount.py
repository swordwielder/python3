t=input().split()
n=int(input())
a=[]
for i in range(len(t),0,-1):
    m=n//int(t[i-1])
    if m>0:n-=int(t[i-1])*m;a.append(str(m)+"x"+str(int(t[i-1])))
print(*a)




note_types = list(reversed(list(map(int,input().split()))))
n = int(input())
final=''
i=0
count=0
while n!=0:
    if n-note_types[i]>=0:
        n-=note_types[i]
        count+=1
    else:
        if count>0:
            final+=str(count)+'x'+str(note_types[i])+' '
        count=0
        i+=1
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(final[:-1])
