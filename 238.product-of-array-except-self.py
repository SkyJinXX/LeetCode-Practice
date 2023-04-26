#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lst_l = [1] * n
        lst_r = [1] * n

        for i in range(len(lst_l)):
            if i == 0:
                continue
            else:
                lst_l[i] = lst_l[i-1] * nums[i - 1]

        for i in range(len(lst_r)-1, -1, -1): 
            if i == len(lst_r) - 1:
                continue
            else:
                lst_r[i] = lst_r[i+1] * nums[i + 1]

        return [lst_l[i]*lst_r[i] for i in range(len(nums))] 
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4]
    print(s.productExceptSelf(nums)) 