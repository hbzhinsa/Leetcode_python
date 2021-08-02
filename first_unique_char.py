#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
#%%
s = "loveleetcode"
output=0

class Solution:
    def firstUniqChar(self, s: str) -> int:
        string=list(s)  
        l=len(string)
        count=0
        for i in range(l):
            string_c=string.copy()
            string_c.pop(i)
            if string[i] not in string_c:
                return i
            else:
                count+=1
            if count==l:
                return -1
    def firstUniqChar2(self, s: str) -> int:
        maps = {}
        for i in s:
            maps[i] = maps.get(i,0) + 1
        for i in range(len(s)):
            if maps[s[i]] == 1:
                return i
        return -1
#%%   
Solution.firstUniqChar(s,s)
# ! not efficient
# %%
Solution.firstUniqChar2(s,s)
# %%
