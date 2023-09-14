#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = list()

        start, end = newInterval
        isPlaced = False

        for start_i, end_i in intervals:
            if end_i < start:
                ans.append([start_i, end_i])
            elif end < start_i:
                if not isPlaced:
                    ans.append([start, end])
                    isPlaced = True
                ans.append([start_i, end_i])
            else:
                start = min(start, start_i)
                end = max(end, end_i)
        
        if not isPlaced:
            ans.append([start, end])
        
        return ans

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = list()
        start, end = newInterval
        final_start, final_end = None, None
        for start_i, end_i in intervals:
            if end_i < start or final_end != None: # no intersection with newInterval, just append original interval
                ans.append([start_i, end_i])
            elif final_start == None: # determian final_start
                final_start = min(start, start_i)
                if end <= end_i:
                    final_end = end_i
                    ans.append([final_start, final_end])
            else: # find final_end
                if end <= end_i:
                    if end < start_i:
                        final_end = end
                        ans.append([final_start, final_end])
                        ans.append([start_i, end_i])
                    else:
                        final_end = end_i
                        ans.append([final_start, final_end])

        if final_start != None and final_end == None:
            ans.append([final_start, end])
        elif final_start == None and final_end == None:
            ans.append([start, end])
        
        return ans

class Solution: # wirte by outline, no simplification
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = list()
        start, end = newInterval
        final_start, final_end = None, None
        for start_i, end_i in intervals:
            if final_start == None:
                if end_i < start:
                    ans.append([start_i, end_i])
                else:
                    if start < start_i:
                        final_start = start
                    else:
                        final_start = start_i
            elif final_end == None:
                if end <= end_i:
                    if end < start_i:
                        final_end = end
                        ans.append([final_start, final_end])
                        ans.append([start_i, end_i])
                    else:
                        final_end = end_i
                        ans.append([final_start, final_end])
            else:
                ans.append([start_i, end_i])

        if final_start != None and final_end == None:
            ans.append([final_start, end])
        elif final_start == None and final_end == None:
            ans.append([start, end])
        
        return ans

# @lc code=end

