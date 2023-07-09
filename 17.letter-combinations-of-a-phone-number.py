#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 能不能不要这句话？
        # 好像去不掉，因为空数组不应该进入`if i==len(digits)`这句话，这句话的目的是把前面的寻找结果都加进去，但空数组都还没开始找
        # 或者硬要进入`if i==len(digits)`，那前面寻找的结果为空，就应该加入一个空进去，而不是一个空字符串''进去
        # 所以其实可以把 `if i == len(digits):`改成`if i == len(digits) and temp:`，但是这样就每次都多判断一下了，浪费时间
        if not digits: 
            return []

        dic = ['', '', ['a', 'b', 'c'], ['d', 'e', 'f'], ['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        temp = []
        res = []

        def helper(i):
            if i == len(digits):
                res.append(''.join(temp))
                return
            for c in dic[int(digits[i])]:
                temp.append(c)
                helper(i + 1)
                temp.pop()
        
        helper(0)
        return res
# @lc code=end

