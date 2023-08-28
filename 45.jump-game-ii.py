#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        crt_border = nxt_border = 0
        times = 0

        # divide nums into several parts, each part represents the area that we have to took  at least 'x' step can get
        for i in range(n):
            if i > crt_border: # 越界了就先更新可供选择的界限
                crt_border = nxt_border
                times += 1
            if crt_border >= n - 1: # 看看最新的界限是否包含终点(也可以删掉这段，因为最后的times就是终点的times)
                return times
            nxt_border = max(nxt_border, i + nums[i]) # 更新下一个界限

# @lc code=end

