#hash and sliding window

class Solution:
    """
    @param nums: the given array
    @param k: the window size
    @return: the sum of the count of unique elements in each window
    """
    def slidingWindowUniqueElementsSum(self, nums, k):
        # write your code here
        if not nums:
            return 0
        
        n = len(nums)
        sum_count = 0
        res = 0
        counter = collections.defaultdict(int)

        if k > len(nums):
            k = len(nums)

        for i in range(k):
            counter[nums[i]] += 1
            if counter[nums[i]] == 1:
                sum_count += 1

            if counter[nums[i]] == 2:
                sum_count -= 1

        res += sum_count

        left, right = 0, k
        while right < n:
   
            counter[nums[right]] += 1
            if counter[nums[right]] == 1:
                sum_count += 1

            if counter[nums[right]] == 2:
                sum_count -= 1
            
          
            counter[nums[left]] -= 1
            if counter[nums[left]] == 1:
                sum_count += 1

            if counter[nums[left]] == 0:
                sum_count -= 1

            right += 1
            left += 1

            res += sum_count

        return res
