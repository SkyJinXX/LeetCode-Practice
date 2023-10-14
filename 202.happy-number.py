#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def calculateHappy(n) -> int:
            res = 0
            while n:
                n, remainer = divmod(n, 10)
                res += remainer ** 2

            return res

        st = set()
        crt_n = n
        while crt_n not in st:
            if crt_n == 1:
                return True
            else:
                st.add(crt_n)
                crt_n = calculateHappy(crt_n)
        return False
        
# @lc code=end

