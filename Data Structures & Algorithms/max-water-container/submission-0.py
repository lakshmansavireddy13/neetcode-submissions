class Solution:
    def maxArea(self, h: List[int]) -> int:
        ans=0

        i=0
        j=len(h)-1

        while i<j:

            width=j-i

            height=min(h[i],h[j])

            water= width * height

            ans=max(ans,water)

            if h[i]<h[j]:
                i+=1
            else:
                j-=1
        return ans