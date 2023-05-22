#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_boundary = 0
        right_boundary = len(nums) - 1

        while left_boundary <= right_boundary:
            middle = int((left_boundary + right_boundary) / 2)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right_boundary = middle - 1
            elif nums[middle] < target:
                left_boundary = middle + 1
        
        return -1
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    # print(s.largestRectangleArea([2,1,5,6,2,3])) 
    print(s.search([-1,0,3,5,9,12], 2)) 