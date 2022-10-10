# string
# time O(n)
# space O(1)

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
    
        ret = palindrome
        all_a = 0
        for i in range(len(palindrome)//2):
            if palindrome[i] != "a":
                ret = palindrome[:i] + "a" + palindrome[i+1:]
                return ret
        
        ret = palindrome[:-1] + "b"
        return ret
