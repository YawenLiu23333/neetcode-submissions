class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    print('1')
                    return False
                seen.add(board[row][col])

        for row in range(9):
            seen2 = set()
            for col in range(9):
                if board[col][row] == '.':
                    continue
                if board[col][row] in seen2:
                    print('2')
                    return False
                seen2.add(board[col][row])

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen3 = set()
                for boxr in range(row, row + 3):
                    for boxc in range(col, col + 3):
                        if board[boxr][boxc] == '.':
                            continue
                        if board[boxr][boxc] in seen3:
                            return False
                        seen3.add(board[boxr][boxc])
        
        return True 





                

             