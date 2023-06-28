#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        que = deque()
        if root: # because We don't want null node in the queue, because we don't need to output null node.
            que.append(root)
        while que:
            # temp = []
            for _ in range(len(que)):
                node = que.popleft()
                # temp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(node.val)
        
        return res
# @lc code=end

