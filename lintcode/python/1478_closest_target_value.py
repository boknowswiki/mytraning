#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param target: the target
    @param array: an array
    @return: the closest value
    """
    def closestTargetValue(self, target, array):
        # Write your code here
        array.sort()
        n = len(array)
        if n == 0:
            return 0
            
        left = 0
        right = n-1
        ret = -sys.maxint
        
        while left < right:
            val = array[left] + array[right]
            
            if val <= target:
                left += 1
                ret = max(ret, val)
            else:
                right -= 1
                
        return ret if ret != -sys.maxint else -1
        
