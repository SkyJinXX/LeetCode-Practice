#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_boundary = 0
        right_boundary = len(nums) - 1
        
        while right_boundary > left_boundary:
            if nums[left_boundary] < nums[right_boundary]:
                break

            middle = left_boundary + (right_boundary - left_boundary) // 2
            if nums[middle] < nums[left_boundary]:
                right_boundary = middle
            else:
                left_boundary = middle + 1
        
        return nums[left_boundary]


# @lc code=end

