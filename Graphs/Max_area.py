class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m , n = len(grid) ,len(grid[0])
        max_count = 0
        count = 0
        

        def dfs(i,j) :
            nonlocal count 
            if i < 0 or i>=m or j <0 or j >= n or grid[i][j] != 1 :
                return
            else :
                count += 1 
                grid[i][j] = 0
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i-1,j)
        

        for i in range(m):
            for j in range(n) :
                if grid[i][j] == 1 :
                    count = 0
                    dfs(i,j)
                if count > max_count :
                        max_count = count     
        return max_count 
