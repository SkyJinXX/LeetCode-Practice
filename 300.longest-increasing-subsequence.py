#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: # O(n*logn)
        n = len(nums)
        tails = [nums[0]] # tails[0] means the min tail of a Increasing Subsequence with length 1

        for i in range(1, n):
            if nums[i] > tails[-1]:
                tails.append(nums[i])
            else:
                L, R = 0, len(tails) - 1
                while L <= R:
                    M = L + (R - L) // 2
                    if tails[M] == nums[i]:
                        break
                    elif tails[M] > nums[i]:
                        R = M - 1
                    else:
                        L = M + 1
                if L > R:
                    tails[L] = nums[i]
        
        return len(tails)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
# @lc code=end

