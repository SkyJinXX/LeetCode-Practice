#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # stk = []
        last_head
        count = 0
        crt = head
        while crt:
            count += 1
            if count == 1:
                last_head = crt
            elif count == k:
                last_head = None
                count = 0
            
            crt 

# @lc code=end

