#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool: # 1-D memo
        s = sum(nums)
        n = len(nums)
        if s % 2 != 0:
            return False
        
        target = s // 2
        if max(nums) > target:
            return False


        memo = [False] * (target + 1) 

        memo[nums[0]] = True
        for i in range(1, n):
            for j in range(target, -1, -1): # we have to reverse traversal order. for example: [2,2,3,5]， if don't reverse, because memo[2] == True, memo[4] = True; then because memo[4] == True, memo[6] = True
                if memo[j] and (j + nums[i] <= target):
                        memo[j + nums[i]] = True
        
        return memo[target]
    def canPartition(self, nums: List[int]) -> bool: # 2-D memo
        s = sum(nums)
        n = len(nums)
        if s % 2 != 0:
            return False
        
        target = s // 2
        if max(nums) > target:
            return False


        memo = [[False] * (target + 1) for _ in range(n)] # memo[i] indicates the numbers that nums[0:i + 1] can sum to

        memo[0][nums[0]] = True
        for i in range(1, n):
            for j in range(target + 1):
                if memo[i - 1][j]:
                    memo[i][j] = True
                    if j + nums[i] <= target:
                        memo[i][j + nums[i]] = True
        
        return memo[n - 1][target]

# @lc code=end

