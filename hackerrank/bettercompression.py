
import string
s='a4b6c7c6b3d1a56b43a2h5a2'
# output:  a60b9c13d1
n= len(s)
i=0
countdict={}
while i<n:
    elem = s[i]
    if elem.isalpha():
        start = i+1
        end = start
        while (end< n and s[end].isnumeric()):
            end+=1
        count = int(s[start:end])
        if elem not in countdict:
            countdict[elem]=count
        else:
            countdict[elem]+=count
        i = end

    else:
        i+=1



solution=''
print(countdict)
alpha='abcdefghijklmnopqrstuvwxyz'
for letter in alpha:
    if letter in countdict:
        solution+=letter+str(countdict[letter])

print(solution)
