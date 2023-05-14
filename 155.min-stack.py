#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

        
    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.main_stack.pop()
        if val == self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[len(self.main_stack) - 1]

    def getMin(self) -> int:
        return self.min_stack[len(self.min_stack) - 1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

