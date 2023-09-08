#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        # find the last position of each letter
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in dic:
                dic[s[i]] = i
        
        res = []
        start = end = 0
        for i in range(len(s)):
            if i > end:
                res.append(end - start + 1)
                start = end = i
            end = max(end, dic[s[i]])
        res.append(end - start + 1)

        return res
# @lc code=end

