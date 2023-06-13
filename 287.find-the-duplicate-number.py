#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        new_slow = 0
        while True:
            new_slow = nums[new_slow]
            slow = nums[slow]
            if slow == new_slow:
                return slow
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    # print(s.findDuplicate([1,3,4,2,2]))
    print(s.findDuplicate([3,1,3,4,2]))
