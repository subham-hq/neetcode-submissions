class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_clean = "".join(char for char in ("".join(s.split()).lower()) if char.isalnum())
 
        r_clean = "".join(char for char in ("".join(s[::-1].split()).lower()) if char.isalnum())


        return s_clean == r_clean