#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # pre sifting
        # reduce runtime from 6000ms to 1000ms !!
        word_counter, board_counter = Counter(word), Counter(char for sublist in board for char in sublist) 
        for c, count in word_counter.items():
            if c not in board_counter or board_counter[c] < count:
                return False

        m = len(board)
        n = len(board[0])
        directions = ((0,1), (0, -1), (1, 0), (-1, 0))
        def helper(row, column, startIndex) -> bool:
            if board[row][column] == word[startIndex]:
                if startIndex == len(word) - 1:
                    return True
                char = board[row][column]
                board[row][column] = '#'

                for d_row, d_column in directions:
                    next_row, next_column = row + d_row, column + d_column
                    if 0 <= next_row < m and 0 <= next_column < n and helper(next_row, next_column, startIndex + 1):
                        return True

                board[row][column] = char

            return False

        for row in range(m):
            for column in range(n):
                if helper(row, column, 0):
                    return True
        
        return False

# @lc code=end

