# heapq
# time O(nlogn)
# space O(n)

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = []
        for stone in stones:
            heapq.heappush(hq, -stone)

        while len(hq) > 1:
            y = -heapq.heappop(hq)
            x = -heapq.heappop(hq)
            if x != y:
                heapq.heappush(hq, -(y-x))
            
        return -hq[0] if len(hq) == 1 else 0
      
      
# bucket sort
# time O(n+max_weight)
# space O(max_weight)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Set up the bucket array.
        max_weight = max(stones)
        buckets = [0] * (max_weight + 1)

        # Bucket sort.
        for weight in stones:
            buckets[weight] += 1

        # Scan through the weights.
        biggest_weight = 0 
        current_weight = max_weight
        while current_weight > 0:
            if buckets[current_weight] == 0:
                current_weight -= 1
            elif biggest_weight == 0:
                buckets[current_weight] %= 2
                if buckets[current_weight] == 1:
                    biggest_weight = current_weight
                current_weight -= 1
            else:
                buckets[current_weight] -= 1
                if biggest_weight - current_weight <= current_weight:
                    buckets[biggest_weight - current_weight] += 1
                    biggest_weight = 0
                else:
                    biggest_weight -= current_weight
        return biggest_weight
