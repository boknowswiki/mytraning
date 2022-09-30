#!/usr/bin/python -t

# binary search
#Time O(logmn) space O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        start = 0
        end = m*n - 1
        
        while start <= end:
            mid = (start+end)/2
            val = matrix[mid/n][mid%n]
            if val == target:
                return True
            elif val < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return False

    class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        
        row = self.find_row(matrix, target)
        
        return self.find_num(matrix[row], target)
    
    def find_row(self, matrix, target):
        l = 0
        r = len(matrix)-1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if matrix[mid][0] <= target:
                l = mid
            else:
                r = mid
                
        if matrix[r][0] <= target:
            return r
        return l
    
    def find_num(self, nums, target):
        l = 0
        r = len(nums)-1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
                
        if nums[l] == target:
            return True
        if nums[r] == target:
            return True
        return False
