#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # max_money = [0] * n
        # max_money[-1] = nums[-1]
        # max_money[-2] = nums[-2]
        # max_money.append(0) # to avoid extra check or 'out of index'
        right_1, right_2, right_3 = nums[-2], nums[-1], 0

        for i in range(n - 3, -1, -1):
            right_1, right_2, right_3 = max(right_2, right_3) + nums[i], right_1, right_2

        return max(right_1, right_2)
# @lc code=end

