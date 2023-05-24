#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)

        if h == len(piles):
            return max_pile

        left_boundary = 1
        right_boundary = max_pile
        
        while left_boundary <= right_boundary:
            k = left_boundary + (right_boundary - left_boundary) // 2
            h_with_k = sum((pile + k - 1) // k for pile in piles)
            if h_with_k <= h:
                right_boundary = k - 1
            else:
                left_boundary = k + 1

        return left_boundary # left_boundary is the minimum k, because left_boundary will across right_boundary in the end， it is the last minimum_k's value


# @lc code=end

