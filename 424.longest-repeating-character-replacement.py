#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        L = 0
        R = 0
        # current_length = 0
        max_freq = 0
        dic = {}

        while R < len(s):
            if s[R] not in dic:
                dic[s[R]] = 1
            else:
                dic[s[R]] += 1
            max_freq = max(max_freq, dic[s[R]])
            current_length = R - L + 1
            if current_length - max_freq <= k:
                # max_length = max(max_length, current_length)
                max_length = current_length
                R += 1
            else:
                dic[s[L]] -= 1
                L += 1

                R += 1
        
        return max_length
                
                
# @lc code=end

