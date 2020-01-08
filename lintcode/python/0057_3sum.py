#!/usr/bin/python -t

# two pointers
# time O(n^2) space O(1)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        
        n = len(numbers)
        ret = []
        
        for i in range(n-2):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            
            l = i+1
            r = n-1
            target = -numbers[i]
            
            while l < r:
                val = numbers[l] + numbers[r]
                if val == target:
                    ret.append([numbers[i], numbers[l], numbers[r]])
                    l += 1
                    r -= 1
                    while l < r and numbers[l] == numbers[l-1]:
                        l += 1
                    while l < r and numbers[r] == numbers[r+1]:
                        r -= 1
                elif val < target:
                    l += 1
                else:
                    r -= 1
                    
        return ret
        
