# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
#%%
s='absc'
t='csba'
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            mapt={}
            maps={}
            for i in s:
                maps[i]=maps.get(i,0)+1
            for j in t:
                mapt[j]=mapt.get(j,0)+1
            print(mapt)
        for k in range(len(maps)):
            num=mapt.get(s[k],-1)
            if num!=maps.get(s[k],-1):
                return False
        return True
Solution.isAnagram(s,s,t)        

#! normal 68%      
        
       
                
            
# %%
