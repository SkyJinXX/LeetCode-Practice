#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stk = []
        if root:
            stk.append(root)
        
        while stk:
            node = stk.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        
        return root
# @lc code=end

