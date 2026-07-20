class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()

        for i in range(0,len(nums)):
            j=i+1
            k=len(nums)-1

            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==0:
                    ans.add((nums[i],nums[j],nums[k]))
                    j=j+1
                    k=k-1
                elif s>0:
                    k-=1
                else:
                    j+=1
        return list(map(list,ans))