#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    # pros: 可以只管把next_target丢给下一个递归函数
    # cons: 多了return True/False，稍微有点诡异吧？
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]: 
        candidates.sort()
        n = len(candidates)
        temp = []
        res = []
        def helper(target: int, startIndex: int) -> bool:
            if target == 0:
                res.append(temp[:])
                return True
            elif target < 0:
                return True


            # last_used = None

            for i in range(startIndex, n):
                # if candidates[i] == last_used: # we can determine whether to skip directly without `last_used` variable
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue

                next_target = target - candidates[i]
                temp.append(candidates[i])

                shouldBreak = helper(next_target, i + 1) 

                # last_used = candidates[i]
                temp.pop()
                
                if shouldBreak:
                    break
            
            return False



        helper(target, 0)
        return res
    # cons: 不能直接把next_target丢给下一个函数，要自己再处理一下。而且还分两部分判断next_target >0 or <=0
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        temp = []
        res = []
        def helper(target: int, startIndex: int):
            last_used = None

            for i in range(startIndex, n):
                if candidates[i] == last_used:
                    continue

                next_target = target - candidates[i]
                temp.append(candidates[i])

                if next_target > 0:
                    helper(next_target, i + 1)
                elif next_target == 0:
                    res.append(temp[:])

                last_used = candidates[i]
                temp.pop()
                
                if next_target <= 0:
                    break



        helper(target, 0)
        return res
# @lc code=end

