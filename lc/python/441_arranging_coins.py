#!/usr/bin/python -t

# binary search
# time O(logn)
# space O(1)

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n
        
        while l + 1 < r:
            mid = l + (r-l)//2
            coin_needed = self.coin_num(mid)
            if coin_needed == n:
                return mid
            elif coin_needed < n:
                l = mid
            else:
                r = mid
                
        if self.coin_num(r) <= n:
            return r
        return l
    
    def coin_num(self, num):
        return (1+num)*num//2

#time O(log2^n) space O(1)

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        
        l = 1
        r = n
        
        while l < r:
            m = l + (r-l)/2
            
            need = (1+m)*m/2
            if need <= n:
                l = m+1
            else:
                r = m
                
        return l-1
