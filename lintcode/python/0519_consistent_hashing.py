#!/usr/bin/python -t

# heap and consistent hashing
# time O(nlogn)


import heapq

class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """
    def consistentHashing(self, n):
        # write your code here
        heap = []
        heapq.heappush(heap, (-360, 1, [0, 359, 1]))
        
        for i in range(2, n+1):
            c_hash = heapq.heappop(heap)[2]
            new_c_hash = [(c_hash[0]+c_hash[1])/2+1, c_hash[1], i]
            c_hash[1] = new_c_hash[0]-1
            heapq.heappush(heap, (-(c_hash[1]-c_hash[0]+1), c_hash[2], c_hash))
            heapq.heappush(heap, (-(new_c_hash[1]-new_c_hash[0]+1), new_c_hash[2], new_c_hash))
            
        hashing = [ele[2] for ele in heap]
        hashing.sort(key=lambda x: x[0])
        
        return hashing
        
# 每次暴力找最大的编号最小的区间，然后分割即可    


class Solution:
    # @param {int} n a positive integer
    # @return {int[][]} n x 3 matrix
    def consistentHashing(self, n):
        # Write your code here
        results = [[0, 359, 1]]
        for i in xrange(1, n):
            index = 0
            for j in xrange(i):
                if results[j][1] - results[j][0] + 1 > \
                   results[index][1] - results[index][0] + 1:
                    index = j
            
            x, y = results[index][0], results[index][1]
            results[index][1] = (x + y) / 2
            results.append([(x + y) / 2 + 1, y, i + 1])

        return results

