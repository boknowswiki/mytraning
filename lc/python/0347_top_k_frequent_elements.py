
# quick select or quick sort
# time O(n) worst case O(n^2)
# space O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = dict()
        unique_nums = []

        for num in nums:
            if num not in counter:
                counter[num] = 1
                unique_nums.append(num)
            else:
                counter[num] += 1
        
        n = len(unique_nums)

        def quicksort(start, end, target):
            nonlocal unique_nums

            def part(low, high):
                nonlocal unique_nums
                point = unique_nums[high]
                index = low
                i = low
                while i < high:
                    if counter[unique_nums[i]] < counter[point]:
                        unique_nums[i], unique_nums[index] = unique_nums[index], unique_nums[i]
                        index += 1
                    i += 1

                unique_nums[index], unique_nums[high] = unique_nums[high], unique_nums[index]

                return index

            if start == end:
                return
            if start < end:
                pivot = part(start, end)
                if pivot == target:
                    return
                elif pivot > target:
                    quicksort(start, pivot-1, target)
                else:
                    quicksort(pivot+1, end, target)

            return
        quicksort(0, n-1, n-k)
        #print(f"unique_nums {unique_nums}")

        return unique_nums[n-k:]
    
# quick select
# time O(n)
# space O(n)

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
            
            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]  
            
            return store_index
        
        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place. 
            """
            # base case: the list contains only one element
            if left == right: 
                return
            
            # select a random pivot_index
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return 
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)
         
        n = len(unique) 
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.  
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]  
    
    
# bucket sort
# time O(n)
# space O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = {}
        frq = {}
        for i in range(0, len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

        for z,v in hs.items():
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        
        arr = []
        
        for x in range(len(nums), 0, -1):
            if x in frq:
                
                for i in frq[x]:
                    arr.append(i)

        return [arr[x] for x in range(0, k)]

# bucket sort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        for num, freq in cnt.items():
            bucket[freq].append(num)
            
        bucketIdx = n
        ans = []
        while k > 0:
            while not bucket[bucketIdx]:  # Skip empty bucket
                bucketIdx -= 1
                
            for num in bucket[bucketIdx]:
                if k == 0: break
                ans.append(num)
                k -= 1
            bucketIdx -= 1
        return ans

# hash map and heap
# time O(nlogn)
# space O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
                
            d[num] += 1
            
        ret = []
        hq = []
        for key, val in d.items():
            heapq.heappush(hq, (-val, key))
            
        while k:
            val, key = heapq.heappop(hq)
            ret.append(key)
            k -= 1
            
        return ret
