#!/usr/bin/python -t

# two pointers
# quickselect
# time O(n), worse case O(n^2)
# link: https://www.geeksforgeeks.org/quickselect-algorithm/

#The algorithm is similar to QuickSort. The difference is, instead of recurring for both sides (after finding pivot), it recurs only for the part that contains the k-th smallest element. The logic is simple, if index of partitioned element is more than k, then we recur for left part. If index is same as k, we have found the k-th smallest element and we return. If index is less than k, then we recur for right part. This reduces the expected complexity from O(n log n) to O(n), with a worst case of O(n^2).


class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        n = len(nums)
        
        return self.quickselect(nums, 0, n-1, k-1)
        
    def quickselect(self, nums, start, end, k):
        if start == end:
            return nums[start]
            
        mid = (start+end)/2
        pivot = nums[mid]
        left = start
        right = end
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
                
            while left <= right and nums[right] > pivot:
                right -= 1
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        if right >= k and start <= right:
            return self.quickselect(nums, start, right, k)
        elif left <= k and left <= end:
            return self.quickselect(nums, left, end, k)
        else:
            return nums[k]
            


# sort
# time O(nlogn)

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        n = len(nums)
        nums.sort()
        
        return nums[k-1]
