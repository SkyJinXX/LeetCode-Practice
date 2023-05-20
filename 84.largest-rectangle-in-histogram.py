#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List
# 总体思路都是遇到一个柱子就左右延展开，找到最大矩形
# 自研，从高到底记录下每个矩形的start,end，可以用来跳过,O(nlogn)
class Solution_1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        largest_rectangle_area = 0
        sorted_indices = [index for _, index in sorted(zip(heights, [i for i in range(n)]), reverse= True)]
        
        for i in sorted_indices:
            if isinstance(heights[i], tuple) or heights[i] == -1:
                continue

            right_pointer = i
            left_pointer = i
            current_rectangle_area = heights[i]

            # try right
            while right_pointer < n - 1:
                if isinstance(heights[right_pointer + 1], int):
                    if heights[right_pointer + 1] >= heights[i]:
                        heights[right_pointer + 1] = -1
                        current_rectangle_area += heights[i]
                    else:
                        break
                else: # tuple: (start index, end index, higher than a height)
                    start, end, min_height = heights[right_pointer + 1]
                    if min_height >= heights[i]:
                        current_rectangle_area += (end - start + 1) * heights[i]
                        right_pointer = end
                        break
                    else:
                        break
                
                right_pointer += 1
                        

            # try left
            while left_pointer > 0:
                if isinstance(heights[left_pointer - 1], int):
                    if heights[left_pointer - 1] >= heights[i]:
                        heights[left_pointer - 1] = -1
                        current_rectangle_area += heights[i]
                    else:
                        break
                else: # tuple: (start index, end index, higher than a height)
                    start, end, min_height = heights[left_pointer - 1]
                    if min_height >= heights[i]:
                        current_rectangle_area += (end - start + 1) * heights[i]
                        left_pointer = start
                        break
                    else:
                        break
                
                left_pointer -= 1

            # save boundary and the height of rectangle
            if left_pointer != right_pointer:
                rectangle_height = heights[i]
                heights[left_pointer] = (left_pointer, right_pointer, rectangle_height)
                heights[right_pointer] = (left_pointer, right_pointer, rectangle_height)
            # update largest_rectangle_area
            largest_rectangle_area = max(largest_rectangle_area, current_rectangle_area)

        return largest_rectangle_area
# 遇到柱子先存着，左右都确定了再取出
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        res = 0
        store = []
        for i in range(len(heights)):
            while store and heights[i] < heights[store[-1]]:
                    tmp = store.pop()
                    res = max(res, (i- store[-1] - 1) * heights[tmp]) # don't worry about exceed index, there always is a 0 in the store
            store.append(i)
        
        return res

            
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # print(s.largestRectangleArea([2,1,5,6,2,3])) 
    print(s.largestRectangleArea([999,999,999,999])) 