#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        temp = []
        locked_column = set()
        locked_diag_up = set()
        locked_diag_down = set()
        left_border = (n + 1) // 2
        def helper(row):
            if row == n:
                res.append([''.join(sublist) for sublist in temp])
                return
            # for row in range(startRow, n):
            limit = left_border if row == 0 else n
            for column in range(limit):
                if column not in locked_column and (row + column) not in locked_diag_up and (row - column) not in locked_diag_down:
                    temp[row][column] = 'Q'
                    locked_column.add(column)
                    locked_diag_up.add(row + column)
                    locked_diag_down.add(row - column)

                    helper(row + 1)

                    temp[row][column] = '.'
                    locked_column.remove(column)
                    locked_diag_up.remove(row + column)
                    locked_diag_down.remove(row - column)
            
            return

        # generate temp
        for i in range(n):
            lst = ['.'] * n
            temp.append(lst)
        
        # main action
        helper(0)
        
        # mirror the left half result
        is_odd = (n % 2 == 1)
        for i in range(len(res)):
            if is_odd and res[i][0][n//2] == 'Q': # don't mirror the middle column
                continue
            reversed_board = []
            for row in res[i]:
                reversed_board.append(row[::-1])
            res.append(reversed_board)

        return res
# @lc code=end

