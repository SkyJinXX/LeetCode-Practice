#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        number_of_prerequisites = [0] * numCourses
        prerequisites_to_next_course = dict()
        ordering_of_courses = []
        for next_course, prerequisite in prerequisites: # first traversal, count the number of prerequisites of a course and generate a hashmap[prerequisite -> next_course]
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
            ordering_of_courses.append(prerequisite)
            if prerequisite in prerequisites_to_next_course:
                for next_course in prerequisites_to_next_course[prerequisite]:
                    number_of_prerequisites[next_course] -= 1
                    if number_of_prerequisites[next_course] == 0:
                        courses_can_take.append(next_course) # add new courses can take
        
        if len(ordering_of_courses) == numCourses:
            return ordering_of_courses
        else:
            return []
# @lc code=end

