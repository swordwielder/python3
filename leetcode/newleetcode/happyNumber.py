#solution
class Solution:
    def isHappy(self, n: int) -> bool:
        a=str(n)
        b=0
        while len(a)!=1:
            print(a)
            b=0
            for i in a:
                b+=int(i)**2
            a=str(b)
        if int(a)==1 or int(a)==7:
            return True
        else:
            return False

#solution 2
