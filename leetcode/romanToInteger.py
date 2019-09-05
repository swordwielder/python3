class Solution:
    def romanToInt(self, s: str) -> int:
        count =0
        for i in s:
            if i=="I":
                count+=1
            if i=="V":
                count+=5
            if i=="X":
                count+=10
            if i=="L":
                count+=50
            if i=="C":
                count+=100
            if i =="D":
                count+=500
            if i =="M":
                count +=1000
                
        if "IV" in s:
            count-=2
        if "IX" in s:
            count-=2
        if "XL" in s:
            count-=20
        if "XC" in s:
            count-=20
        if "CD" in s:
            count-=200
        if "CM" in s:
            count-=200
            
        return count
                
        
        
        
        
