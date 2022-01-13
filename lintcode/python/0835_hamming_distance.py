#!/usr/bin/python -t

# binary

class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        # write your code here
        Distance = 0;
        
        while ( x != 0 or y != 0 ):
            if ( x % 2 != y % 2 ):
                Distance += 1;
            x //= 2;
            y //= 2;
        return Distance;
