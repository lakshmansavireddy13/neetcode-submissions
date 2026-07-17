class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h={}
        i=0

        for x in nums:
            if (target-x) in h:
                return [h[target-x],i]
            else:
                h[x]=i
            i=i+1
        return []