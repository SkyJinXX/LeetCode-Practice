#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(n)]
        current = 1
        target = n ** 2
        row, column = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d_index = 0
        while current <= target:
            matrix[row][column] = current
            dr, dc = directions[d_index]
            if -1 < row + dr < n and -1 < column + dc < n and matrix[row + dr][column + dc] == -1:
                row += dr
                column += dc
            else:
                d_index = (d_index + 1) % len(directions)
                dr, dc = directions[d_index]
                row += dr
                column += dc
            current += 1
        
        return matrix


        
# @lc code=end

