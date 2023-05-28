#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        # we can add a "if" when first run, to exclude some situation. 
        if nums[L] > nums[R]:
            if target < nums[L] and target > nums[R]:
                return -1
        else:
            if target > nums[R] or target < nums[L]:
                return -1

        while L <= R:
            M = L + (R - L) // 2
            if nums[M] == target:
                return M
            elif nums[L] > nums[R]: # unnormal binary search. There are two ascending part.
                if nums[M] >= nums[L]: # M is in the left part
                    if target <= nums[R] or target > nums[M]:
                        L = M + 1
                    else:
                        R = M - 1
                else: # M is in the right part
                    if target <= nums[R] and target > nums[M]:
                        L = M + 1
                    else:
                        R = M - 1
            else: # nomal binary search
                if nums[M] < target:
                    L = M + 1
                else:
                    R = M - 1
        
        return -1
# @lc code=end

