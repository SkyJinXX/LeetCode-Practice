#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        j_moved = False
        k_moved = False
        for i in range(len(nums) - 2):
            # 跳过重复的nums[i]
            if i - 1 >= 0 and nums[i - 1] == nums[i]: 
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                # i不变时，跳过重复的nums[j]/nums[k]
                if j_moved == True:
                    if nums[j] == nums[j - 1]:
                        j += 1
                        continue
                    else:
                        j_moved = False
                if k_moved == True:
                    if nums[k] == nums[k + 1]:
                        k -= 1
                        continue
                    else:
                        k_moved = False

                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    j_moved = True
                    k -= 1
                    k_moved = True
                elif nums[i] + nums[j] + nums[k] < 0:
                    j +=1 
                    j_moved = True
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    k_moved = True
            # i将要变了，j和k的移动就重置
            j_moved = False
            k_moved = False
        return result

# if __name__ == "__main__":
#     s = Solution()
#     nums = [-1,0,1,2,-1,-4]
#     print(s.threeSum(nums)) 

# @lc code=end

