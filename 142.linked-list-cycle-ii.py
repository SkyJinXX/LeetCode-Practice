#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # let two pointers run util they meet or to the end of the list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # why not put this logics after "while"? because in the first loop, they are in the same place.
                break
        
        if not fast or not fast.next: # if no cycle
            return None
        
        new_slow = head
        while slow != new_slow:
            slow = slow.next
            new_slow = new_slow.next
        
        return new_slow


# @lc code=end

