class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h={}
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        
        l=list(h.items())

        l.sort(key=lambda x: x[1], reverse=True)

        ans=[]
        for i in range(k):
            ans.append(l[i][0])
        return ans
        