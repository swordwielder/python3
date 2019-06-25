class Solution:
    def removeOuterParentheses(self, S):
        a=""
        count=0
        for c in S:
            if c == '(':
                if count !=0:
                    a += '('
                count+=1 
            elif c== ')':
                if count != 1:
                    a += ')'
                count-=1
        return a
    
