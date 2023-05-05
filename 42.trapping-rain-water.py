#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        sum_area = 0
        pools = []
        left_pointer = 0
        right_pointer = n - 1

        if n < 3:  # 最少得三个（也就是[1, 0, 1]）才能聚水
            return sum_area

        # find all pool from left to right
        mode = 0  # 0: 试图找到第一个下降的点。 1：试图找到最近的一个>=左边柱子高度的柱子
        left_pillar = None
        right_pillar = None
        for i in range(1, n):
            if mode == 0:
                if height[i - 1] > height[i]:
                    left_pillar = i - 1
                    mode = 1
            else:
                if height[i] >= height[left_pillar]:
                    right_pillar = i
                    left_pointer = right_pillar
                    pools.append((left_pillar, right_pillar))

                    mode = 0
                    left_pillar = None
                    right_pillar = None

        # find all pool from right to left
        mode = 0  # 0: 试图找到第一个下降的点。 1：试图找到最近的一个>=左边柱子高度的柱子
        left_pillar = None
        right_pillar = None
        for i in range(n - 2, left_pointer -1, -1):
            if mode == 0:
                if height[i+1] > height[i]:
                    right_pillar = i + 1
                    mode = 1
            else:
                if height[i] >= height[right_pillar]:
                    left_pillar = i
                    right_pointer = left_pillar
                    pools.append((left_pillar, right_pillar))

                    mode = 0
                    left_pillar = None
                    right_pillar = None
        
        # calculate area
        for pool in pools:
            abs_height = min(height[pool[0]], height[pool[1]])
            for i in range(pool[0] + 1, pool[1]):
                sum_area += (abs_height - height[i])

        return sum_area

# if __name__ == "__main__":
#     s = Solution()
#     height = [4,2,0,3,2,5]
#     print(s.trap(height)) 
# @lc code=end
