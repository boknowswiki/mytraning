#!/usr/bin/python -t

class Solution:
    """
    @param nums: the given array
    @param k: the given number
    @return:  whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k
    """
    def containsNearbyDuplicate(self, nums, k):
        # Write your code here

        dic = {}
        for index, value in enumerate(nums):
            if value in dic and index - dic[value] <= k:
                return True
            dic[value] = index
        return False


# hash table

class Solution:
    """
    @param nums: the given array
    @param k: the given number
    @return:  whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k
    """
    def containsNearbyDuplicate(self, nums, k):
        # Write your code here
        if not nums:
            return False
            
        h = {}
        
        n = len(nums)
        
        for i in range(n):
            if nums[i] not in h:
                h[nums[i]] = i
            else:
                diff = abs(h[nums[i]]-i)
                if diff <= k:
                    return True
                h[nums[i]] = i
                
        return False
        

