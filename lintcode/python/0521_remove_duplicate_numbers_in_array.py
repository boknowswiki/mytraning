#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        n = len(nums)
        l = 0
        r = n-1
        index = 0
        d = set()
        
        while l <= r:
            if nums[l] not in d:
                nums[index] = nums[l]
                d.add(nums[index])
                index += 1
                l += 1
            else:
                if l == r:
                    break
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                
        return index
        

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        d = set()
        n = len(nums)
        index = 0
        
        for i in range(n):
            if nums[i] not in d:
                nums[index] = nums[i]
                index += 1
                
            d.add(nums[i])
            
        return index
        
