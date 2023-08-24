#!/usr/bin/python -t

# hash table
# time O(n)
# space O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = dict()
        ret = []

        for i in range(len(nums)):
            if target-nums[i] in ht:
                ret.append(i)
                ret.append(ht[target-nums[i]])
                return ret
            ht[nums[i]] = i

        return ret

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

