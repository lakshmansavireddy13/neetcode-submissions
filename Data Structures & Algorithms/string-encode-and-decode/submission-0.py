class Solution:

    def encode(self, strs: List[str]) -> str:
        h=''
        for s in strs:
            l=str(len(s))    #take word and find length change to string like '3'
            l=l + "#" + s    #add that string number and # and that word
            h+=l             #add to one new string   
        return h             ## return all strings in one string

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            length=''
            while s[i]!='#':
                length+=s[i]
                i+=1

            length=int(length)

            i+=1

            word=s[i:i+length]

            ans.append(word)

            i=i+length

        return ans


