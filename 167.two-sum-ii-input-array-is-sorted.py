#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            n_sum = numbers[left_pointer] + numbers[right_pointer]
            if n_sum == target:
                return [left_pointer + 1, right_pointer + 1]
            if n_sum > target:
                right_pointer -= 1
            if n_sum < target:
                left_pointer += 1
# @lc code=end

