#solution
a="JFMAMJJASOND"
m=input()
print(a[(a.index(m[:2])+len(m))%12])




#incomplete, mine
m='JFMAMJJSOND'
n=input()

print(m[(int(m.index(n[-2:])+2))%12])


