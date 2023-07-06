#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
# [7,3,2]\n18
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # impossible_target = set() # 前面不行不代表后面不行
        candidates.sort()
        def findAllCombinationForTarget(target, startIndex):
            # if target in impossible_target:
            #     return []
            
            res = []
            for i in range(startIndex, len(candidates)):
                next_target = target - candidates[i]
                sub_res = []
                if next_target > 0:
                    sub_res = findAllCombinationForTarget(next_target, i)
                elif next_target == 0:
                    sub_res = [[]]
                else:
                    break
                
                for lst in sub_res:
                    lst.append(candidates[i])
                    res.append(lst)
            
            # if not res:
            #     impossible_target.add(target)
            
            return res

        return findAllCombinationForTarget(target, 0)
# @lc code=end

