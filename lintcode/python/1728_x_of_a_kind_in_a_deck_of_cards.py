#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param deck: a integer array
    @return: return a value of bool
    """
    def hasGroupsSizeX(self, deck):
        # write your code here
        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a
            
        d = {}
        min_avg = sys.maxint
        
        for num in deck:
            d[num] = d.get(num, 0) + 1
            
        for num in d:
            min_avg = min(min_avg, d[num])
            
        print min_avg
        
        for num in d:
            min_avg = gcd(min_avg, d[num])
        
        if min_avg < 2:
            return False
            
        for num in d:
            if d[num] != min_avg:
                if d[num] % min_avg:
                    return False
                
        return True
        
