class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        count = 0
        for i in S:
            if i=='(':
                stack.append('(')
            else:
                if len(stack)==0:
                    count +=1
                else:
                    stack.pop()
        return count+len(stack)
