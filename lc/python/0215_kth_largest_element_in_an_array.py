# quick select
# time O(n)
# space O(n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            if k <= len(left):
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            return pivot
        
        return quick_select(nums, k)
        
# heap
# time O(nlogn)
# space O(n-k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        
        for num in nums:
            heapq.heappush(hq, -num)
            while len(hq) > len(nums)-k+1:
                heapq.heappop(hq)
                
        return -hq[0]
      
# quick select
# time O(n)
# space O(1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0 or n < k:
            return 0
        
        return self.qs(nums, 0, n-1, k-1)
    
    def qs(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        part = self.part(nums, start, end)
        if part == k:
            return nums[part]
        elif part < k:
            return self.qs(nums, part+1, end, k)
        else:
            return self.qs(nums, start, part-1, k)
        
    def part(self, nums, start, end):
        pivot = nums[end]
        i = start
        
        for j in range(start, end):
            if nums[j] >= pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                
        nums[i], nums[end] = nums[end], nums[i]
        
        return i
