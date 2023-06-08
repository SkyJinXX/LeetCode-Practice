#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        pre = head
        crt = head.next
        nxt = None
        
        head.next = None
        while crt:
            nxt = crt.next

            crt.next = pre
            # pre.next = None

            pre = crt
            crt = nxt
        head = pre

        return head
    def reverseList_high_space_complexity(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stk = []
        node = head
        while node:
            stk.append(node)
            node = node.next
        
        head = stk.pop()
        node = head
        while stk:
            node.next = stk[-1]
            node = stk.pop()
        
        node.next = None

        return head

# @lc code=end

