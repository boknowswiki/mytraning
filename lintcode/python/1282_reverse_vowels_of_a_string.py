#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """
    def reverseVowels(self, s):
        # write your code here
        n = len(s)
        if n < 2:
            return s
            
        left = 0
        right = n-1
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        while left < right:
            # find left side
            while left < right and s[left].lower() not in vowels:
                left += 1
                
            if left == right:
                return s
                
            # find right side
            while left < right and s[right].lower() not in vowels:
                right -= 1
                
            if left == right:
                return s
                
            s = s[:left] + s[right] + s[left+1:right] + s[left] + s[right+1:]
            left += 1
            right -= 1
            
        return s
        


class Solution:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """
    def reverseVowels(self, s):
        # write your code here
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        res = list(s)
        start, end = 0, len(res)-1
        while start <= end:
            while start <= end  and res[start] not in vowels:
                start += 1
            while start <= end and res[end] not in vowels:
                end -= 1
            if start <= end:
                res[start], res[end] = res[end], res[start]
                start += 1
                end -= 1
        return "".join(res)
