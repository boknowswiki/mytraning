#!/usr/bin/python -t

# heap solution

# 使用九章算法强化班中讲到的 HashHeap。即一个 Hash + Heap。
# Hash 的 key 是 Heap 里的每个元素，值是这个元素在 Heap 中的下标。
# 
# 要做这个题首先需要先做一下 Data Stream Median。这个题是只在一个集合中增加数，不删除数，然后不断的求中点。
# Sliding Window Median，就是不断的增加数，删除数，然后求中点。比 Data Stream Median 难的地方就在于如何支持删除数。
# 
# 因为 Data Stream Median 的方法是用 两个 Heap，一个 max heap，一个min heap。所以删除的话，就需要让 heap 也支持删除操作。
# 由于 Python 的 heapq 并不支持 logn 时间内的删除操作，因此只能自己实现一个 hash + heap 的方法。
# 
# 总体时间复杂度 O(nlogk)O(nlogk)，n是元素个数，k 是 window 的大小。

# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class HashHeap:
    
    def __init__(self, desc=False):
        self.hash = dict()
        self.heap = []
        self.desc = desc
        
    @property
    def size(self):
        return len(self.heap)
        
    def push(self, item):
        self.heap.append(item)
        self.hash[item] = self.size - 1
        self._sift_up(self.size - 1)
        
    def pop(self):
        item = self.heap[0]
        self.remove(item)
        return item
    
    def top(self):
        return self.heap[0]
        
    def remove(self, item):
        if item not in self.hash:
            return
            
        index = self.hash[item]
        self._swap(index, self.size - 1)
        
        del self.hash[item]
        self.heap.pop()
        
        # in case of the removed item is the last item
        if index < self.size:
            self._sift_up(index)
            self._sift_down(index)

    def _smaller(self, left, right):
        return right < left if self.desc else left < right

    def _sift_up(self, index):
        while index != 0:
            parent = index // 2
            if self._smaller(self.heap[parent], self.heap[index]):
                break
            self._swap(parent, index)
            index = parent
    
    def _sift_down(self, index):
        if index is None:
            return
        while index * 2 < self.size:
            smallest = index
            left = index * 2
            right = index * 2 + 1
            
            if self._smaller(self.heap[left], self.heap[smallest]):
                smallest = left
                
            if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
                smallest = right
                
            if smallest == index:
                break
            
            self._swap(index, smallest)
            index = smallest
        
    def _swap(self, i, j):
        elem1 = self.heap[i]
        elem2 = self.heap[j]
        self.heap[i] = elem2
        self.heap[j] = elem1
        self.hash[elem1] = j
        self.hash[elem2] = i
    
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        if not nums or len(nums) < k:
            return []
            
        self.maxheap = HashHeap(desc=True)
        self.minheap = HashHeap()
        
        for i in range(0, k - 1):
            self.add((nums[i], i))
            
        medians = []
        for i in range(k - 1, len(nums)):
            self.add((nums[i], i))
            # print(self.maxheap.heap, self.median, self.minheap.heap)
            medians.append(self.median)
            self.remove((nums[i - k + 1], i - k + 1))
            # print(self.maxheap.heap, self.median, self.minheap.heap)
            
        return medians
            
    def add(self, item):
        if self.maxheap.size > self.minheap.size:
            self.minheap.push(item)
        else:
            self.maxheap.push(item)
            
        if self.maxheap.size == 0 or self.minheap.size == 0:
            return
            
        if self.maxheap.top() > self.minheap.top():
            self.maxheap.push(self.minheap.pop())
            self.minheap.push(self.maxheap.pop())
        
    def remove(self, item):
        self.maxheap.remove(item)
        self.minheap.remove(item)
        if self.maxheap.size < self.minheap.size:
            self.maxheap.push(self.minheap.pop())
        
    @property
    def median(self):
        return self.maxheap.top()[0]


# my solution
# two pointers and sort
# time O(n^2logn)

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        n = len(nums)
        if n == 0:
            return []
        if n < k:
            return []
            
        w = nums[:k]
        w.sort()
        if len(w) % 2 == 0:
            ret = [w[len(w)/2-1]]
        else:
            ret = [w[len(w)/2]]
        #print w
        
        left = 0
        right = k
        
        while right < n:
            w.append(nums[right])
            w.remove(nums[left])
            left += 1
            w.sort()
            #print w, w[len(w)/2]
            if len(w) % 2 == 0:
                ret.append(w[len(w)/2-1])
            else:
                ret.append(w[len(w)/2])
            right += 1
            
        return ret


# don't know which part is wrong, not AC
# this is because list remove breaks heap queue features, we need to call heapify again after that, but it will hit time limit exceeded after the fix the code below this one.

import heapq

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        n = len(nums)
        if n == 0 or k == 0:
            return []
            
        if n < k:
            return []
            
        ret = []
        maxhq = []
        minhq = []
        mid = 0
        
        if k > 1:
            maxhq.append(-nums[0])
            for i in range(1, k-1):
                num = nums[i]
                if num > -maxhq[0]:
                    heapq.heappush(minhq, num)
                else:
                    heapq.heappush(maxhq, -num)
                mid = -maxhq[0]
        else:
            return nums
            
        for i in range(k-1, n):
            num = nums[i]
            if num > mid:
                heapq.heappush(minhq, num)
            else:
                heapq.heappush(maxhq, -num)

            while len(maxhq) > len(minhq) + 1:
                heapq.heappush(minhq, -heapq.heappop(maxhq))
            while len(maxhq) < len(minhq):
                heapq.heappush(maxhq, -heapq.heappop(minhq))
            
            print maxhq, minhq
            
            mid = -maxhq[0]
            ret.append(mid)
            
            if nums[i-k+1] > mid:
                minhq.remove(nums[i-k+1])
            else:
                maxhq.remove(-nums[i-k+1])
                
        return ret
            

# time limit exceeded

import heapq

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        n = len(nums)
        if n == 0 or k == 0:
            return []
            
        if n < k:
            return []
            
        ret = []
        maxhq = []
        minhq = []
        mid = 0
        
        if k > 1:
            maxhq.append(-nums[0])
            for i in range(1, k-1):
                num = nums[i]
                if num > -maxhq[0]:
                    heapq.heappush(minhq, num)
                else:
                    heapq.heappush(maxhq, -num)
                mid = -maxhq[0]
        else:
            return nums
            
        for i in range(k-1, n):
            num = nums[i]
            if num > mid:
                heapq.heappush(minhq, num)
            else:
                heapq.heappush(maxhq, -num)

            while len(maxhq) > len(minhq) + 1:
                heapq.heappush(minhq, -heapq.heappop(maxhq))
            while len(maxhq) < len(minhq):
                heapq.heappush(maxhq, -heapq.heappop(minhq))

            
            mid = -maxhq[0]
            ret.append(mid)
            
            if nums[i-k+1] > mid:
                minhq.remove(nums[i-k+1])
                heapq.heapify(minhq)
            else:
                maxhq.remove(-nums[i-k+1])
                heapq.heapify(maxhq)
                
        return ret


from heapq import heappush,heappop

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        if not nums or k == 0:
            return []
        
        max_heap = []
        min_heap = []
        res = []
        
        for i in range(k):
            heappush(max_heap, (-nums[i], i))
        
        for _ in range(k // 2):
            num, index = heappop(max_heap)
            heappush(min_heap, (-num, index))
        res.append(-max_heap[0][0])
        
        # ***max_heap*** median ***min_heap***
        
        for i in range(k, len(nums)):
            # insert the num into max_heap if num < last_median
            # insert the num into min_heap if num >= last_median
            last_median = res[-1]
            if nums[i] >= last_median:
                heappush(min_heap, (nums[i], i))
                # since add the new num into the min_heap
                # if nums[i - k] in max_heap
                # then need to move one num from min_heap to max_heap
                if nums[i - k] <= last_median:
                    val, index = heappop(min_heap)
                    heappush(max_heap, (-val, index))
            else:
                heappush(max_heap, (-nums[i], i))
                # since add the new num into the max_heap
                # if nums[i - k] in min_heap
                # then need to move one num from max_heap to min_heap
                if nums[i - k] >= last_median:
                    val, index = heappop(max_heap)
                    heappush(min_heap, (-val, index))
            #print('max_heap1: ' + str(max_heap))
            #print('min_heap1: ' + str(min_heap))
            #print('------------------------')
            
            # maintain heap 
            while max_heap and i - k >= max_heap[0][1]:
                heappop(max_heap)
            while min_heap and i - k >= min_heap[0][1]:
                heappop(min_heap)
            
            #print('max_heap2: ' + str(max_heap))
            #print('min_heap2: ' + str(min_heap))
            #print('------------------------')
                
            res.append(-max_heap[0][0])
        return res


import heapq
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        self.leftMaxHeap = []
        self.rightMinHeap = []
        result = []
        for i in range(len(nums)):
            # insert new num 
            if len(self.leftMaxHeap) == 0 or nums[i] <= -self.leftMaxHeap[0]:
                heapq.heappush(self.leftMaxHeap, -nums[i])
            else:
                heapq.heappush(self.rightMinHeap, nums[i])

            self.balance()
            
            # delete old num 
            if i - k >= 0:
                if nums[i - k] <= -self.leftMaxHeap[0]:
                    self.leftMaxHeap.remove(-nums[i - k])
                    #heapq doesn't provide remove() function, we use the list.remove()
                    #but the list.remove() it will break the heap, so we need heapify the list again.
                    heapq.heapify(self.leftMaxHeap)
                else:
                    self.rightMinHeap.remove(nums[i - k])
                    heapq.heapify(self.rightMinHeap)
                    
            self.balance()
            
            if i >= k - 1:
                result.append(-self.leftMaxHeap[0])
                #print("max: " + str(self.leftMaxHeap) + " min: " + str(self.rightMinHeap))
        
        return result
    
    def balance(self):
        while len(self.leftMaxHeap) < len(self.rightMinHeap):
            heapq.heappush(self.leftMaxHeap, -heapq.heappop(self.rightMinHeap))
            
        while len(self.rightMinHeap) < len(self.leftMaxHeap) - 1:
            heapq.heappush(self.rightMinHeap, -heapq.heappop(self.leftMaxHeap))
