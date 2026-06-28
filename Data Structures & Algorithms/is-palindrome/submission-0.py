class Solution:
    def isPalindrome(self, s: str) -> bool:
        origString = "".join(c for c in s.lower().replace(" ", "") if c.isalnum())
        newString = "".join(c for c in s[::-1].lower().replace(" ", "") if c.isalnum())
        
        return origString == newString
        