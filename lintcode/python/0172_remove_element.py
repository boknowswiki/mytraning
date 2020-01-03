#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        n = len(A)
        j = n-1
        for i in range(n-1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
                
        return j+1
        

class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        n = len(A)
        if n == 0:
            return 0
            
        if n == 1 and A[0] == elem:
            return 0
            
        index = 0
        
        for i in range(n):
            if A[i] != elem:
                A[index] = A[i]
                index += 1
        
        return index
                
        
