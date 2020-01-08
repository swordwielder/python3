class Solution:
    def reverse(self, x):
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

