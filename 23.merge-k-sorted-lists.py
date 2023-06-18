#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> Optional[ListNode]:
        # list1 is None or list2 is None
        if not list2:
            return list1
        elif not list1:
            list1 = list2
            return list1

        # initiate parameters
        if list1.val > list2.val:
            temp = list2.next
            list2.next = list1
            list1 = list2
            list2 = temp
        confirmed_pointer = list1
        crt1 = list1.next
        crt2 = list2

        # main part
        while crt1 and crt2:
            if crt1.val <= crt2.val:
                confirmed_pointer.next = crt1
                confirmed_pointer = confirmed_pointer.next
                crt1 = crt1.next
            else:
                confirmed_pointer.next = crt2
                crt2 = crt2.next
                confirmed_pointer = confirmed_pointer.next
                confirmed_pointer.next = None


        # process the remainer
        # before optimized
        # if crt2:
        #     confirmed_pointer.next = crt2
        # elif crt1:
        #     confirmed_pointer.next = crt1
        # after optimized
        confirmed_pointer.next = crt1 or crt2
        
        return list1
    def printList(self, head: List[Optional[ListNode]]):
        crt = head
        while crt:
            print(crt.val, '->')
            crt = crt.next
        print('---------------')
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        k = len(lists)
        i = 0
        T = 1
        while i+T < k: # we can simplify "i+T < k" to "T < k", because i always is 0, when loop begain
            while i+T < k: # how to merge two "while"?
                # print(i, i+T)
                # self.printList(self.merge2Lists(lists[i], lists[i+T]))
                lists[i] = self.merge2Lists(lists[i], lists[i+T])
                i += 2 * T
            T *= 2
            i = 0

        return lists[0]
# @lc code=end

