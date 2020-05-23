#!/usr/bin/python -t

# heap

# sift down

# time O(n)

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        n = len(A)
        for i in range((n-1-1)/2, -1, -1):
            self.siftdown(A, n, i)
            
        return
    
    def siftdown(self, A, end, start):
        while start < end:
            left = 2*start+1
            right = left + 1
            
            min_index = start
            
            if left < end and A[left] < A[min_index]:
                min_index = left
            if right < end and A[right] < A[min_index]:
                min_index = right
                
            if min_index == start:
                break
            A[min_index], A[start] = A[start], A[min_index]
            start = min_index
            
        return

# shift up
# time O(nlogn)

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        n = len(A)
        if n < 2:
            return A
            
        for i in range(0, n):
            self.shiftup(A, i)
        
        return A
        
    def shiftup(self, A, i):
        while True:
            p = (i-1)/2
            if p >= 0:
                if A[i] > A[p]:
                    break
                A[i], A[p] = A[p], A[i]
                self.shiftup(A, p)
            else:
                break
                
        return
