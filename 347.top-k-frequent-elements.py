#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return nums

        dic = {}
        lst = [[] for i in range(len(nums))]
        # lst = [None] * len(nums)

        # 统计数量
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        # 放入桶里
        for i in dic:
            lst[dic[i] - 1].append(i)

        # current_order = 0
        res = []
        # 输出
        for i in range(len(lst) - 1, -1, -1):
            if len(res) >= k:
                return res
            if len(lst[i]) != 0:
                res.extend(lst[i])
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    print(s.topKFrequent(nums, k)) 
            
        
# @lc code=end

