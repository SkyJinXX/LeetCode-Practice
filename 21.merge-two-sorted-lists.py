#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # only list1=[] or  only list2=[] or both =[]
        if not list1:
            return list2
        elif not list2:
            return list1

        pre = None
        node_in_list1 = list1
        node_in_list2 = list2
        head = None

        while node_in_list1 and node_in_list2:
            if node_in_list1.val <= node_in_list2.val:
                crt = node_in_list1
                node_in_list1 = node_in_list1.next
            else:
                crt = node_in_list2
                node_in_list2 = node_in_list2.next
            
            if pre:
                pre.next = crt
            else:
                head = crt
            pre = crt

        if node_in_list1:
            pre.next = node_in_list1
        elif node_in_list2:
            pre.next = node_in_list2

        return head

        

# @lc code=end

