#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
# WA
# [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]

class Solution:
    def solve(self, board: List[List[str]]) -> None: # only search from borders, every step can confirm a cell/node.
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, column):
            if row == m or row == -1 or column == n or column == -1 or board[row][column] != 'O':
                return
            board[row][column] = '#'

            for direction in directions:
                d_row, d_column = direction
                next_row, next_column = row + d_row, column + d_column

                dfs(next_row, next_column)

        for i in range(n):# search 'O' from top border and bottom border
            dfs(0, i)
            dfs(m - 1, i)
        for i in range(m):# search 'O' from left border and right border
            dfs(i, 0)
            dfs(i, n - 1)
        
        for row in range(m):
            for column in range(n):
                if board[row][column] == 'O':
                    board[row][column] = 'X'
                elif board[row][column] == '#':
                    board[row][column] = 'O'

    # def solve(self, board: List[List[str]]) -> None: # traverse with normal order(left to right, top to bottom)
    #     m, n = len(board), len(board[0])
    #     safe_set = set()
    #     def helper(row: int, column: int):
    #         nonlocal is_captured
    #         directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    #         temp_set.add((row, column))

    #         for direction in directions:
    #             d_row, d_column = direction
    #             next_row, next_column = row + d_row, column + d_column

    #             if next_row == m or next_row == -1 or next_column == n or next_column == -1:
    #                 is_captured = False
    #             elif board[next_row][next_column] == 'O' and (next_row, next_column) not in temp_set:
    #                 helper(next_row, next_column)


    #     for row in range(m):
    #         for column in range(n):
    #             if board[row][column] == 'O' and (row, column) not in safe_set:
    #                 print('for for的helper:', row, column)
    #                 temp_set = set()
    #                 is_captured = True
    #                 helper(row, column)

    #                 if is_captured:
    #                     for r, c in temp_set: # warning! don't use 'row' 'column' agian
    #                         board[r][c] = 'X'
    #                 else:
    #                     safe_set.update(temp_set)

# @lc code=end

