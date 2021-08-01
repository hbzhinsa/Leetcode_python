#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
#%%
input=[0,1,0,3]
output=[1,3,0,0,]
class Solution:
    def moveZeroes(self, nums):
        output=[]
        n=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                nums.pop(i)
                n+=1
        nums+=n*[0]
        print(nums)

Solution.moveZeroes(input,input)     
# %%
#! good result 92%