#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # stk = [(p, q)] # if we add "None" node to stack too, then this expression is OK
        stk_p = [p]
        stk_q = [q]

        while stk_p and stk_q:
            node_p = stk_p.pop()
            node_q = stk_q.pop()

            if not node_p or not node_q:
                if node_p != node_q:
                    return False
                continue

            if node_p.val != node_q.val:
                return False
            
            stk_p.append(node_p.left)
            stk_p.append(node_p.right)
            stk_q.append(node_q.left)
            stk_q.append(node_q.right)
        
        return True

# @lc code=end

