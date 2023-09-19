#
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#

# @lc code=start
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort queries and intervals
        sorted_queries = []
        for i, query in enumerate(queries):
            sorted_queries.append((query, i))
        sorted_queries.sort()
        intervals.sort()

        pq = [] # priority_queue to find min interval
        ans = [-1] * len(queries) # answer, default is -1 meaning not existing answer

        j = 0
        for query, i in sorted_queries: # iterate every query
            while j < len(intervals) and intervals[j][0] <= query: # collect all intervals that left_border meet the requirement
                heapq.heappush(pq, (intervals[j][1] - intervals[j][0] + 1, intervals[j][1]))
                j += 1
            while pq and pq[0][1] < query: # delete the top interval element of the min-heap, whose right_border doesn't meet the requirement
                heapq.heappop(pq)
            if pq:
                ans[i] = pq[0][0]
        
        return ans

# @lc code=end

