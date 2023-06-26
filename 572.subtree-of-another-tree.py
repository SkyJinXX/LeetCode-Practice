#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from typing import List
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def treeToArray(root: Optional[TreeNode]) -> Optional[TreeNode]:
            stk = [root]
            res = []
            while stk:
                node = stk.pop()
                res.append(node.val if node else None)
                if node:
                    stk.append(node.right)
                    stk.append(node.left)
            return res
        def isPatternInArray(pattern: list, arr: list) -> bool:
            def generateSuffix(pattern: list) -> list: # my suffix_arr equals to other's next_arr, suffix is easier to understand for me
                suffix_arr = [0] * len(pattern)

                j, k = 0, 1
                while k < len(pattern):
                    if pattern[k] == pattern[j]: # if we can extend the suffix(and prefix)
                        suffix_arr[k] = j + 1
                        j += 1
                        k += 1
                    elif j > 0: # if we can't extend the suffix(and prefix), we choose to shorten suffix(and prefix) 
                        j = suffix_arr[j - 1] 
                    else: # if we can't extend the suffix(and prefix) and can't shorten suffix(and prefix), suffix_arr[k] = 0
                        k += 1

                return suffix_arr

            suffix_arr = generateSuffix(pattern)
            print('suffix_arr:', suffix_arr)
            j, k = 0, 0
            while j < len(arr):
                if arr[j] == pattern[k]:
                    j += 1
                    k += 1
                    if k == len(pattern):
                        return True
                elif k > 0:
                    k = suffix_arr[k - 1]
                else:
                    j += 1

            return False

        root_arr = treeToArray(root)
        subRoot_arr = treeToArray(subRoot)
        print(root_arr)
        print(subRoot_arr)

        return isPatternInArray(subRoot_arr, root_arr)
# @lc code=end

