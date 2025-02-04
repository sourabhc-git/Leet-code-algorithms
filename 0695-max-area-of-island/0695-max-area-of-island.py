class Solution:
    max_area = float('-inf')
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):

            if  i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 0

            area = 1
            grid[i][j] = 0

            area = area + dfs(i, j + 1)
            area = area + dfs(i + 1, j)
            area = area + dfs(i, j - 1)
            area = area + dfs(i - 1, j)

            return area

        max_area = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1:
                    area = 0
                    max_area = max(max_area, dfs(i, j))

        return max_area
