class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        B=[]
        j=0
        for i in range(len(A)):
            if A[i]%2==0:
                B.append(A[i])
                j+=1
        
        for index in range(len(A)):
            if A[index]%2==1:
                B.append(A[index])
                j+=1
        return B
        
