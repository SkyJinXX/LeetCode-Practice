#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        st = {'+': lambda a, b: a+b,
              '-': lambda a, b: a - b,
              '*': lambda a, b: a * b,
              '/': lambda a, b: int(a/b)}
        for token in tokens:
            if token in st:
                operand_2 = stk.pop()
                operand_1 = stk.pop()
                stk.append(st[token](operand_1,operand_2))
            else:
                stk.append(int(token))

        return stk[0]

# @lc code=end
