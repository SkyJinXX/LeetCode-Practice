#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def maxContribution(root) -> int:
            nonlocal res
            if not root:
                return 0

            max_ctbt_left_subtree = maxContribution(root.left)
            max_ctbt_right_subtree = maxContribution(root.right)

            res = max(res, root.val + max(max_ctbt_left_subtree, 0) + max(max_ctbt_right_subtree, 0)) # 明修栈道，暗度陈仓，夹带私货

            return root.val + max(max_ctbt_left_subtree, max_ctbt_right_subtree, 0)
        
        maxContribution(root)

        return res
# @lc code=end

