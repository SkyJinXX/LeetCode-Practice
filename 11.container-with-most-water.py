#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0

        while left_pointer < right_pointer:
            max_area = max(max_area, (right_pointer - left_pointer) * min(height[right_pointer], height[left_pointer]))
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return max_area
# @lc code=end

