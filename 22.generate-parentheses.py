#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        st = []
        st.append(('', n, n, 0))

        while st:
            result, left_remain, right_remain, left_to_pair = st.pop()
            if not left_remain and not right_remain:
                results.append(result)

            if left_remain:
                st.append((result + '(', left_remain - 1, right_remain, left_to_pair + 1))
            if left_to_pair: # if left_to_pair, then left_to_pair only contains '(', and right must remains
                st.append((result + ')', left_remain, right_remain - 1, left_to_pair - 1))

        return results
# @lc code=end

# if __name__ == "__main__":
#     s = Solution()
#     print(s.generateParenthesis(3)) 