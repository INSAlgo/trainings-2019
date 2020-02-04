class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = [0 for k in range(len(grid))]
        col = [0 for k in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
        cpt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (row[i] != 1 or col[j] != 1):
                    cpt += 1
        return cpt
                