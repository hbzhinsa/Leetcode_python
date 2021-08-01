#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
#%%
num=[2,3,5,7,2,3,5]
output=7
#
class Solution:
    def singleNumber(nums):
        num.sort()
        num.append(0.1)
        for i in range(0,len(num),2):
            if num[i]!=num[i+1]:
               break
        return num[i]

Solution.singleNumber(num)              
# %%
#! good result 97%