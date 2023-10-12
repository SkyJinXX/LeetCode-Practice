#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy1, dummy2 = ListNode(), ListNode(0, head)
        dummy1.next = dummy2

        pre, crt = dummy1, head
        while crt:
            if not crt.next:
                pre.next = crt
                break
            pre.next = crt.next
            crt.next.next, crt.next, pre, crt = crt, None, crt, crt.next.next

        return dummy1.next
# @lc code=end

