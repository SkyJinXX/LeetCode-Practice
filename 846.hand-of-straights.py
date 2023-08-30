#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        hand_counter = Counter(hand)

        for val in hand:
            if val in hand_counter:
                for val_in_group in range(val, val + groupSize):
                    if val_in_group not in hand_counter:
                        return False
                    else:
                        hand_counter[val_in_group] -= 1
                        if hand_counter[val_in_group] == 0:
                            del hand_counter[val_in_group]
        
        return True

# @lc code=end

