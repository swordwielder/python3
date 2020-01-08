class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=s.lower()
        if st=='':
            return True
        i=0
        j=len(st)-1
        while i<j:
            if not st[i].isalnum():
                i+=1
                continue
            if not st[j].isalnum():
                j-=1
                continue
            if st[i]!=st[j]:
                return False
            else:
                i+=1
                j-=1
        return True
