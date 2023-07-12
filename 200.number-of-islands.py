#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
# [["1","1","1"],["0","1","0"],["1","1","1"]]
# class UnionHelper: # try using set
#     def __init__(self, grid):
#         m = len(grid)
#         n = len(grid[0])
#         self.sets = [-1] * (m * n)
#         self.num_of_sets = 0

#         for row in range(m):
#             for column in range(n):
#                 if grid[row][column] == '1':
#                     self.sets[row * n + column] = {row * n + column}
#                     self.num_of_sets += 1
        
#         for row in range(m):
#             for column in range(n):
#                 if grid[row][column] == '1':
#                     if row + 1 < m and grid[row + 1][column] == '1':
#                         self.union(row * n + column, (row + 1)*n + column)
#                     if column + 1 < n and grid[row][column + 1] == '1':
#                         self.union(row * n + column, row * n + column + 1)
#                     if column - 1 > -1 and grid[row][column - 1] == '1':
#                         self.union(row * n + column, row * n + column - 1)
#                     if row - 1 > -1 and grid[row - 1][column] == '1':
#                         self.union(row * n + column, (row - 1) * n + column)
#     def union(self, x, y):
#         if self.sets[x] != self.sets[y]:
#             print(self.sets[x], ', ', self.sets[y])
#             self.sets[x] = self.sets[x] | self.sets[y] # wrong, because this action only update the current position, many other positions are still using the previous set.
#             self.sets[y] = self.sets[x]
#             self.num_of_sets -= 1
class UnionHelper:
    def __init__(self, grid):
        m = len(grid)
        n = len(grid[0])
        self.parent = [-1] * (m * n)
        self.num_of_sets = 0

        for row in range(m):
            for column in range(n):
                if grid[row][column] == '1':
                    self.parent[row * n + column] = row * n + column
                    self.num_of_sets += 1
        
        for row in range(m):
            for column in range(n):
                if grid[row][column] == '1':
                    if row + 1 < m and grid[row + 1][column] == '1':
                        self.union(row * n + column, (row + 1)*n + column)
                    if column + 1 < n and grid[row][column + 1] == '1':
                        self.union(row * n + column, row * n + column + 1)
                    if column - 1 > -1 and grid[row][column - 1] == '1':
                        self.union(row * n + column, row * n + column - 1)
                    if row - 1 > -1 and grid[row - 1][column] == '1':
                        self.union(row * n + column, (row - 1) * n + column)
    def findRootOf(self, current):
        if self.parent[current] == current:
            return current
        else:
            self.parent[current] = self.findRootOf(self.parent[current])
            return self.parent[current]
    def union(self, x, y):
        root_of_x = self.findRootOf(x)
        root_of_y = self.findRootOf(y)
        if root_of_x != root_of_y:
            self.parent[root_of_y] = root_of_x
            self.num_of_sets -= 1
class Solution:
    # DSU, search all the rocks first, then union rocks
    def numIslands(self, grid: List[List[str]]) -> int:
        uh = UnionHelper(grid) # create a helper which can help us union ajacent rocks to island 

        return uh.num_of_sets

    # DFS, when meet a single rock, remove all the rocks of the land(or tag all the rocks)
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     number_of_islands = 0
    #     m = len(grid)
    #     n = len(grid[0])
    #     def helper(row, column):
    #         grid[row][column] = '0'
    #         if row + 1 < m and grid[row + 1][column] == '1':
    #             helper(row + 1, column)
    #         if column + 1 < n and grid[row][column + 1] == '1':
    #             helper(row, column + 1)
    #         if column - 1 > -1 and grid[row][column - 1] == '1':
    #             helper(row, column - 1)
    #         if row - 1 > -1 and grid[row - 1][column] == '1':
    #             helper(row - 1, column)

    #     for row in range(m):
    #         for column in range(n):
    #             if grid[row][column] == '1':
    #                 number_of_islands += 1
    #                 helper(row, column)
        
    #     return number_of_islands
# @lc code=end

