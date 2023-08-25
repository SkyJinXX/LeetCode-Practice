#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_zero_index = None
        for i in range(len(nums) - 1, -1, -1):
            if farthest_zero_index != None and (farthest_zero_index - i) < nums[i]:
                farthest_zero_index = None
            elif nums[i] == 0:
                farthest_zero_index = i
        
        return farthest_zero_index == None

# @lc code=end

