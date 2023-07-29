#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
# [2,-5,-2,-4,3]
# [1,0,-1,2,3,-5,-2]
class Solution:
    def maxProduct(self, nums: List[int]) -> int: # DP
        n = len(nums)
        dp_min = [None] * n
        dp_max = [None] * n
        dp_min[0], dp_max[0] = nums[0], nums[0]

        for i in range(1, n):
            dp_min[i] = min(dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i])
            dp_max[i] = max(dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i])
        
        max_product = float('-inf')
        for product in dp_max:
            max_product = max(max_product, product)
        
        return max_product
    def maxProduct(self, nums: List[int]) -> int: # Sliding Window
        n = len(nums)
        next_negative_index = [-1] * n # next negative number without the break by '0'

        # initiate next_negative_index
        pre_negative_index = -1
        for i in range(n):
            if nums[i] < 0:
                if pre_negative_index == -1:
                    pre_negative_index = i
                else:
                    next_negative_index[pre_negative_index] = i
                    pre_negative_index = -1
            if nums[i] == 0:
                pre_negative_index = -1
        
        print(next_negative_index)
         
        crt_product, max_product = 1, float('-inf')
        L, R = 0, 0
        while R < n and L < n:
            if nums[R] < 0:
                # if crt_product > 0: # the crt_product can be negative, so we have to make sure we will meet negative number again.
                #     if next_negative_index[R] > 0:
                #         crt_product *= nums[R]
                #     else:
                #         crt_product = 1
                # else:
                #     crt_product *= nums[R]'

                # or
                if crt_product > 0 and next_negative_index[R] == -1:
                    crt_product *= nums[R]
                    while L < R: # move left_pointer to right, until we find a negative number
                        crt_product //= nums[L]
                        L += 1
                        if crt_product > 0:
                            break
                    max_product = max(max_product, crt_product)
                    if crt_product < 0: # if we didn't find another negative number, we have to skip current negetive number
                        crt_product = 1
                        L += 1
                else: # (crt_product > 0 and next_negative_index[R] != -1) or (crt_product < 0)
                    crt_product *= nums[R]
                    max_product = max(max_product, crt_product)
            elif nums[R] == 0:
                max_product = max(max_product, 0)
                crt_product = 1
                L = R + 1
            else:
                crt_product *= nums[R]
                max_product = max(max_product, crt_product)
            
            R += 1
        
        return max_product

                


# @lc code=end

