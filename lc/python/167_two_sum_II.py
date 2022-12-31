#!/usr/bin/python -t

# two pointers
# time O(n)
# space O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            val = numbers[l] + numbers[r]
            if val == target:
                return [l+1, r+1]
            elif val < target:
                l += 1
            else:
                r -= 1

        return [-1, -1]

# binary search
# time O(n)
# space O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n < 2:
            return [-1, -1]
    
        for i in range(n):
            need = target - numbers[i]
            index = self.find(numbers, need)
            if index >= 0 and index != i:
                return [min(i+1, index+1), max(i+1, index+1)]
            
        return [-1, -1]
    
    def find(self, nums, target):
        l = 0
        r = len(nums)-1
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
                
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1

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
