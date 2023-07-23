#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    # # 用“派任务”去理解递归：给2派发任务，把从你那个台阶往上走到所有台阶的min cost都给我算出来。然后2它说，我只能算出我自己的min cost，剩下的交给我的下一个台阶吧。
    # # 也可以理解为外部在控制：外部的一个人，对每层楼都计算一遍min cost。(但是外部控制的话，还是iterative比较好，递归用来解决内部矛盾更容易理解)
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     n = len(cost)
    #     memo = [-1] * (n + 1)
    #     memo[0], memo[1] = 0, 0
    #     # 
    #     def helper(floor): # calculate the min total cost to cu rrent floor, and 
    #         memo[floor] = min(memo[floor - 1] + cost[floor - 1], memo[floor - 2] + cost[floor - 2])
    #         if floor != n:
    #             helper(floor + 1)


    #     helper(2) 
    #     return memo[n]
    
    # 用外部控制去写一遍：外部的一个人，对每层楼都计算一遍min cost
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        pre_1_cost, pre_2_cost = 0, 0

        for crt_floor in range(2, n + 1):
            pre_1_cost, pre_2_cost = min(pre_1_cost + cost[crt_floor - 1], pre_2_cost + cost[crt_floor - 2]), pre_1_cost
        
        return pre_1_cost



    # 用“派任务”的递归写一遍：给某一个floor派任务，给我算出从-1层走到你那层的cost。
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @cache
        def helper(floor: int) -> int:
            if floor < -1:
                return float('inf')
            elif floor == -1:
                return 0
            else:
                if floor - 1 == -1 or floor - 2 == -1:
                    return 0
                return min(helper(floor - 1) + cost[floor - 1] if floor - 1 != -1 else 0, helper(floor - 2) + cost[floor - 2] if floor - 2 != -1 else 0)

        return helper(len(cost))

    # # 用“派任务”去理解递归：给某一个floor派任务，给我算出从你那层走到0层所需的最小cost。
    # # 比如一开始找了第n层，n可以把任务扔给n-1和n-2，让他们找出最小cost，然后你从中挑出最小的，然后再加上离开第n层所需的cost。
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     cost.append(0)

    #     @cache
    #     def helper(floor: int) -> int:
    #         if floor == 0:
    #             return 0
    #         elif floor < 0:
    #             return float('inf')
    #         else:
    #             return min(helper(floor - 1), helper(floor - 2)) + cost[floor - 1] # why cost[floor - 1]?


    #     return helper(len(cost))
# @lc code=end

