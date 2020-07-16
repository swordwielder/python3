class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])        
        # transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
        #print the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j],end=' ')
            print()
            
        # reverse each row
        for i in range(n):
            matrix[i].reverse()
            
        print()
        #print the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j],end=' ')
            print()
