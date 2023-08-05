#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
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
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = MinHeap()
        self.k = k

        for i in range(min(k, len(nums))):
            self.min_heap.push(nums[i])
        for i in range(k, len(nums)):
            self.min_heap.push(nums[i])
            self.min_heap.pop()


    def add(self, val: int) -> int: 
        if self.min_heap.getLength() == self.k and val <= self.min_heap.getHeapTop():
            return self.min_heap.getHeapTop()

        self.min_heap.push(val)
        if self.min_heap.getLength() > self.k:
            self.min_heap.pop()
        return self.min_heap.getHeapTop()
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

