#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []
        res = []

        def recursion(i):
            if i == len(nums):
                res.append(temp[:])
                return
            temp.append(nums[i]) # 还必须得先执行appen过后的recursion？
            recursion(i + 1)
            temp.pop()
            recursion(i + 1)

        recursion(0)
        return res

    def aborted_but_optimized_subsets(self, nums: List[int]) -> List[List[int]]: # 看了别人的之后优化的
        res = []
        temp = []

        def recursion(i):
            res.append(temp[:])

            for j in range(i, len(nums)):
                temp.append(nums[j])
                recursion(j + 1)
                temp.pop()
        
        recursion(0)
        return list(res)

    def aborted_subsets(self, nums: List[int]) -> List[List[int]]: # 最初的自己的方法
        res = set()
        # 用set来存储frozenset是可以避免重复，但是之前重复操作的太多了，能不能提早避免?
        # 很简单，就是传个参数i，i只往前走不往回走。

        def recursion(st):
            res.add(frozenset(st))

            if len(st) == len(nums):
                return

            for n in nums:
                if n not in st:
                    st.add(n)
                    recursion(st)
                    st.remove(n)
        
        recursion(set())
        return list(res)



# @lc code=end

