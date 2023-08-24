#!/usr/bin/python -t

# hash table

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        s = set()

        for num in nums:
            if num in s:
                return True
            s.add(num)

        return False

#Time: O(nlogn), space O(1)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        nums.sort()
        
        index = 0
        
        for i in range(1, n):
            if nums[i] == nums[index]:
                return True
            else:
                index = index + 1
                
        return False

        

#Time: O(n), space O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        d = set()
        
        for i in range(n):
            if nums[i] in d:
                return True
            else:
                d.add(nums[i])
                
        return False

