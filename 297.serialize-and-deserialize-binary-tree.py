#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        stk = [root]
        output = []

        while stk:
            node = stk.pop()
            if not node:
                output.append('N')
            else:
                output.append(str(node.val))
                stk.append(node.right)
                stk.append(node.left)
        
        return ','.join(output)
        

    def deserialize(self, data):
        data = data.split(',')
        
        direction = 'left'
        dummy = TreeNode(None)
        crt = dummy
        stk = [dummy]

        for i in range(len(data)):
            if data[i] == 'N':
                if direction == 'left':
                    # node.left = None
                    direction = 'right'
                crt = stk.pop() # try the right side of the popped node
            else:
                setattr(crt, direction, TreeNode(int(data[i])))
                crt = getattr(crt, direction)
                stk.append(crt)

                direction = 'left'

        return dummy.left

                

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

