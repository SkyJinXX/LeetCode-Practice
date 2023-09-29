#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = deque()
        L, R = 0, len(nums) - 1
        while L <= R: 
            if abs(nums[L]) <= abs(nums[R]):
                res.appendleft(nums[R] ** 2)
                R -= 1
            else:
                res.appendleft(nums[L] ** 2)
                L += 1
        
        return res

    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [value * value for value in nums]
        elif nums[-1] <= 0:
            return [nums[i] * nums[i] for i in range(len(nums) - 1, -1, -1)]
        elif len(nums) == 1:
            return [nums[0] * nums[0]]
        
        for i in range(len(nums) - 1):
            if nums[i] < 0 and nums[i + 1] >= 0:
                neg_arrow, pos_arrow = i, i + 1

        res = []
        while neg_arrow >= 0 and pos_arrow < len(nums):
            if -nums[neg_arrow] > nums[pos_arrow]:
                res.append(nums[pos_arrow] * nums[pos_arrow])
                pos_arrow += 1
            else:
                res.append(nums[neg_arrow] * nums[neg_arrow])
                neg_arrow -= 1
        # print(neg_arrow, pos_arrow)
        if neg_arrow >= 0:
            for i in range(neg_arrow, -1, -1):
                res.append(nums[i] * nums[i])
        elif pos_arrow < len(nums):
            for i in range(pos_arrow, len(nums)):
                res.append(nums[i] * nums[i])

        return res

# @lc code=end

