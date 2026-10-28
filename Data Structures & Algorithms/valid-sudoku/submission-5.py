class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            check = set()
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] not in check:
                        check.add(board[row][col])
                    else:
                        return False

        for row in range(9):
            check = set()
            for col in range(9):
                if board[col][row] != '.':
                    if board[col][row] not in check:
                        check.add(board[col][row])
                    else:
                        return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                check = set()
                i = 0
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] != '.':
                            if board[r][c] not in check:
                                check.add(board[r][c])
                            else:
                                return False

        return True



        
        