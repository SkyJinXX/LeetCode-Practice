#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        new_rotten_oranges = deque()
        fresh_orange = 0

        # store initial rotten oranges and count fresh oranges
        for row in range(m):
            for column in range(n):
                if grid[row][column] == 2:
                    new_rotten_oranges.append((row, column))
                if grid[row][column] == 1:
                    fresh_orange += 1

        # begin rotting. one while loop, one minute.
        minutes = 0
        while new_rotten_oranges and fresh_orange: # check fresh_orange too, because we can avoid unnecessary rotting when fresh_orange is 0
            for _ in range(len(new_rotten_oranges)):
                row, column = new_rotten_oranges.popleft()
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for d_row, d_column in directions:
                    next_row, next_column = row + d_row, column + d_column
                    if -1 < next_row < m and -1 < next_column < n and grid[next_row][next_column] == 1:
                        grid[next_row][next_column] = 2
                        fresh_orange -= 1
                        new_rotten_oranges.append((next_row, next_column))
            minutes += 1

        if fresh_orange:
            return -1
        else:
            return minutes
        

# @lc code=end

