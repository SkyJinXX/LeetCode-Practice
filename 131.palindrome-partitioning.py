#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]: # faster 100ms than the below. Maybe because this don't generate all substrings at once.
        temp = []
        res = []

        @cache
        def isPalindrome(startIndex: int, endIndex: int) -> bool:
            if startIndex >= endIndex:
                return True
            return isPalindrome(startIndex + 1, endIndex - 1) if s[startIndex] == s[endIndex] else False

        def helper(current_divider: int):
            if current_divider == len(s):
                res.append(temp[:])
                return
            for next_divider in range(current_divider + 1, len(s) + 1):
                if isPalindrome(current_divider, next_divider - 1):
                    temp.append(s[current_divider:next_divider])
                    helper(next_divider)
                    temp.pop()

        helper(0)

        isPalindrome.cache_clear()

        return res
    # def partition(self, s: str) -> List[List[str]]:
    #     dividers = [0] # 0 means the divider is before index 0
    #     res = []

    #     @cache
    #     def isPalindrome(startIndex: int, endIndex: int) -> bool:
    #         if startIndex >= endIndex:
    #             return True
    #         return isPalindrome(startIndex + 1, endIndex - 1) if s[startIndex] == s[endIndex] else False
    #         # while startIndex < endIndex:
    #         #     if s[startIndex] != s[endIndex]:
    #         #         return False
    #         #     startIndex += 1
    #         #     endIndex -= 1
    #         # return True

    #     def helper(newDividerIndex: int):
            # if newDividerIndex > len(s):
            #     res.append([s[dividers[j]:dividers[j + 1]] for j in range(len(dividers) - 1)])
            #     return
    #         for i in range(newDividerIndex, len(s) + 1): # len(s)+1 means a divider after the last element
    #             if isPalindrome(dividers[-1], i - 1):
    #                 dividers.append(i)
    #                 helper(i + 1)
    #                 dividers.pop()

    #     helper(1)

    #     isPalindrome.cache_clear()

    #     return res
# @lc code=end

