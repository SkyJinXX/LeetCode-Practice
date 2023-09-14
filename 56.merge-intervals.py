#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start_crt, end_crt = intervals[0]

        for start_i, end_i in intervals:
            if end_crt < start_i:
                res.append([start_crt, end_crt])
                start_crt, end_crt = start_i, end_i
            else:
                start_crt = min(start_crt, start_i)
                end_crt = max(end_crt, end_i)
        res.append([start_crt, end_crt])

        return res
# @lc code=end

