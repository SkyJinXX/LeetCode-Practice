#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        visited = set()
        dq = deque()
        dq.append((0, 0, 0))

        while dq:
            current_amount, min_numbers, start_index = dq.popleft()

            # skip visited amount
            if current_amount in visited:
                continue
            # store the amount has been visited
            visited.add(current_amount)

            if current_amount == amount:
                return min_numbers
            elif current_amount > amount:
                continue
                

            # ddd
            for i in range(start_index, len(coins)):
                dq.append((current_amount + coins[i], min_numbers + 1, i))
        
        return -1
# @lc code=end

