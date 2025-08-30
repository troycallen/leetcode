class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if board is None:
            return board
        
        ROWS = len(board)
        COLS = len(board[0])
        all_crushed = True

        # mark rows
        for row in range(ROWS):
            for col in range(COLS - 2):
                #print(board[row][col + 1])
                num1 = abs(board[row][col])
                num2 = abs(board[row][col + 1])
                num3 = abs(board[row][col + 2])

                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[row][col] = -num1
                    board[row][col + 1] = -num2
                    board[row][col + 2] = -num3
                    all_crushed = False

        # mark cols
        for col in range(COLS):
            for row in range(ROWS - 2):
                num1 = abs(board[row][col])
                num2 = abs(board[row + 1][col])
                num3 = abs(board[row + 2][col])

                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[row][col] = -num1
                    board[row + 1][col] = -num2
                    board[row + 2][col] = -num3
                    all_crushed = False
                
        # crush
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] <= 0:
                    board[row][col] = 0

        # gravity
        for col in range(COLS):
            idx = ROWS - 1
            for row in range(ROWS -1, -1, -1):
                if board[row][col] > 0:
                    board[idx][col], board[row][col] = board[row][col], board[idx][col]
                    idx -= 1
        
        return board if all_crushed else self.candyCrush(board)
