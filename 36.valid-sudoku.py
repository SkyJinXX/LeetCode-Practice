#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        blocks = [[0,1,2],[3,4,5],[6,7,8]]
        valid_pool = [0] * 9

        for row in board:
            for i in row:
                if i == '.':
                    continue
                else:
                    if valid_pool[int(i) -1 ] >= 1:
                        return False
                    else:
                        valid_pool[int(i)-1] += 1
            valid_pool = [0] * 9
        
        for column in range(9):
            for row in range(9):
                if board[row][column] == '.':
                    continue
                else:
                    if valid_pool[int(board[row][column])-1] >= 1:
                        return False
                    else:
                        valid_pool[int(board[row][column])-1] += 1
            valid_pool = [0] * 9
        
        for row_block in blocks:
            for column_block in blocks:
                for row in row_block:
                    for column in column_block:
                        if board[row][column] == '.':
                            continue
                        else:
                            if valid_pool[int(board[row][column])-1] >= 1:
                                return False
                            else:
                                valid_pool[int(board[row][column])-1] += 1
                valid_pool = [0] * 9

        return True


        
# @lc code=end

