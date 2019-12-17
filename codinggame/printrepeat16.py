s = input()
end=16
beg=0
if len(s)>end:
    while end<=len(s):
        print(s[beg:end])
        end+=1
        beg+=1
else:
    print((end-len(s))*' '+s)



