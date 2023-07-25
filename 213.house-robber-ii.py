#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
# [1,2,3,1]
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robNoneCircle(start_index: int, end_index: int) -> int:
            n = end_index - start_index + 1
            if n == 1:
                return nums[start_index]

            right_1, right_2, right_3 = nums[end_index - 1], nums[end_index], 0

            for i in range(end_index - 2, start_index - 1, -1):
                right_1, right_2, right_3 = max(right_2, right_3) + nums[i], right_1, right_2

            return max(right_1, right_2)
        return max(robNoneCircle(1, len(nums) - 1), robNoneCircle(0, len(nums) - 2))
# @lc code=end

