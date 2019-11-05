class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # compute the max on every col & line
        max_lines = [-1 for k in range(len(grid))]
        max_columns = [-1 for k in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_lines[i] = max(max_lines[i], grid[i][j])
                max_columns[j] = max(max_columns[j], grid[i][j])
        # increase every square as much as possible
        cumulated_increase = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cumulated_increase += min(max_lines[i],
                                          max_columns[j]) - grid[i][j]
        return cumulated_increase
