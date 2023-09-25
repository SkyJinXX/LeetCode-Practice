#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, l = 0, len(nums)
        
        while i < l:
            if nums[i] == val:
                for j in range(i, l - 1):
                    nums[j] = nums[j + 1]
                i -= 1
                l -= 1
            i += 1
        
        return l
# @lc code=end

