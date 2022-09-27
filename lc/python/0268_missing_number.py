#!/usr/bin/python -t

# sum solution
# time O(n)
# space O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = (0 + len(nums)) * (len(nums)+1)//2
        
        for num in nums:
            total -= num
            
        return total
      
# binary search
# time O(nlogn)
# space O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        nums.sort()
        print(f"nums {nums}")
        
        l = 0
        r = n
        
        while l < r:
            mid = l + (r-l)//2
            print(f"mid {mid}, nums[mid] {nums[mid]}, l {l}, r {r}")
            if nums[mid] > mid:
                r = mid
            else:
                l = mid+1
                
        return l
