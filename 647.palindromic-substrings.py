#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def countPalindromeByCore(j: int, k: int) -> int: # can't ensure s[j:k+1] is a valid core, so we have to check the core first
            sub_count = 0
            while j > -1 and k < len(s) and s[j] == s[k]:
                j = j - 1
                k = k + 1
                sub_count += 1
            return sub_count

        for i in range(len(s)):
            # sigle core
            count += countPalindromeByCore(i, i)

            # double core
            count += countPalindromeByCore(i, i + 1)

        return count
# @lc code=end

