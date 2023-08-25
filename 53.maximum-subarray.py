#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        last_dp = float('-inf')
        
        for num in nums:
            if last_dp > 0:
                last_dp = last_dp + num
            else:
                last_dp = num
            maxSum = max(maxSum, last_dp)

        return maxSum
# @lc code=end

