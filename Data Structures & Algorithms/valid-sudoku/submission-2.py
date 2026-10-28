class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #checks the rows of the board
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[i][j] in seen:
                    return False
                if board[i][j] != ".":
                    seen.add(board[i][j])

        #checks the columns of the board

        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[j][i] in seen:
                    return False
                if board[j][i] != ".":
                    seen.add(board[j][i])

        #checks the subboard
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] in seen:
                            return False 
                        if board[r][c] != ".":
                            seen.add(board[r][c])

        return True

                


