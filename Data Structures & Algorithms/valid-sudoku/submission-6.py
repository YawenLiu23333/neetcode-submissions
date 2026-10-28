class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[col][row] == '.':
                    continue
                if board[col][row] not in seen:
                    seen.add(board[col][row])
                else:
                    # print('1')
                    return False
        
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] not in seen:
                    seen.add(board[row][col])
                else:
                    # print('2')
                    return False

        for col in range(0, 9, 3):
            for row in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        # print('i is', i, 'j is', j, 'row is', row, col+ i, row + j)
                        if board[col + i][row + j] == '.':
                            continue
                        if board[col + i][row + j] not in seen:
                            seen.add(board[col + i][row + j])
                        else:
                            # print('3')
                            return False
        return True

