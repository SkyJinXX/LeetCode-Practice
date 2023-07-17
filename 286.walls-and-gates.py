#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        m, n = len(rooms), len(rooms[0])
        dq = deque()
        for row in range(m): # find all gates
            for column in range(n):
                if rooms[row][column] == 0:
                    dq.append((row, column))
        
        distance = 0
        while dq: # BFS(more time efficient than DFS, because BFS can avoid some search), only search and update the cells whose value is greater than the distance
            distance += 1
            for _ in range(len(dq)):
                row, column = dq.popleft()
                for next_row, next_column in ((row, column + 1), (row + 1, column), (row, column - 1), (row - 1, column)):
                    if -1 < next_row < m and -1 < next_column < n and distance < rooms[next_row][next_column]:
                        rooms[next_row][next_column] = distance
                        dq.append((next_row, next_column))


# @lc code=end

