#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        # Write your code here
        s =set(J)
        ret = 0
        
        for ss in S:
            if ss in s:
                ret += 1
                
        return ret
        
        
