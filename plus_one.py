#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
#%%
input=[9,9,9]
output=[1,0,0,0]
class Solution:
    def plusOne(digits):
        l=len(digits) #3
        intd=0
        for i in range(l): #0，1，2
            intd+=digits[i]*10**(l-i-1) # 2,1,0
        # +1
        intd+=1       
        temp=intd//10**(l)
        out=[]
        if temp!=0:
            out+=[temp]
            intd-=out[-1]*10**(l)
        for i2 in range(l-1,-1,-1):# 2,1,0
            divid=10**(i2)
            out+=[intd//divid]
            intd-=out[-1]*divid
        return out 

            
        

        
        
              
Solution.plusOne(input)
# %%
#! ordinary 67%
