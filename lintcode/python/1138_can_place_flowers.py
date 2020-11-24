#!/usr/bin/python -t

class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """
    def canPlaceFlowers(self, flowerbed, n):
        # Write your code here
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0) and (flowerbed[i-1] == 0 or i == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                
        return True if n <= 0 else False
