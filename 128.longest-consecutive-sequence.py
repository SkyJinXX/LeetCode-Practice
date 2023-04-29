#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence_length = 0
        nums_set = set(nums)

        while len(nums_set):
            num = nums_set.pop()
            sequence_length = 1

            # 往左找连续数
            left_num = num - 1
            while left_num in nums_set:
                nums_set.remove(left_num)
                sequence_length += 1
                left_num -= 1

            # 往右找连续数
            right_num = num + 1
            while right_num in nums_set:
                nums_set.remove(right_num)
                sequence_length += 1
                right_num += 1
            
            # 全部找完之后，判断一下这次抓出的序列有没有比最长的还长
            if sequence_length > longest_sequence_length:
                longest_sequence_length = sequence_length
            
        return longest_sequence_length
# @lc code=end

