#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        pointer = root
        while True:
            if pointer.val > p.val and pointer.val > q.val:
                pointer = pointer.left
            elif pointer.val < p.val and pointer.val < q.val:
                pointer = pointer.right
            else: # (pointer.val == p.val and pointer.val == q.val) or (pointer.val > p.val and pointer.val < q.val) or (....) or (...)
                return pointer

        # res = root # 
        # has_find_p, has_find_q = False, False # 找到任意一个就可以退出了，所以没必要记录
        # pointer_for_p, pointer_for_q = root, root # 一旦他们有分歧，也就该退出了，所以没必要分2个。

        # 直接把下面6种情况排列组合一下，最后你会发现只有两种情况是可以继续的，其他情况都该直接return res

        # while not has_find_p and not has_find_q:
        #     # action for p
        #     if pointer_for_p.val == p.val:
        #         has_find_p = True
        #     elif pointer_for_p.val < p.val:
        #         pointer_for_p = pointer_for_p.right
        #     else:
        #         pointer_for_p = pointer_for_p.left

        #     # action for q
        #     if pointer_for_q.val == q.val:
        #         has_find_q = True
        #     elif pointer_for_q.val < q.val:
        #         pointer_for_q = pointer_for_q.right
        #     else:
        #         pointer_for_q = pointer_for_q.left
            
        #     # update res
        #     if pointer_for_p == pointer_for_q:
        #         res = pointer_for_p
        #     else:
        #         break

        # return res
# @lc code=end

