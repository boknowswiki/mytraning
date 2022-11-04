# two pointers
# time O(n)
# space O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return ""
        
        list_s = list(s)
        #print(f"list {list_s}")
        l = 0
        r = len(list_s)-1
        #print(f"l {l}, r {r}")
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        while l < r:
            while l < r and list_s[l] not in vowels:
                l += 1
                
            while l < r and list_s[r] not in vowels:
                r -= 1
                
            if l < r:
                list_s[l], list_s[r] = list_s[r], list_s[l]
                l += 1
                r -= 1
                
        return "".join(list_s)
