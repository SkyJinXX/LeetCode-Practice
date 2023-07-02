#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST_solved_when_input(self, root: Optional[TreeNode]) -> bool:
        stk = [(root, float('-inf'), float('inf'))]

        while stk:
            node, min_boundary, max_boundary = stk.pop()
            if node.val <= min_boundary or node.val >= max_boundary:
                return False
            if node.left:
                stk.append((node.left, min_boundary, node.val))
            if node.right:
                stk.append((node.right, node.val, max_boundary))

        return True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stk = []
        crt = root
        pre_output = float('-inf')

        while stk or crt:
            while crt:
                stk.append(crt)
                crt = crt.left
            node = stk.pop() # 唯一能输出的就是中间的节点，不管先序后序还是中序
            if pre_output >= node.val:
                return False 
            pre_output = node.val
            crt = node.right

        return True
# @lc code=end

