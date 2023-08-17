#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
import heapq
from collections import deque
class Solution:
    # using a sheet
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        max_exec = max(freq.values())
        number_of_max_exec = 0
        for v in freq.values():
            if v == max_exec:
                number_of_max_exec += 1
        
        return max(len(tasks), (n + 1) * (max_exec - 1) + number_of_max_exec)


    # using max_heap and queue 
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        # count tasks
        counter = {}
        for task in tasks:
            if task not in counter:
                counter[task] = 1
            else:
                counter[task] += 1
        
        # generate a max_heap from counter
        max_heap = []
        for task, number in counter.items():
            heapq.heappush([-number, task])
        
        cooldown_queue = deque([[1, None] for _ in range(n)])

        interval = 0
        while max_heap or cooldown_queue[-1][1] != None:
            
            # select a task from max_heap and do it
            if max_heap:
                task = heapq.heappop(max_heap)
                task[0] += 1
                # if the task hasn't been done
                if task[0] != 0:
                    cooldown_queue.append(task)
            
            # one unit of time has passed, add the cooldown finished task back
            task = cooldown_queue.popleft()
            if task[1] != None:
                heapq.heappush(max_heap, task)

            interval += 1
        
        return interval
            
# @lc code=end

