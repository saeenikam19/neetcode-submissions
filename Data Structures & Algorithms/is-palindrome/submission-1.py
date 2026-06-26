class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        x=0
        y=len(s)-1
        while x<y:
            if s[x]!=s[y]:
                return False
            x+=1
            y-=1
        else:
            return True
