# math
# time O(n)
# space O(1)

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = missing = -1
        
        for num in nums:
            if nums[abs(num)-1] < 0:
                dup = abs(num)
            else:
                nums[abs(num)-1] *= -1
                
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i+1
                
        return [dup, missing]

# hashmap
# time O(n)
# space O(n)

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}
        dup = -1
        missing = -1
        
        for num in nums:
            d[num] = d.get(num, 0) + 1
            
        for i in range(1, len(nums)+1):
            if i in d:
                if d[i] == 2:
                    dup = i
            else:
                missing = i
                
        return [dup, missing]
