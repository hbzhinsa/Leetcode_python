#%%
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
nums=[1,2,3,4,5,6,7]
k=3

#%%
# method 1
class Solution(object):
    def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp=nums.pop(-1)
            nums.insert(0,temp)
        return nums
# %%
Solution.rotate(nums,k)
# %% method 2  
class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        l=len(nums)
        if l!=1 and k!=0 and l>k:
            nums[:]=nums[-k:]+nums[:l-k]
        if l!=1 and k!=0 and l<k:
           n=k%l
           nums[:]=nums[-n:]+nums[:l-n]     
#! 97% nice result
