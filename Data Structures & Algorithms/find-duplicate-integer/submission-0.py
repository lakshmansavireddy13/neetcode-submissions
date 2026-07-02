class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        h=set()
        for x in nums:
            if x not in h:
                h.add(x)
            else:
                return x
        