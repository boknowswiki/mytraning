#!/usr/bin/python -t

# binary search solution

class Solution:
    """
    @param n: a non-negative integer
    @return: the total number of full staircase rows that can be formed
    """
    def arrangeCoins(self, n):
        # Write your code here
        l = 0
        r = n
        
        while l < r:
            mid = (l+r)/2
            total = (mid+1)*mid/2
            if total == n:
                return mid
            elif total < n:
                l = mid+1
            else:
                r = mid
                
        if (l+1)*l/2 <= n:
            return l
        else:
            return l-1


class Solution:
    """
    @param n: a non-negative integer
    @return: the total number of full staircase rows that can be formed
    """
    def arrangeCoins(self, n):
        # Write your code here
        # n = (1 + x) * x / 2, 求解得 x = (-1 + sqrt(8 * n + 1)) / 2, 答案对x取整
        return int(math.floor((-1 + math.sqrt(1 + 8*n)) / 2))

