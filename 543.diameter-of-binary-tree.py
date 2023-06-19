#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.longest_length = 0
    def depthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left_depth = self.depthOfBinaryTree(root.left) if root.left else 0
        right_depth = self.depthOfBinaryTree(root.right) if root.right else 0
        self.longest_length = max(self.longest_length, left_depth + right_depth) 
        return max(left_depth, right_depth) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        self.depthOfBinaryTree(root) # 夹带私货算法，看起来我在求二叉树深度，其实我在算longest_length
        return self.longest_length
# @lc code=end

