#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        
        n = len(numbers)
        diff = sys.maxint
        ret = 0
        
        for i in range(n-2):
            l = i+1
            r = n-1
            while l < r:
                val = numbers[l]+numbers[r]+numbers[i]
                if abs(val-target) < diff:
                    diff = abs(val-target)
                    ret = val
                if val == target:
                    return ret
                elif val > target:
                    r -= 1
                else:
                    l += 1

                        
        return ret
        
