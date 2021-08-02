#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
#%%
input=-123
output=321
class Solution:
    def reverse(self, x: int) -> int:
        
            string=list(str(abs(x)))
            string.reverse()
            
            if x>=0:
                temp=int(''.join(string)) 
                if temp>2**31-1:
                    return 0
                else:
                    return temp
            if x<0:
                temp=-int(''.join(string)) 
                if temp<-2**31:
                    return 0
                else:
                    return temp
        
Solution.reverse(123,input)       
# %%
# ! good result 99%
