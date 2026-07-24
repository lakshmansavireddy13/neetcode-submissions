class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        n=len(s)
        max_l=0
        h=set()
        for j in range(0,n):
            while s[j] in h:
                h.remove(s[i])
                i+=1
            h.add(s[j])

            max_l=max(max_l, j-i+1)
    
        return max_l
        