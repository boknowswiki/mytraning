#!/usr/bin/python -t

# binary search solution

"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        l = 0
        r = n
        
        while l < r:
            mid = (l+r)/2
            if Guess.guess(mid) == 0:
                return mid
            elif Guess.guess(mid) == 1:
                l = mid + 1
            else:
                r = mid
                
        if Guess.guess(l) == 0:
            return l
            

