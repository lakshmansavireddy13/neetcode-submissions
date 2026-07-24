class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        if len(s1)> len(s2):
            return False
        h1={}
        h2={}
        
        i=0
        while i<len(s1):
            if s1[i] not in h1:
                h1[s1[i]]=1
            else:
                h1[s1[i]]+=1

            if s2[i] not in h2:
                h2[s2[i]]=1
            else:
                h2[s2[i]]+=1
            
            i+=1
        if h1 == h2:
            return True

        while i < len(s2):
            left = s2[i - len(s1)]
            h2[left] -= 1

            if h2[left] == 0:
                del h2[left]
            
            if s2[i] not in h2:
                h2[s2[i]] = 1
            else:
                h2[s2[i]] += 1
            
            if h1 == h2:
                return True

            i += 1

        return False


            


        

        