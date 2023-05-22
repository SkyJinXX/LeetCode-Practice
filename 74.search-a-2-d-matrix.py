#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left_boundary = 0
        right_boundary = m * n - 1

        while left_boundary <= right_boundary:
            middle = left_boundary + (right_boundary - left_boundary) // 2
            row_of_middle = middle // n
            column_of_middle = middle % n
            if matrix[row_of_middle][column_of_middle] == target:
                return True
            elif matrix[row_of_middle][column_of_middle] > target:
                right_boundary = middle - 1
            else:
                left_boundary = middle + 1
        
        return False
# @lc code=end

