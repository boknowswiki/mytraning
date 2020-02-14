#!/usr/bin/python -t

# heap

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        n = len(A)
        
        for i in range(n, -1, -1):
            self.helper(A, n, i)
            
    def helper(self, A, end, start):
        min_val = start
        left = 2*start+1
        right = 2*start+2
        
        if left < end and A[left] < A[start]:
            min_val = left
        if right < end and A[right] < A[min_val]:
            min_val = right
            
        if min_val != start:
            A[start], A[min_val] = A[min_val], A[start]
            self.helper(A, end, min_val)
            
        return
    

# sift down

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

