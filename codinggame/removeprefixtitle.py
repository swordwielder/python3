pre='DrMrMrsMsLordLadySir'
n = 'Lord Richard Dichin'
for i in range(n):
    name = input().split(',')[0].split()
    if name[0] in pre:
        name.pop(0)
    s=[name[i][0] for i in range(0,len(name))]
    print('.'.join(s)+'.')
