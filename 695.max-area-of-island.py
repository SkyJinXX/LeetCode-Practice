#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        area = 0
        m = len(grid)
        n = len(grid[0])
        def helper(row, column):
            nonlocal area
            grid[row][column] = 0
            area += 1
            if row + 1 < m and grid[row + 1][column] == 1:
                helper(row + 1, column)
            if column + 1 < n and grid[row][column + 1] == 1:
                helper(row, column + 1)
            if column - 1 > -1 and grid[row][column - 1] == 1:
                helper(row, column - 1)
            if row - 1 > -1 and grid[row - 1][column] == 1:
                helper(row - 1, column)

        for row in range(m):
            for column in range(n):
                if grid[row][column] == 1:
                    area = 0
                    helper(row, column)
                    max_area = max(max_area, area)
        
        return max_area
# @lc code=end

