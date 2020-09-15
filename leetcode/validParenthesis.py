class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        t='true'
        f='false'
        for i in s:
            if i in '[{(':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                b=stack.pop()
                if i==')':
                    if b!='(':
                        return False
                elif i==']':
                    if b!='[':
                        return False
                elif i=='}':
                    if b!='{':
                        return False
        if len(stack)!=0:
                return False
        return True
