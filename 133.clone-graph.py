#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node': # iterative version（better)
        if not node:
            return None
        dic = dict()
        stk = [node]
        dic[node] = Node(node.val) # 第一个节点的part1
        while stk:
            current_node = stk.pop()
            copied_crt_node = dic[current_node]
            
            # 当前节点的part2 and part3: 让当前节点的邻居也生成克隆；把线连到邻居身上
            for neighbor in current_node.neighbors:
                if neighbor in dic:
                    copied_neighbor_node = dic[neighbor]
                else:
                    copied_neighbor_node = Node(neighbor.val) # 邻居的part1：克隆自己
                    dic[neighbor] = copied_neighbor_node
                    stk.append(neighbor)
                copied_crt_node.neighbors.append(copied_neighbor_node)
            

        return dic[node]
    def cloneGraph(self, node: 'Node') -> 'Node': # recursive version（better)
        if not node:
            return None

        dic = dict()
        def cloneNode(current_node):
            if current_node in dic:
                return dic[current_node]
            
            copied_crt_node = Node(current_node.val)
            dic[current_node] = copied_crt_node

            for neighbor in current_node.neighbors:
                copied_crt_node.neighbors.append(cloneNode(neighbor))
            
            return copied_crt_node

        cloneNode(node)

        return dic[node]

    def cloneGraph(self, node: 'Node') -> 'Node': # recursive version
        if not node:
            return None

        dic = dict()
        def helper(current_node, copied_pre_node):
            # clone current node and it's neighbors
            if current_node in dic:
                copied_crt_node = dic[current_node]
            else:
                copied_crt_node = Node(current_node.val)
                dic[current_node] = copied_crt_node
                for neighbor in current_node.neighbors:
                    helper(neighbor, copied_crt_node)

            # add connection with previous copied node
            copied_pre_node.neighbors.append(copied_crt_node)

        helper(node, Node())

        return dic[node]

    # def cloneGraph(self, node: 'Node') -> 'Node': # iterative
    #     if not node:
    #         return None
    #     dic = dict()
    #     stk = [(node, None)]
    #     while stk:
    #         current_node, copied_pre_node = stk.pop()

    #         # clone current node and it's neighbors
    #         if current_node in dic:
    #             copied_crt_node = dic[current_node]
    #         else:
    #             copied_crt_node = Node(current_node.val)
    #             dic[current_node] = copied_crt_node
    #             for neighbor in current_node.neighbors:
    #                 # if not copied_pre_node or neighbor.val != copied_pre_node.val: # why can't I connect two direction together?
    #                 #     stk.append((neighbor, copied_crt_node))
    #                 stk.append((neighbor, copied_crt_node))

    #         # add connection with previous copied node
    #         if copied_pre_node:
    #             # copied_crt_node.neighbors.append(copied_pre_node)
    #             copied_pre_node.neighbors.append(copied_crt_node)

    #     return dic[node]
            
# @lc code=end

