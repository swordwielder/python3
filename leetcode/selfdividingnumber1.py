class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = [];
        add = False;
        for i in range(left,right+1):
            if not ('0' in str(i)):
                if len(str(i))==1:
                    arr.append(i);
                else:
                    s = str(i);
                    for j in len(s):
                        add = True;
                        
                        
                        
        return arr;
