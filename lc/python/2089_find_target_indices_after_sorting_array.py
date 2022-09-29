# binary search
# time O(logn)
# space O(1)

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        low = self.find_low(nums, target)
        high = self.find_high(nums, target)
        
        if low == high:
            if low == -1:
                return []
            else:
                return [low]

        return [i for i in range(low, high+1)]
        
    def find_low(self, nums, target):
        l = 0
        r = len(nums)-1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
                
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
    
    def find_high(self, nums, target):
        l = 0
        r = len(nums)-1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid
            
        if nums[r] == target:
            return r
        if nums[l] == target:
            return l

        return -1
