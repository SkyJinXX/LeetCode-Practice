#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        # impossible condition
        if sum(gas) - sum(cost) < 0: # when > 0, does it must have a solution?
            return -1
        
        start_point = 0
        sm = 0
        for i in range(n):
            sm = sm + gas[i] - cost[i]
            if sm < 0:
                start_point = i + 1
                sm = 0
        
        return start_point

        # while start_point < n:
        #     sm = 0
        #     for i in range(start_point, n):
        #         sm = sm + gas[i] - cost[i]
        #         if sm < 0:
        #             start_point = i + 1
        #             break
        #     if sm >= 0:
        #         break
        
        # return start_point

# @lc code=end

