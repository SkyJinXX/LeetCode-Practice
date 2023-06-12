#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # initiate parameters
        crt_sum = l1.val + l2.val
        l3 = ListNode(crt_sum % 10)
        v0 = crt_sum // 10
        l1_crt, l2_crt, l3_crt = l1.next, l2.next, l3

        # main part
        while l1_crt or l2_crt:
            v1 = l1_crt.val if l1_crt else 0
            v2 = l2_crt.val if l2_crt else 0

            crt_sum = v1+v2+v0
            l3_crt.next = ListNode(crt_sum % 10)
            v0 = crt_sum // 10

            if l1_crt:
                l1_crt = l1_crt.next
            if l2_crt:
                l2_crt = l2_crt.next
            l3_crt = l3_crt.next
        # process the remainer
        if v0:
            l3_crt.next = ListNode(v0)
        
        return l3

# @lc code=end

