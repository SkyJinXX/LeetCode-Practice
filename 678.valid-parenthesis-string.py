#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        # check from left to right
        n_of_left_prth = 0
        for c in s:
            if c == '(' or c == '*':
                n_of_left_prth += 1
            else:
                n_of_left_prth -= 1
            if n_of_left_prth < 0:
                return False
        
        # check from left to right
        n_of_right_prth = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == ')' or c == '*':
                n_of_right_prth += 1
            else:
                n_of_right_prth -= 1
            if n_of_right_prth < 0:
                return False
        
        return True
# @lc code=end

