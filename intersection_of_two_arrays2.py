#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
#%%
num1=[1,2,2,1]
num2=[2]
class Solution:
    def intersect(nums1, nums2):
        out=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                out+=[nums1[i]]
                nums2.remove(nums1[i])
        return out
                

        
Solution.intersect(num1,num2)   
   
        
# %%
#! too slow 22%