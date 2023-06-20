#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    class BalanceException(Exception):
        pass
    # def __init__(self):
    #     self.res = True
    def depthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left_depth = self.depthOfBinaryTree(root.left) + 1 if root.left else 0
        right_depth = self.depthOfBinaryTree(root.right) + 1 if root.right else 0
        if abs(left_depth - right_depth) > 1: # 也是夹带私货，函数名叫depthOfBinaryTree，其实主要是在计算是否balanced
            # self.res = False
            raise self.BalanceException
        return max(left_depth, right_depth)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        try:
            self.depthOfBinaryTree(root)
            return True
        except self.BalanceException:
            return False
        # return self.res
# @lc code=end

