class Solution:
    def trap(self, height: List[int]) -> int:

        total=0
        left_max=height[0]
        right_max=height[-1]

        i=1
        j=len(height)-2

        while i<=j:
            if left_max <= right_max:
                if left_max > height[i]:
                    total+=(left_max - height[i])
                else:
                    left_max=height[i]
                i+=1
    
            else:
                if right_max > height[j]:
                    total+=(right_max - height[j])

                else:
                    right_max=height[j]
                j-=1
            
        return total

