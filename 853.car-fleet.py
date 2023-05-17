#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort two list by position
        position[:], speed[:] = zip(*sorted(zip(position, speed), key=lambda x: x[0]))

        n = len(position)
        fleet_num = 0
        for i in range(n):
            speed[i] = (target - position[i])/ speed[i] # directly overwrite speed list with spent time to save space

        fleet_head_index = n - 1 # the first car must be a fleet_head
        fleet_num += 1 
        for i in range(n - 1, -1, -1):
            if speed[i] > speed[fleet_head_index]: # only when car_i arrives the destination later than the fleet_head, it can be another fleet_head
                fleet_head_index = i
                fleet_num += 1

        return fleet_num
# @lc code=end


# if __name__ == "__main__":
#     s = Solution()
#     print(s.carFleet(10,
# [0,4,2],
# [2,1,3])) 