#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
#%%
nums = [3,2,4]
target = 6
output=[2,0]

def twoSum(self, nums, target):
        h_map=set()
        for i in range(len(nums)):
            if target-nums[i] in h_map:
                return [i,nums.index(target-nums[i])]
            else:
                h_map.add(nums[i])
        return[]

twoSum(nums,nums,target)

# %%
