class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter, value  = 0, 0
        rows, cols = len(grid), len(grid[0])
        def checkonsides(grid, i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            checkonsides(grid, i + 1, j)
            checkonsides(grid, i, j + 1)
            checkonsides(grid, i - 1, j)
            checkonsides(grid, i, j - 1)
        for i in range(0, rows):
            for j in range(0, cols):
                  if grid[i][j] == '1':
                    counter = counter + 1
                    checkonsides(grid, i, j)
        return counter