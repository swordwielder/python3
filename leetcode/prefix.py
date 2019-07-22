class Solution(object):
    def longestCommonPrefix(self, strs):
        l=list(zip(*strs))
        check =""
        if not strs:
            return ""
        
        for i in l:
            if len(set(i))==1:
                check+=i[0]
            else:
                break
            #while check not in i:
                #check = check[:-1]
                
        
        return check    
            
        
        
        
        """
        :type strs: List[str]
        :rtype: str
        """
        




 check =""
        if strs:
            check = strs[0]
        else:
            return ""
        
        for i in strs:
            
            while check not in i:
                check = check[:-1]
                
        
        return check    
            
