#%%
class Solution(object):
    def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len0=len(nums)
        len1=len(set(list(nums)))
        return len0!=len1
        



# %%
Solution.containsDuplicate([1,2,3,3])
# %%
Solution.containsDuplicate([1,2,3,4])
# %%
