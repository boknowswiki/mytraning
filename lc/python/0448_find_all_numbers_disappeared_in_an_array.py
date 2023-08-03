# array, hash table
# time O(n)
# space O(1)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        for i in range(n):
            index = abs(nums[i])-1
            if nums[index] > 0:
                nums[index] *= -1
        
        # print(f"nums {nums}")
        return [i+1 for i in range(n) if nums[i] > 0]
