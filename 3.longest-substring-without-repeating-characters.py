#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        lst = []
        max_length = 0
        for c in s:
            if c in st:
                max_length = max(len(st), max_length)
                popped_char = None
                while popped_char != c:
                    popped_char = lst.pop(0)
                    st.remove(popped_char)
            st.add(c)
            lst.append(c)
        
        max_length = max(len(st), max_length)
        
        return max_length
# @lc code=end

