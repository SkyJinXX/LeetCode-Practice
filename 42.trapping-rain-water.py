#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List
# 方法1：找到所有pool，再数每个pool里的水
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         sum_area = 0
#         pools = []
#         left_pointer = 0
#         right_pointer = n - 1

#         if n < 3:  # 最少得三个（也就是[1, 0, 1]）才能聚水
#             return sum_area

#         # find all pool from left to right
#         mode = 0  # 0: 试图找到第一个下降的点。 1：试图找到最近的一个>=左边柱子高度的柱子
#         left_pillar = None
#         right_pillar = None
#         for i in range(1, n):
#             if mode == 0:
#                 if height[i - 1] > height[i]:
#                     left_pillar = i - 1
#                     mode = 1
#             else:
#                 if height[i] >= height[left_pillar]:
#                     right_pillar = i
#                     left_pointer = right_pillar
#                     pools.append((left_pillar, right_pillar))

#                     mode = 0
#                     left_pillar = None
#                     right_pillar = None

#         # find all pool from right to left
#         mode = 0  # 0: 试图找到第一个下降的点。 1：试图找到最近的一个>=左边柱子高度的柱子
#         left_pillar = None
#         right_pillar = None
#         for i in range(n - 2, left_pointer -1, -1):
#             if mode == 0:
#                 if height[i+1] > height[i]:
#                     right_pillar = i + 1
#                     mode = 1
#             else:
#                 if height[i] >= height[right_pillar]:
#                     left_pillar = i
#                     right_pointer = left_pillar
#                     pools.append((left_pillar, right_pillar))

#                     mode = 0
#                     left_pillar = None
#                     right_pillar = None
        
#         # calculate area
#         for pool in pools:
#             abs_height = min(height[pool[0]], height[pool[1]])
#             for i in range(pool[0] + 1, pool[1]):
#                 sum_area += (abs_height - height[i])

#         return sum_area

# 方法2： 竖着数水(two pointers)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        sum_area = 0

        if n < 3:  # 最少得三个（也就是[1, 0, 1]）才能聚水
            return sum_area

        left_pointer = 1
        left_max_and_closest_pointer = 0
        right_pointer = n - 2
        right_max_and_closest_pointer = n - 1

        while left_pointer <= right_pointer:
            # 先看看左指针上的柱子有没有积水，有的话就算积水量，不确定的话就过会再看
            # left_pointer左右都有更高的，就一定有积水
            if height[left_max_and_closest_pointer] > height[left_pointer] and height[right_max_and_closest_pointer] > height[left_pointer]:
                if height[left_max_and_closest_pointer] <= height[right_max_and_closest_pointer]:
                    sum_area += (height[left_max_and_closest_pointer] - height[left_pointer])
                    left_pointer += 1
                    continue
            elif height[left_max_and_closest_pointer] <= height[left_pointer]:
                left_max_and_closest_pointer = left_pointer
                left_pointer += 1
                continue

            # 再看看右指针上的柱子有没有积水，有的话就算积水量，不确定的话就过会再看
            # right_pointer左右都有更高的，就一定有积水
            if height[left_max_and_closest_pointer] > height[right_pointer] and height[right_max_and_closest_pointer] > height[right_pointer]:
                if height[right_max_and_closest_pointer] <= height[left_max_and_closest_pointer]:
                    sum_area += (height[right_max_and_closest_pointer] - height[right_pointer])
                    right_pointer -= 1
                    continue
            elif height[right_max_and_closest_pointer] <= height[right_pointer]:
                right_max_and_closest_pointer = right_pointer
                right_pointer -= 1
                continue
        
        return sum_area

# if __name__ == "__main__":
#     s = Solution()
#     # height = [4,2,0,3,2,5]
#     height = [2,0,2]
#     print(s.trap(height)) 
# @lc code=end
