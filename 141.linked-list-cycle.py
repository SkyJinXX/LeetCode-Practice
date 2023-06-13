#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow_pointer = head
        fast_pointer = head.next
        while fast_pointer and fast_pointer.next:
            if slow_pointer == fast_pointer:
                return True
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return False
# @lc code=end

