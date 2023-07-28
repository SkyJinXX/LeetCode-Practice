#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int: # from start to end (space efficient)
        possible_two = {'10', '11', '12', '13','14','15','16','17','18','19','20','21','22','23','24','25','26'}
    
        pre_psblt_2, pre_psblt_1 = 1, 0 # pre_psblt_2 means an empty string ''. To decode an empty string '', there is only 1 possibility
        if s[0] != '0':
            pre_psblt_1 = 1
        
        for i in range(2, len(s) + 1):
            pre_psblt_1, pre_psblt_2 = (pre_psblt_1 if s[i - 1] != '0' else 0) + (pre_psblt_2 if s[i - 2: i] in possible_two else 0), pre_psblt_1 # also we can use "int(s[i - 2: i]) < 27 and s[i - 2] != '0'" to replace 's[i - 2: i] in possible_two'
        
        return pre_psblt_1


    # def numDecodings(self, s: str) -> int: # from start to end
    #     possible_two = {'10', '11', '12', '13','14','15','16','17','18','19','20','21','22','23','24','25','26'}
    
    #     possibilities = [0] * (len(s) + 1) # '11106', the first '1''s possibilities is stored in possibilities[1], because '1'.length is 1
    #     possibilities[0] = 1 # to decode an empty string '', there is only 1 possibility
    #     if s[0] != '0':
    #         possibilities[1] = 1
        
    #     for i in range(2, len(s) + 1):
    #         possibilities[i] = (possibilities[i - 1] if s[i - 1] != '0' else 0) + (possibilities[i - 2] if s[i - 2: i] in possible_two else 0)
        
    #     return possibilities[len(s)]


    # def numDecodings(self, s: str) -> int:# from end to start
    #     if len(s) == 1:
    #         if s == '0':
    #             return 0
    #         else:
    #             return 1
        
    #     possible_two = {'10', '11', '12', '13','14','15','16','17','18','19','20','21','22','23','24','25','26'}
    
    #     possibilities = [0] * (len(s) + 1) # '11106', '6' is stored in possibilities[1], because '6'.length is 1
    #     possibilities[0] = 1 # can't explain, but is right?
    #     if s[-1] != '0':
    #         possibilities[1] = 1
    #     possibilities[2] = (possibilities[1] if s[-2] != '0' else 0) + (possibilities[0] if s[-2:] in possible_two else 0)
        
    #     for i in range(3, len(s) + 1):
    #         possibilities[i] = (possibilities[i - 1] if s[-i] != '0' else 0) + (possibilities[i - 2] if s[-i: -i + 2] in possible_two else 0)
        
    #     return possibilities[len(s)]

# @lc code=end

