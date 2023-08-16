#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq
class MinHeap:
    def __init__(self):
        self.heap = []
    def push(self, val:int):
        self.heap.append(val)
        length = len(self.heap)

        child_index = length - 1
        parent_index = (child_index + 1) // 2 - 1
        while parent_index > -1 and self.heap[parent_index] > self.heap[child_index]:
            self.heap[parent_index], self.heap[child_index] = self.heap[child_index], self.heap[parent_index]
            child_index = parent_index
            parent_index = (child_index + 1) // 2 - 1
        # print(val, self.heap)
    def pop(self):
        self.heap[0] = self.heap.pop()
        length = len(self.heap)

        parent_index = 0
        left_child = parent_index * 2 + 1
        right_child = parent_index * 2 + 2
        while left_child < length:
            right_child = right_child if right_child < length else left_child
            if self.heap[parent_index] > self.heap[left_child] or self.heap[parent_index] > self.heap[right_child]:
                if self.heap[left_child] < self.heap[right_child]:
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

    def getHeapTop(self) -> int:
        return self.heap[0]
    def getLength(self) -> int:
        return len(self.heap)
class Solution:
    # using Heapq module
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for i in range(min(k, len(nums))):
            heapq.heappush(min_heap, nums[i])
        for i in range(k, len(nums)):
            heapq.heappushpop(min_heap, nums[i])
        
        return min_heap[0]

    # using custom MinHeap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = MinHeap()

        for i in range(min(k, len(nums))):
            min_heap.push(nums[i])
        for i in range(k, len(nums)):
            min_heap.push(nums[i])
            min_heap.pop()
        
        return min_heap.getHeapTop()
# @lc code=end

