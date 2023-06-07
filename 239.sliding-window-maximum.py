#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        sticks = []
        L_sticks = 0
        
        L, R = 0, 0
        while R < k:
            while sticks and L_sticks != len(sticks) and nums[R] > sticks[-1]:
                sticks.pop()
            sticks.append(nums[R])
            R += 1
        
        # R -= 1 # offset
        res.append(sticks[L_sticks])

        while R < len(nums):
            # process L
            if nums[L] == sticks[L_sticks]:
                L_sticks += 1
            L += 1

            # process R
            while sticks and L_sticks != len(sticks) and nums[R] > sticks[-1]:
                sticks.pop()
            sticks.append(nums[R])

            res.append(sticks[L_sticks])
            R += 1

        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
    # print(s.maxSlidingWindow([1,-1],1))
    # print(s.maxSlidingWindow([7,2,4], 2))
