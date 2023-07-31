#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True # '0' means the length from left to right

        for i in range(n):
            for j in range(i - 1, -2, -1):
                if dp[j + 1] and s[j + 1:i + 1] in word_set:
                    dp[i + 1] = True
                    break
        
        return dp[n]

# @lc code=end

