class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s.lower() if c.isalnum())
        for i in range(int(len(s)/2)):
            end = s[-1-i]
            if s[i] != end:
                return False
        
        return True
        