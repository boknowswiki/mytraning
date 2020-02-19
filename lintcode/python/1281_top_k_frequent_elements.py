#!/usr/bin/python -t

# heap


import heapq

class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        # Write your code here
        n = len(nums)
        d = {}
        ret = []
        
        for num in nums:
            d[num] = d.get(num, 0) + 1
            
        heap = []
        
        for key, v in d.items():
            heapq.heappush(heap, (-v, key))
            
        for _ in range(k):
            v, key = heapq.heappop(heap)
            ret.append(key)
            
        return ret
        

# hash table


class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        # Write your code here
        d = {}
        ret = []
        
        for num in nums:
            d[num] = d.get(num, 0) + 1
            
        q = []
            
        for key, val in d.items():
            q.append((val, key))
            
            
        q.sort(cmp=self.cmp)
        
        #print q
        
        for i in range(k):
            ret.append(q[i][1])
            
        return ret
        
        
        
    def cmp(self, a, b):
        if a[0] < b[0]:
            return 1
        elif a[0] == b[0]:
            return 0
        else:
            return -1
            
        


class Solution:
    def topKFrequent(self, nums, k):
        # 统计元素的频率
        freq_dict = dict()
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
            
        # 按照频率进行排序
        freq_dict_sorted = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        
        # 取前k个元素返回
        ret = list()
        for i in range(k):
            ret.append(freq_dict_sorted[i][0])
        return ret

