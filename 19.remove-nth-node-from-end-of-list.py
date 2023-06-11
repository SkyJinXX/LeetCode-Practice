#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = n - 1
        L, R = head, head

        # calculate distance_of_R
        distance_of_R = 0
        while distance_of_R < s:
            R = R.next
            distance_of_R += 1

        if not R.next: # special case: the node needed to remove is the head
            return head.next
        
        # move the line(L to R) to the end
        R = R.next # make L is the node left to the node to be removed
        while R.next:
            R = R.next
            L = L.next

        # remove the node right to L
        L.next = L.next.next
        
        return head
        
        
# @lc code=end

