# hash map
# time O(n)
# space O(1)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        if not s:
            return True
        
        return self.vowels_cnt(s[:len(s)//2]) == self.vowels_cnt(s[len(s)//2:])
    
    def vowels_cnt(self, s):
        cnt = 0
        vowels = {"a", "e", "i", "o", "u"}
        for c in s:
            if c.lower() in vowels:
                cnt += 1
                
        return cnt
