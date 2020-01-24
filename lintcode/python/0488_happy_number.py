#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        # write your code here
        seen = set()
        while n > 1:
            tmp = 0
            while n:
                tmp += (n % 10) * (n % 10)
                n = n // 10
            if tmp in seen:
                return False
            seen.add(tmp)
            n = tmp
        return n == 1


class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        # write your code here
        if n <= 0:
            return False
            
        d = set()
        
        while True:
            sum = 0
            while n > 0:
                val = n%10
                #print val
                sum += val ** 2
                n = n//10
                
            #print sum
            if sum == 1:
                return True
            if sum in d:
                return False
                
            d.add(sum)
            n = sum
            
        return False
            
            
            

