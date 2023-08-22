#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = [float('-inf')]
        self.max_heap = [float('-inf')]
        self.isEven = True

    def addNum(self, num: int) -> None:
        self.isEven = not self.isEven # the total number of data stream after addNum
        if self.isEven:
            # push to min_heap
            another_possible_num = float('-inf')
            if len(self.max_heap) > 1:
                another_possible_num = max(-self.max_heap[1], -self.max_heap[2] if len(self.max_heap) > 2 else float('-inf'))
            heapq.heappush(self.min_heap, max(num, another_possible_num))

            # push to max_heap
            another_possible_num = float('inf')
            if len(self.min_heap) > 1:
                another_possible_num = min(self.min_heap[1], self.min_heap[2] if len(self.min_heap) > 2 else float('inf'))
            heapq.heappush(self.max_heap, -min(num, another_possible_num))
        else:
            heapq.heappush(self.min_heap, num)
            heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -num)
            heapq.heappop(self.max_heap)
        
        # print(self.min_heap)
        # print([-v for v in self.max_heap])
            

    def findMedian(self) -> float:
        if self.isEven:
            return (self.min_heap[0] + min(self.min_heap[1], self.min_heap[2] if len(self.min_heap) > 2 else float('inf'))) / 2
        else:
            return self.min_heap[0]
# @lc code=end

