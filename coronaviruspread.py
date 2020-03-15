def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh=set()
        rotten=set()
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    fresh.add((x,y))
                elif grid[x][y] == 2:
                    rotten.add((x,y))
        time=0
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while len(fresh) > 0:
            infected = set()
            for rottenCoords in rotten:
                rotX, rotY = rottenCoords
                for direction in directions:
                    neighborX = rotX + direction[0]
                    neighborY = rotY + direction[1]
                    
                    if (neighborX,neighborY) in fresh:
                        fresh.remove((neighborX,neighborY))
                        infected.add((neighborX,neighborY))
            
            if len(infected) == 0:
                return -1
            
            rotten = infected
            time +=1
        
        return time
