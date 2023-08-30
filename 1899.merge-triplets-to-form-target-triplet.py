#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#

# @lc code=start
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # x, y, z = target
        # a, b, c = False, False, False

        # for ai, bi, ci in triplets:
        #     if ai > x or bi > y or ci > z:
        #         continue
        #     temp_a, temp_b, temp_c = False if ai != x else True, False if bi != y else True, False if ci != z else True
        #     a, b, c = a or temp_a, b or temp_b, c or temp_c

        # return a and b and c

        x, y, z = target
        a, b, c = 1, 1, 1

        for ai, bi, ci in triplets:
            if ai > x or bi > y or ci > z:
                continue
            a, b, c = max(ai, a), max(bi, b), max(ci, c)
        
        return a == x and b == y and c == z
# @lc code=end

