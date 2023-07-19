#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
#[[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]
class UnionFind:
    def __init__(self, length):
        self.parent = [i for i in range(length)]
    def union(self, x: int, y: int) -> bool:
        root_of_x = self.findRootOf(x)
        root_of_y = self.findRootOf(y)
        if root_of_x == root_of_y:
            return False
        else:
            self.parent[root_of_x] = root_of_y
            return True
    def findRootOf(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.findRootOf(self.parent[x])
            return self.parent[x]
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1) # "+1" because "n nodes labeled from 1 to n"

        for x, y in edges:
            if not uf.union(x, y):
                return [x, y]

# @lc code=end

