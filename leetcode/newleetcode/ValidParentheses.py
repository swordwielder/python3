class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if i=='(' or i =='[' or i=='{':
                a.append(i)
            else:
                if len(a)==0:
                    return False
                b=a.pop()
                if i==')':
                    if b!='(':
                        return False;
                elif i==']':
                    if b!='[':
                        return False;
                elif i=='}':
                    if b!='{':
                        return False;
        if len(a)!=0:
            return False
        return True
