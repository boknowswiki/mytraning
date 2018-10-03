#!/usr/bin/python -t

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
		n = len(nums)
		d = {}
		for i in range(n):
			val = nums[i]
			need = target - val
			if need in d:
				return [i, d[need]]
			else:
				d[val] = i

		return []
		


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        d = {}
        for i in xrange(n):
            val = nums[i]
            need = target - val
            if (need in d):
                return [d[need], i]
            d[val] = i
            
        return []

