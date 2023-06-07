#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter
from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        m = len(s)
        if n > m:
            return ""

        dic_t = {}
        for c in t:
            if c in dic_t:
                dic_t[c] += 1
            else:
                dic_t[c] = 1
        # dic_t = Counter(t) # more concise

        virtual_length = 0 # for example, t = "ABC“ substring"ABBDE", virtual_length = 2, only 1 'A' and 1 'B' will be counted
        L, R = 0, 0
        dic_try = {}
        minimum_substring = ""
        chance = m
        while R < m:
            if chance:
                if virtual_length == 0: # L and R jump together
                    if s[R] in dic_t:
                        dic_try[s[R]] = 1
                        virtual_length += 1
                        if virtual_length == n:
                            minimum_substring = s[L:R + 1]
                            chance = 0
                    else:
                        L += 1
                else: # only R jump
                    if s[R] in dic_t and (s[R] not in dic_try or dic_try[s[R]] < dic_t[s[R]]): # s[R] is not redundant
                        if s[R] not in dic_try:
                            dic_try[s[R]] = 1
                        else:
                            dic_try[s[R]] += 1
                        virtual_length += 1
                        if virtual_length == n:
                            minimum_substring = s[L:R + 1]
                            chance = 0
                            continue # avoid R += 1
                    else: # for redundant chars
                        if s[R] in dic_try:
                            dic_try[s[R]] += 1
                        chance -= 1
                        if not chance:
                            continue # avoid R += 1, because "if not chance" require R not move

                R += 1
            else: # get more chance by deleting redundant elements
                while L <= R and (not chance or (s[L] not in dic_t or (dic_try[s[L]] > dic_t[s[L]]))): # stop loop when L>=R or  (chance > 0 and s[L] is not redundant char)
                    if s[L] in dic_t and dic_try[s[L]] <= dic_t[s[L]]: # if s[L] is not redundant
                        dic_try[s[L]] -= 1
                        virtual_length -= 1
                    else:
                        if s[L] in dic_try:
                            dic_try[s[L]] -= 1
                        chance += 1
                        if virtual_length == n:
                            minimum_substring = s[L + 1:R + 1]
                            chance = 0
                    L += 1
                
                if chance == 0:
                    return minimum_substring
                else:
                    R += 1
                    
        return minimum_substring


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    # print(s.minWindow("cabwefgewcwaefgcf","cae")) 
    # print(s.minWindow("a","a")) 
    # print(s.minWindow("bba","ab")) 
    print(s.minWindow("adobecodebancbbcaa","abc")) 
