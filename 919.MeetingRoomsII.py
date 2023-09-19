from typing import (
    List,
)
from lintcode import (
    Interval,
)
import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    # put all intervals onto timeline axis
    def min_meeting_rooms(self, intervals: List[Interval]) -> int: 

        timeline = []
        for interval in intervals:
            timeline.append((interval.start, 1))
            timeline.append((interval.end, -1))
        timeline.sort()

        count, max_count = 0, 0
        for t in timeline:
            count += t[1]
            max_count = max(count, max_count)

        return max_count

    # my solution, using heapq
    def min_meeting_rooms(self, intervals: List[Interval]) -> int: 
        intervals.sort(key= lambda interval: (interval.start, interval.end))
        min_heap = [-1]

        for interval in intervals:
            if interval.start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)


        return len(min_heap)
