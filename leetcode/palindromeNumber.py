class Solution(object):
    def isPalindrome(self, x):
        a = str(x)
        b = a[::-1]
        
        if a == b:
            return True
        else:
            return False
        
        
        """
        :type x: int
        :rtype: bool
        """
        
