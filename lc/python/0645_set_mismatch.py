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
