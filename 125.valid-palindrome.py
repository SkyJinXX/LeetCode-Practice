#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            left_char = s[left_pointer]
            right_char = s[right_pointer]
            if not left_char.isalnum():
                left_pointer+=1
            elif not right_char.isalnum():
                right_pointer -=1
            else:
                # 把大写转为小写
                if s[left_pointer].isupper():
                    left_char = s[left_pointer].lower()
                if s[right_pointer].isupper():
                    right_char = s[right_pointer].lower()
                
                if left_char != right_char:
                    return False

                left_pointer +=1
                right_pointer -=1
        
        return True
        
# @lc code=end

