#!/usr/bin/python -t

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        start = 0
        end = n - 1
        while start < end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end = end - 1
            elif sum < target:
                start = start + 1
            else:
                return [start+1, end+1]

        return []


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)
        start = 0
        end = length - 1
        
        while start < end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end = end - 1
            elif sum < target:
                start = start + 1
            else:
                return [start+1, end+1]


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        ret = []
        l = 0
        r = n - 1
            
        while l <= r:
            total = numbers[l] + numbers[r]
            
            if total == target:
                ret = [l+1, r+1]
                return ret
            elif target < total:
                    r = r - 1
            else:
                    l = l + 1
                    
        return ret
