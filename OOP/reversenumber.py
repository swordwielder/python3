class Solution:
    def reverse(self, x):
        print(0.75%10)
        a=str(x)
        if a[0]=='-':
            b=a[::-1]
            if (int(b[:-1:])*-1) < -2147483648:
                return 0
            else:
                return (int(b[:-1:])*-1)
        else:
            if (int(a[::-1]))>2147483648:
                return 0
            else:
                return (int(a[::-1]))

class Solution2:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        s=''

        neg=False
        if x<0:
            neg=True
            x*=-1
        while x>0:
            s+=str(x%10)
            x=x//10

        s=int(s)
        if s>2**31:
            return 0
        if neg:
            return s*-1
        return (s)
