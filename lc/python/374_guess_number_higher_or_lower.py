#!/usr/bin/python -t

#time O(log2 ^n) space O(1)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        
        while l < r:
            m = l + (r-l)/2
            
            ret = guess(m)
            #print ret, m
            if ret == 0:
                return m
            elif ret > 0:
                l = m+1
            else:
                r = m
                
        return -1


#ternay search
#time O(log3 ^n) space O(1)

#/* The guess API is defined in the parent class GuessGame.
#   @param num, your guess
#   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
#      int guess(int num); */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int low = 1;
        int high = n;
        while (low <= high) {
            int mid1 = low + (high - low) / 3;
            int mid2 = high - (high - low) / 3;
            int res1 = guess(mid1);
            int res2 = guess(mid2);
            if (res1 == 0)
                return mid1;
            if (res2 == 0)
                return mid2;
            else if (res1 < 0)
                high = mid1 - 1;
            else if (res2 > 0)
                low = mid2 + 1;
            else {
                low = mid1 + 1;
                high = mid2 - 1;
            }
        }
        return -1;
    }
}
