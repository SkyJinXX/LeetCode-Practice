#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stk = []
        num_good_nodes = 0
        if root:
            stk.append((root,root.val))
        
        while stk:
            node, max_ancestor = stk.pop()
            if node.val >= max_ancestor:
                num_good_nodes += 1
                print(node.val, max_ancestor)
                max_ancestor = node.val
            if node.left:
                stk.append((node.left, max_ancestor))
            if node.right:
                stk.append((node.right, max_ancestor))
        
        return num_good_nodes
        
# @lc code=end

