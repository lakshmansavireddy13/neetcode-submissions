class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        i=0
        j=0
        max_len=0
        max_freq=0
        h={}
        while j<len(s):
            if s[j] in h:
                h[s[j]]+=1
            else:
                h[s[j]]=1
            
            if h[s[j]] > max_freq:
                max_freq=h[s[j]]
            
            if (j-i+1)- max_freq <=k:
                if (j-i+1) > max_len:
                    max_len=j-i+1
                
            else:
                h[s[i]]-=1

                max_freq=0
                for key in h:
                    if h[key] > max_freq:
                        max_freq=h[key]
                    
                i+=1
            j+=1

        return max_len


