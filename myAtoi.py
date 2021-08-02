#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
#%%
s="words and 987"
class Solution:
    def myAtoi(self, s: str) -> int:
        tem_s=[]
        val=1
        for i in s:
            if i==' ':
                continue         
            elif i=='-':
                val=-1  
            elif i.isdigit():
                tem_s+=i
            elif not i.isdigit():
                break   
        if not tem_s:
            tem_s+='0'          
        out=val*int(''.join(tem_s)) 
        if out>2**31 - 1:
            return 2**31-1
        if out<-2**31:
            return -2**31
        return out       
Solution.myAtoi(s,s)
# %%
# ! shit question..