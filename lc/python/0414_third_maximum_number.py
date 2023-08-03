# array, sort, pointers

# sort
# time O(nlogn)
# space O(1)

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        ele_cnt = 1
        pre = nums[0]

        for i in range(len(nums)):
            if nums[i] != pre:
                pre = nums[i]
                ele_cnt += 1

            if ele_cnt == 3:
                return nums[i]

        return nums[0]

  # pointers
  # time O(n)
  # space O(1)

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Three variables to store maxiumum three numbers till now.
        first_max = -inf
        second_max = -inf
        third_max = -inf
    
        for num in nums:
            # This number is already used once, thus we skip it.
            if first_max == num or second_max == num or third_max == num:
                continue
            
            # If current number is greater than first maximum,
            # It means that this is the greatest number and first maximum and second max
            # will become the next two greater numbers.
            if first_max <= num:
                third_max = second_max
                second_max = first_max
                first_max = num
            # When current number is greater than second maximum,
            # it means that this is the second greatest number.
            elif second_max <= num:
                third_max = second_max
                second_max = num
            # It is the third greatest number.
            elif third_max <= num:
                third_max = num
        
        # If third max was never updated, it means we don't have 3 distinct numbers.
        if third_max == -inf:
            return first_max
        
        return third_max
