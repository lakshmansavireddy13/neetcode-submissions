class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if x<0:
            sign=-1
            x=-x

        ans=0
        while x>0:
            r=x%10
            x=x//10
            ans=ans*10+r
        ans=ans*sign
        
        if ans < -(2**31)  or ans > (2**31-1):
            return 0
    
        return ans

