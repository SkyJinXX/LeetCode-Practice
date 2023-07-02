#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
        
        def recursiveBuildTree(pre_left: int, pre_right: int, in_left: int, in_right: int) -> Optional[TreeNode]:
            if pre_left > pre_right or in_left > in_right:
                return None

            root = TreeNode(preorder[pre_left])
            root_index_in_inorder = hashmap[root.val]

            root.left = recursiveBuildTree(pre_left + 1, pre_left + root_index_in_inorder - in_left, in_left, root_index_in_inorder - 1)
            root.right = recursiveBuildTree(pre_left + root_index_in_inorder - in_left + 1, pre_right, root_index_in_inorder + 1, in_right)
            return root
        return recursiveBuildTree(0, len(preorder) - 1, 0, len(preorder) - 1)
# @lc code=end

