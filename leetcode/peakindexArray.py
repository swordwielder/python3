class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        peak=0
        indexcount=0
        for index in range(len(A)):
            if A[index] > peak:
                peak = A[index]
                indexcount = index
        return indexcount



def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        peak=0
        index=0
        half=int(len(A)/2)+1
        for i in range(0,len(A),half):
            if A[i] > peak:
                peak = A[i]
                index = i
        
        
        return index
