class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        n=int(''.join(map(str,nums)))
        n=n+1
        ans=list(map(int,str(n)))
        return ans