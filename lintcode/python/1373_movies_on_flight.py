#!/usr/bin/python -t

import sys

class Solution:
    """
    @param arr: An integer array represents durations of movies
    @param k: An integer represents the duration of the flight
    @return: the pair of movies index with the longest total duration
    """
    def FlightDetails(self, arr, k):
        # write your code here
        n = len(arr)
        mm = []
        for i, t in enumerate(arr):
            mm.append((t, i))

        mm.sort()
        
        l = 0
        r = n-1
        target = k-30
        retIndex = None
        retT = 0
        while l < r:
            total = mm[l][0]+mm[r][0]
            if total <= target:
                if target-total < target-retT:
                    retIndex = (l, r)
                    retT = total
                l += 1
            else:
                r -= 1
        return sorted([mm[retIndex[0]][1], mm[retIndex[1]][1]])


if __name__ == '__main__':
    s = Solution()
    a = [90, 85, 75, 60, 120, 150, 125]
    b = 250
    print(s.FlightDetails(a, b))