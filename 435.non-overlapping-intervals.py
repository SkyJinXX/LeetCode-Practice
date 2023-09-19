#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        times = -1

        start_last, end_last = intervals[0]
        for start_i, end_i in intervals:
            if start_i < end_last:
                times += 1
                end_last = min(end_last, end_i)
        
        return times
# @lc code=end

