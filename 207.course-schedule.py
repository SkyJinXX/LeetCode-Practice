#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: # abandoned
    #     number_of_prerequisites = [0] * numCourses
    #     prerequisites_to_next_course = dict()
    #     for next_course, prerequisite in prerequisites: # first traversal, count the number of prerequisites of a course and generate a hashmap[prerequisite -> next_course]
    #         number_of_prerequisites[next_course] += 1
    #         if prerequisite in prerequisites_to_next_course:
    #             prerequisites_to_next_course[prerequisite].append(next_course)
    #         else:
    #             prerequisites_to_next_course[prerequisite] = [next_course]
        
    #     courses_can_take = []
    #     for i, n in enumerate(number_of_prerequisites): # second traversal, find all courses I can take right now.
    #         if n == 0:
    #             courses_can_take.append(i)
        
    #     for prerequisite in courses_can_take:
    #         def dfs(prerequisite):
    #             if prerequisite in prerequisites_to_next_course:
    #                 for next_course in prerequisites_to_next_course[prerequisite]:


    #         if not dfs(prerequisite):
    #             return False
    #     return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        number_of_prerequisites = [0] * numCourses
        prerequisites_to_next_course = dict()
        for next_course, prerequisite in prerequisites: # first traversal, count the number of prerequisites(inDegree) of a course and generate a hashmap[prerequisite -> next_course]
            number_of_prerequisites[next_course] += 1
            if prerequisite in prerequisites_to_next_course:
                prerequisites_to_next_course[prerequisite].append(next_course)
            else:
                prerequisites_to_next_course[prerequisite] = [next_course]
        
        courses_can_take = []
        for i, n in enumerate(number_of_prerequisites): # second traversal, find all courses I can take right now.
            if n == 0:
                courses_can_take.append(i)
        
        while courses_can_take:
            prerequisite = courses_can_take.pop() # take a course
            numCourses -= 1
            if prerequisite in prerequisites_to_next_course:
                for next_course in prerequisites_to_next_course[prerequisite]:
                    number_of_prerequisites[next_course] -= 1
                    if number_of_prerequisites[next_course] == 0:
                        courses_can_take.append(next_course) # add new courses can take
        
        return numCourses == 0


# @lc code=end

