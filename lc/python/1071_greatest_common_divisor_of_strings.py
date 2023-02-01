# math string and gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x%y)
            
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
