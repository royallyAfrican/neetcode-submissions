class Solution:
    def flood_fill(self,i,j,grid, seen):

        # handle up 1
        if(i-1>=0 and grid[i-1][j]!="0" and (i-1,j) not in seen):
            seen.add((i-1,j))
            self.flood_fill(i-1,j,grid,seen)

        # handle down 1
        if(i+1<len(grid) and grid[i+1][j]!="0" and (i+1,j) not in seen):
            seen.add((i+1,j))
            self.flood_fill(i+1,j,grid,seen)

        # handle left 1
        if(j-1>=0 and grid[i][j-1]!="0" and (i,j-1) not in seen):
            seen.add((i,j-1))
            self.flood_fill(i,j-1,grid,seen)

        # handle left 1
        if(j+1<len(grid[0]) and grid[i][j+1]!="0" and (i,j+1) not in seen):
            seen.add((i,j+1))
            self.flood_fill(i,j+1,grid,seen)


    def numIslands(self, grid: List[List[str]]) -> int:
        # traverse row by row 

        # for each 1 found, flood fill 
        # adding it to seen. 

        # if in seen already move on.  
        # else move on. 

        seen = set()
        res=0;
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if( (i,j) not in seen and grid[i][j]=="1"):
                    res+=1
                    seen.add( (i,j))
                    self.flood_fill(i,j,grid,seen)
        return res;




        