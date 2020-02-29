class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        a=0
        for i in grid:
            for j in range(len(i)-1,-1,-1):
                if i[j]<0:
                    a+=1
                else:
                    break
        return a
