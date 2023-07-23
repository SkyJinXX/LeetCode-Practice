#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def helper(n: int):
            if n < 0:
                return 0
            elif n == 0:
                return 1
            else:
                return helper(n - 1)  + helper(n - 2)

        return helper(n)
# @lc code=end

