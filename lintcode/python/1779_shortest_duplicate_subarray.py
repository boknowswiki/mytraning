#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param arr: The array you should find shortest subarray length which has duplicate elements.
    @return: Return the shortest subarray length which has duplicate elements.
    """
    def getLength(self, arr):
        # Write your code here.
        n = len(arr)
        d = {}
        ret = sys.maxint
        
        for i in range(n):
            if arr[i] not in d:
                d[arr[i]] = i
            else:
                ret = min(ret, i-d[arr[i]]+1)
                d[arr[i]] = i
                
        return ret if ret != sys.maxint else -1
        
        
