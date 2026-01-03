class Solution(object):
    def countNegatives(self, grid):
        m=len(grid)
        n=len(grid[0])
        count=0
        for row in range (m-1,-1,-1):
            col=n-1

            while col>=0 and grid[row][col]<0:
                count+=1
                col-=1                

        return count            


        