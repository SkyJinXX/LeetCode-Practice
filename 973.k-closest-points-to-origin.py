#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
class MyMaxHeap:
    def __init__(self):
        self.heap = []
    def push(self, x: int, y: int):
        self.heap.append(((x, y), x * x + y * y))
        length = len(self.heap)

        child_index = length - 1
        parent_index = (child_index + 1) // 2 - 1
        while parent_index > -1 and self.heap[parent_index][1] < self.heap[child_index][1]:
            self.heap[parent_index], self.heap[child_index] = self.heap[child_index], self.heap[parent_index]
            child_index = parent_index
            parent_index = (child_index + 1) // 2 - 1
        # print(val, self.heap)
    def pop(self) -> int:
        if self.getLength() == 1:
            return self.heap.pop()
        
        popped_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        length = len(self.heap)

        parent_index = 0
        left_child = parent_index * 2 + 1
        right_child = parent_index * 2 + 2
        while left_child < length:
            right_child = right_child if right_child < length else left_child
            if self.heap[parent_index][1] < self.heap[left_child][1] or self.heap[parent_index][1] < self.heap[right_child][1]:
                if self.heap[left_child][1] > self.heap[right_child][1]:
                    self.heap[left_child], self.heap[parent_index] = self.heap[parent_index], self.heap[left_child]
                    parent_index = left_child
                    left_child = parent_index * 2 + 1
                    right_child = parent_index * 2 + 2
                else:
                    self.heap[right_child], self.heap[parent_index] = self.heap[parent_index], self.heap[right_child]
                    parent_index = right_child
                    left_child = parent_index * 2 + 1
                    right_child = parent_index * 2 + 2
            else:
                break
        
        return popped_value

    def getHeapTop(self) -> int:
        return self.heap[0]
    def getLength(self) -> int:
        return len(self.heap)
class Solution:
    # using myMaxheap
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     mh = MyMaxHeap()
    #     for i in range(k):
    #         mh.push(points[i][0], points[i][1])
    #     for i in range(k, len(points)):
    #         mh.push(points[i][0], points[i][1])
    #         mh.pop()
        
    #     return [[point[0], point[1]] for point, distance in mh.heap]

    # using heapq module
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for i in range(k):
            x, y = points[i]
            heapq.heappush(min_heap, (-x ** 2 - y ** 2, (x, y)))
        for i in range(k, len(points)):
            x, y = points[i]
            heapq.heappushpop(min_heap, (-x ** 2 - y ** 2, (x, y)))
        
        return [[point[0], point[1]] for distance, point  in min_heap]
# @lc code=end

