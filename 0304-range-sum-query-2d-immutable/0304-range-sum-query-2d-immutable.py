class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # making matrix 1 row and 1 col bigger to adjust for edge case
        self.sumMatrix = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMatrix[r][c + 1]
                self.sumMatrix[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2, = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bot_right = self.sumMatrix[r2][c2]
        above = self.sumMatrix[r1 - 1][c2]
        left = self.sumMatrix[r2][c1 - 1]
        top_left = self.sumMatrix[r1 - 1][c1 - 1]

        return bot_right - above - left + top_left



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)