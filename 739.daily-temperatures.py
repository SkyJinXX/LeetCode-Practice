#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        st = []
        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:
                    former_temperature_index = st.pop()
                    result[former_temperature_index] = i - former_temperature_index
            st.append(i)

        return result
        
# @lc code=end

