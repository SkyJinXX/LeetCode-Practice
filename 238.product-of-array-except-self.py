#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
# from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(n):
            if i == 0:
                continue
            else:
                res[i] = res[i-1] * nums[i - 1]

        
        multiplier = 1
        for i in range(n-1, -1, -1): 
            res[i] = res[i] * multiplier
            multiplier *= nums[i]

        return res
# @lc code=end

# if __name__ == "__main__":
#     s = Solution()
#     nums = [1,2,3,4]
#     print(s.productExceptSelf(nums)) 