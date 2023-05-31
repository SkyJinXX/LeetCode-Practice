#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    def __init__(self):
        self.obj = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.obj:
            self.obj[key] = []
            
        self.obj[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.obj:
            return ""
        
        value_list = self.obj[key]

        if timestamp >= value_list[-1][1]:
            return value_list[-1][0]
        elif timestamp < value_list[0][1]:
            return ""
        else:
            L, R = 0, len(value_list) - 1
            while L <= R:
                M = L + (R - L) // 2
                if value_list[M][1] == timestamp:
                    return value_list[M][0]
                elif value_list[M][1] > timestamp:
                    R = M - 1
                else:
                    L = M + 1
            return value_list[R][0]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

