#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        isEven = ((m + n) % 2 == 0)
        half_len = (m + n) // 2
        if n > m: # ensure nums1 is always the shorter one
            nums1, nums2 = nums2, nums1
            n, m = m, n
        
        L, R = 0, n
        while L <= R:
            divider_n = L + (R - L) // 2
            divider_m = half_len - divider_n # all the left elements must be half_len, and divider_n also means left elements in the nums1, so left elements in the nums2 is (half_len - divider_n)
            
            if divider_n - 1 >= 0 and divider_m < m and nums1[divider_n - 1] > nums2[divider_m]:
                R = divider_n - 1
            elif divider_m - 1 >= 0 and divider_n < n and nums2[divider_m - 1] > nums1[divider_n]:
                L = divider_n + 1
            else:
                # calculate right_min
                if divider_m >= m:
                    right_min = nums1[divider_n]
                elif divider_n >= n:
                    right_min = nums2[divider_m]
                else:
                    right_min = min(nums1[divider_n], nums2[divider_m])
                
                if isEven:
                    # calculate left_max
                    if divider_m - 1 < 0:
                        left_max = nums1[divider_n - 1]
                    elif divider_n - 1 < 0:
                        left_max = nums2[divider_m - 1]
                    else:
                        left_max = max(nums1[divider_n - 1], nums2[divider_m - 1])
                    return (left_max + right_min) / 2
                else:
                    return right_min


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,2,2]
,[1,2,3]))
            
        
# @lc code=end

