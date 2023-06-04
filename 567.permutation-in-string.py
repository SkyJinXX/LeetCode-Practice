#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic_s1 = {}
        for c in s1: # how to code more elegant?
            if c in dic_s1:
                dic_s1[c] += 1
            else:
                dic_s1[c] = 1
        
        L, R = 0, 0
        dic_try = {}
        dic_try_length = 0
        while R < len(s2):
            if s2[R] in dic_s1: # if char in s1, we will check if we have add the same char to dic_try
                if s2[R] in dic_try: # if the char has already been added, there are two contidions
                    if dic_try[s2[R]] < dic_s1[s2[R]]: # 1. not meet the requirement in dic_s1
                        dic_try[s2[R]] += 1
                        dic_try_length += 1
                        if dic_try_length == len(s1):
                            return True
                    else: # 2. already meet the requrement, we have to cut the try_length from left
                        while s2[L] != s2[R]: # how to code more elegant?
                            dic_try[s2[L]] -= 1
                            dic_try_length -= 1
                            L += 1
                        dic_try[s2[L]] -= 1
                        dic_try_length -= 1
                        L += 1
                        dic_try[s2[R]] += 1
                        dic_try_length += 1 # this two line can offset their counterparts above. I keep them for readability
                else:
                    dic_try[s2[R]] = 1
                    dic_try_length += 1
                    if dic_try_length == len(s1):
                        return True
                R += 1
            else: # if char not in s1, we have to clear dic_try, then reset L, R
                dic_try = {}
                dic_try_length = 0
                L, R = R + 1, R + 1

        return False
# @lc code=end

