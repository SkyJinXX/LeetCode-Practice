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
        # find the pre node of the last head which doesn't have to be reversed
        pre_of_last_head = ListNode(0, head)
        count = 0
        crt = head
        while crt:
            count += 1
            if count == k:
                pre_of_last_head = crt
                count = 0
            
            crt = crt.next
        
        # cut the list
        remainer = pre_of_last_head.next
        pre_of_last_head.next = None

        # reverse 
        dummy = ListNode(0, head)
        crt = dummy
        new_head = None
        pre_tail = None
        while crt.next:
            crt = crt.next
            sub_head = crt
            count = 1
            # sub_tail = crt
            while crt.next and count < k:
                # reverse
                # tmp = crt.next
                # crt.next = crt.next.next
                # tmp.next = sub_head
                # sub_head = tmp
                sub_head, crt.next.next, crt.next = crt.next, sub_head, crt.next.next
                # count++
                count += 1
            if not new_head:
                new_head = sub_head
            if pre_tail:
                pre_tail.next = sub_head
            pre_tail = crt
            print(new_head.val)
            count = 0
        
        # append the remainer
        crt.next = remainer

        return new_head

# @lc code=end

