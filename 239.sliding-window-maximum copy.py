#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        class Node:
            def __init__(self, data=None):
                self.data = data
                self.prev = None

        class reversedLinkedList:
            def __init__(self, data):
                self.end = Node(data)

            # def insert_before_node(self, node, data):
            #     new_node = Node(data)
            #     if node is None:
            #         return
            #     if node.prev is None:
            #         new_node.prev = None
            #         node.prev = new_node
            #         self.end = new_node
            #     else:
            #         new_node.prev = node.prev
            #         node.prev = new_node
            def insert_after_end(self, data):
                new_node = Node(data)
                new_node.prev = self.end
                self.end = new_node

            def insert_before_end(self, data):
                new_node = Node(data)
                if self.end.prev:
                    new_node.prev = self.end.prev
                self.end.prev = new_node
                
            def insert_before_second_end(self, data):
                new_node = Node(data)
                second_end = self.end.prev
                if second_end.prev:
                    new_node.prev = second_end.prev
                second_end.prev = new_node
            def remove_end(self):
                self.end = self.end.prev

            def print(self):
                current = self.end
                lst = []
                while current is not None:
                    lst.append(current.data)
                    current = current.prev
                print(lst[::-1])
                
        res = []
        rll = None # a reversedLinkedList
        
        L, R = 0, 0
        while R < k:
            if not rll:
                rll = reversedLinkedList(nums[R])
            elif not rll.end.prev:
                if nums[R] > rll.end.data:
                    rll.insert_after_end(nums[R])
                else:
                    rll.insert_before_end(nums[R])
            else:
                if nums[R] > rll.end.data:
                    rll.insert_after_end(nums[R])
                elif nums[R] > rll.end.prev.data:
                    rll.insert_before_end(nums[R])
                else:
                    rll.insert_before_second_end(nums[R])
            R += 1

        res.append(rll.end.data)

        # move the window
        # L += 1

        while R < len(nums):
            rll.print()

            # process nums[L]
            if nums[L] == rll.end.data:
                rll.remove_end()
            # else: add to a dictionary
            L += 1 

            # process nums[R]
            if not rll or not rll.end:
                rll = reversedLinkedList(nums[R])
            elif not rll.end.prev:
                if nums[R] > rll.end.data:
                    rll.insert_after_end(nums[R])
                else:
                    rll.insert_before_end(nums[R])
            else:
                if nums[R] > rll.end.data:
                    rll.insert_after_end(nums[R])
                elif nums[R] > rll.end.prev.data:
                    rll.insert_before_end(nums[R])
                else:
                    rll.insert_before_second_end(nums[R])

            res.append(rll.end.data)
            R += 1

        return res


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    # print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
    # print(s.maxSlidingWindow([1,-1],1))
    print(s.maxSlidingWindow([9,8,7,6,1,1,1,1], 4))
