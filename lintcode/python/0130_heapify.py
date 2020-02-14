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
    
