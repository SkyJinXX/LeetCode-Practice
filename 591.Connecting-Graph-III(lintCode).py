#
# @lc app=lintcode id=591 lang=python3
#
# [591] Connecting Graph III
#

# @lc code=start
class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.count = n
    
    def connect(self, a, b):
        root_of_a = self.findRootOf(a)
        root_of_b = self.findRootOf(b)
        if root_of_a != root_of_b:
            self.parent[root_of_a] = root_of_b
            self.count -= 1

    def findRootOf(self, x):
        if x == self.parent[x]:
            return x
        else:
            self.parent[x] = self.findRootOf(self.parent[x])
            return self.parent[x]

    """
    @return: An integer
    """
    def query(self):
        return self.count

# @lc code=end

