class MaxHeap:
    def __init__(self):
        self.heap = []
    def push(self, val:int):
        self.heap.append(val)
        length = len(self.heap)

        child_index = length - 1
        parent_index = (child_index + 1) // 2 - 1
        while parent_index > -1 and self.heap[parent_index] < self.heap[child_index]:
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
            if self.heap[parent_index] < self.heap[left_child] or self.heap[parent_index] < self.heap[right_child]:
                if self.heap[left_child] > self.heap[right_child]:
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
    def lastStoneWeight(self, stones: List[int]) -> int:
        mh = MaxHeap()
        for stone in stones:
            mh.push(stone)
        
        while mh.getLength() > 1:
            first_largest = mh.pop()
            second_largest = mh.pop()
            if first_largest != second_largest:
                mh.push(first_largest - second_largest)
        
        return mh.getHeapTop() if mh.getLength() else 0