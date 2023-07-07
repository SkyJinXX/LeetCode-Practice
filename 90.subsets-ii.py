#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]: # every layer has it's own last_used
        nums.sort()
        n = len(nums)
        temp = []
        res = []
        def helper(startIndex):
            res.append(temp[:])

            last_used = None
            for i in range(startIndex, n):
                if nums[i] == last_used:
                    continue
                temp.append(nums[i])
                helper(i + 1)
                temp.pop()
                last_used = nums[i]

        helper(0)

        return res
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]: # use a global set to store used number
    #     nums.sort()
    #     n = len(nums)
    #     last_used = None
    #     temp = []
    #     res = []
    #     def helper(startIndex):
    #         nonlocal last_used
    #         res.append(temp[:])
    #         for i in range(startIndex, n):
    #             if nums[i] == last_used:
    #                 continue
    #             temp.append(nums[i])
    #             helper(i + 1)
    #             temp.pop()
    #             last_used = nums[i]
    #         # restore `last_used`
    #         last_used = None

    #     helper(0)

    #     return res
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]: # learned online and has a `used` list
    #     nums.sort()
    #     n = len(nums)
    #     used = [False] * n
    #     temp = []
    #     res = []
    #     def helper(startIndex):
    #         res.append(temp[:])
    #         for i in range(startIndex, n):
    #             # print(nums[startIndex])
    #             if i > 0 and nums[i - 1] == nums[i] and used[i - 1]:
    #                 used[i] = True
    #                 continue
    #             temp.append(nums[i])
    #             helper(i + 1)
    #             temp.pop()
    #             used[i] = True
    #         # restore `used`
    #         for i in range(startIndex, n):
    #             used[i] = False

    #     helper(0)

    #     return res

# @lc code=end

