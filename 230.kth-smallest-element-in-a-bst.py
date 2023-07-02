#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        crt = root
        count = 0

        while stk or crt:
            while crt:
                stk.append(crt)
                crt = crt.left
            node = stk.pop() # 唯一能输出的就是中间的节点，不管先序后序还是中序
            count += 1
            if count == k:
                return node.val 
            crt = node.right
# @lc code=end

