class Solution:
    def validRow(self, start, grid):
        seen = set()
        for k in range(9):
            number = grid[start + k]
            if number != ".":
                if number in seen:
                    return False
                seen.add(number)
        return True

    def validColumn(self, start, grid):
        seen = set()
        for k in range(9):
            number = grid[start + 9 * k]
            if number != ".":
                if number in seen:
                    return False
                seen.add(number)
        return True

    def validSquare(self, start, grid):
        seen = set()
        list_number = []
        for k in range(3):
            list_number.append(grid[start + k])
            list_number.append(grid[start + 9 + k])
            list_number.append(grid[start + 18 + k])
        for number in list_number:
            if number != ".":
                if number in seen:
                    return False
                seen.add(number)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid = []
        for l in board:
            grid += l
        for k in range(9):
            if not self.validColumn(k, grid) or not self.validRow(k * 9, grid):
                return False
        for i in range(3):
            for j in range(3):
                if not self.validSquare(i * 3 + j * 27, grid):
                    return False
        return True
