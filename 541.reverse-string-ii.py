#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        def reverseByIndex(L: int, R: int):
            while L < R:
                s_list[L], s_list[R] = s_list[R], s_list[L]
                L += 1
                R -= 1
        
        L, R = 0, k - 1
        while R < len(s):
            reverseByIndex(L, R)
            L += 2 * k
            R += 2 * k
        if L < len(s):
            reverseByIndex(L, len(s) - 1)
        
        return ''.join(s_list)
class Solution: # less efficient in time and space
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        def reverseByIndex(text):
            L, R = 0, len(text) - 1
            while L < R:
                text[L], text[R] = text[R], text[L]
                L += 1
                R -= 1
            return text
        
        p = 0
        while p < len(s):
            s_list[p:p+k] = reverseByIndex(s_list[p:p+k])
            p += 2 * k
        
        return ''.join(s_list)
        
# @lc code=end

