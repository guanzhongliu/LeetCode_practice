'''
Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules

'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 遍历即可
        for i in range(0, 9):
            set_row = set()
            set_line = set()
            set_block = set()
            for j in range(0, 9):
                if board[i][j] != '.':
                    if board[i][j] not in set_row:
                        set_row.add(board[i][j])
                    else:
                        return False
                if board[j][i] != '.':
                    if board[j][i] not in set_line:
                        set_line.add(board[j][i])
                    else:
                        return False
                # 唯一稍复杂一点点的就是这里的计算
                block_x = (i // 3) * 3 + (j //3)
                block_y = (i % 3) * 3 + (j % 3)
                if board[block_x][block_y] != '.':
                    if board[block_x][block_y] not in set_block:
                        set_block.add(board[block_x][block_y])
                    else:
                        return False
        return True