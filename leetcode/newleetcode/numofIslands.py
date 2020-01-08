class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        numIslands=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] =='1':
                    numIslands+=1
                    self.dfs(grid, i , j)
                
                
                
        return numIslands
    def dfs(self,grid,i,j):
        if i<0 or i==len(grid) or j<0 or j==len(grid[i]) or grid[i][j]!='1':
            return 0
        
        grid[i][j]='0'
        
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        
