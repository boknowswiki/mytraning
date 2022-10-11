# greedy
# time O(n)
# space O(1)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = sys.maxsize
        for num in nums:
            if num < first:
                first = num
            if num > first and num < second:
                second = num
            if num > second:
                return True
            
        return False
      
