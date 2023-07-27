#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_start, max_end = 0, 0

        def extendCore(j: int, k: int):
            while j > -1 and k < len(s) and s[j] == s[k]:
                j = j - 1
                k = k + 1
            return (j + 1, k - 1)

        for i in range(len(s)):
            # sigle core
            start, end = extendCore(i, i)
            if end - start > max_end - max_start:
                max_start = start
                max_end = end

            # double core
            start, end = extendCore(i, i + 1)
            if end - start > max_end - max_start:
                max_start = start
                max_end = end

        return s[max_start: max_end + 1]
# @lc code=end

