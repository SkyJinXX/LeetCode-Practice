#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums, n = deque(nums), len(nums)
        temp = []
        res = []
        def helper(last_not_chosen_number):
            if len(temp) == n:
                res.append(temp[:])
                return
            if nums[0] == last_not_chosen_number:
                return # return what?
            
            # choose the head
            temp.append(nums.popleft())
            helper(None) # core
            nums.appendleft(temp.pop())

            # not choose the head
            nums.append(nums.popleft())
            helper(last_not_chosen_number if last_not_chosen_number != None else nums[-1])
            nums.appendleft(nums.pop())
        
        helper(None)

        return res


        
# @lc code=end

