#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
#%%
s = "A man, a plan, b canal: Panama"
out=True

class Solution:
    def isPalindrome(self, s: str) -> bool:        
        alpha_num_str = "".join([char for char in s if char.isalnum()])
        print(alpha_num_str)
        if alpha_num_str.lower() == "".join([char for char in reversed(alpha_num_str.lower())]):
            return True
        else:
            return False
        
Solution.isPalindrome(s,s)       
# %%
#! not understanding..- -