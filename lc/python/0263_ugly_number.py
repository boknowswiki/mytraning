
# math
# time O(n)
# space O(1)

class Solution:
    def isUgly(self, n: int) -> bool:
        if not n:
            return False
        
        while n != 1:
            if n % 5 == 0:
                n /= 5
            elif n % 3 == 0:
                n /= 3
            elif n % 2 == 0:
                n /= 2
            else:
                return False
            
        return True
