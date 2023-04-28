#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def calculateLongestLength(dic, n): #计算以当前数为始的最长序列长度，并返回长度
            if n + 1 in dic:
                if dic[n+1] != None:
                    dic[n] = dic[n+1] + 1
                else:
                    dic[n] = calculateLongestLength(dic, n + 1) + 1
            else:
                dic[n] = 1

            return dic[n]

        dic = {key: None for key in nums}
        global_longest_length = 0

        for num in dic:
            # 没走过的路就先走一下
            if dic[num] == None:
                calculateLongestLength(dic, num)
            
            # 不管是刚走过，还是之前走的时候顺带走过了，反正dic[num]有个数了
            if dic[num] > global_longest_length:
                global_longest_length = dic[num]
        
        return global_longest_length
    


        
# @lc code=end

