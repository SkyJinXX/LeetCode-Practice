#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        new_head = Node(head.val)
        head.new = new_head

        new_crt = new_head
        old_crt = head
        while old_crt:
            if old_crt.next:
                if hasattr(old_crt.next,'new'):
                    new_crt.next = old_crt.next.new
                else:
                    new_crt.next = Node(old_crt.next.val)
                    old_crt.next.new = new_crt.next
            
            if old_crt.random:
                if hasattr(old_crt.random,'new'):
                    new_crt.random = old_crt.random.new
                else:
                    new_crt.random = Node(old_crt.random.val)
                    old_crt.random.new = new_crt.random
            
            # print(new_crt.val, new_crt.next.val if new_crt.next else 'None', new_crt.random.val if new_crt.random else 'None')
            old_crt = old_crt.next
            new_crt = new_crt.next
        
        return new_head
# @lc code=end

