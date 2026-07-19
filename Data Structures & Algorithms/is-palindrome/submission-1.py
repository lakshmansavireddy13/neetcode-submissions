class Solution:
    def isPalindrome(self, num: str) -> bool:

        s=''
        for i in num:
            if i.isalnum():
                s=s+i.lower()

        i=0
        j=len(s)-1


        while i<j:
            if s[i]!=s[j]:
                return False
            else:
                i=i+1
                j=j-1

        return True
    

        