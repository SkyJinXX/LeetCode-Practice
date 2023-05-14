#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        brackets = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in brackets:
                if not stack: 
                    return False
                elif stack[len(stack) - 1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
# @lc code=end

