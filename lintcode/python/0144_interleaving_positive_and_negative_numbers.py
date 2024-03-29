#!/usr/bin/python -t

# two pointers
# time O(n)
# space O(1)

from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, a: List[int]):
        # write your code here
        pos, neg = 0, 0
        for num in a:
            if num > 0:
                pos += 1
            else:
                neg += 1

        self.partition(a, pos > neg)
        self.interleave(a, pos == neg)

    def partition(self, A, start_positive):
        flag = 1 if start_positive else -1
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] * flag > 0:
                left += 1
            while left <= right and A[right] * flag < 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

    def interleave(self, A, has_same_length):
        left, right = 1, len(A) - 1
        if has_same_length:
            right = len(A) - 2

        while left < right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 2, right - 2

# two pointers

# better
class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        la = len(A)
        if la <= 1:
            return
        cnt_z = 0
        cnt_f = 0
        for i in A:
            if i > 0:
                cnt_z += 1
            else:
                cnt_f += 1
        if cnt_z > cnt_f:
            fu = 1
            zheng = 0
        else:
            fu = 0
            zheng = 1
        while fu < la and zheng < la:
            while fu < la and A[fu] < 0:
                fu += 2
            while zheng < la and A[zheng] > 0:
                zheng += 2
            if fu < la and zheng < la:
                A[fu], A[zheng] = A[zheng], A[fu]
                fu += 2
                zheng += 2
                
        return
    
                

# 两根指针，首先判断正数多还是负数多，并把多的那一部分移到后半部分，最后两根指针分别递增二交换即可

class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        n = len(A)
        pos = 0
        neg = 0
        
        for i in range(n):
            if A[i] < 0:
                neg += 1
            else:
                pos += 1
                
        if pos > neg:
            left, right = 0, n-1
            while left < right:
                while left < right and A[left] > 0:
                    left += 1
                while left < right and A[right] < 0:
                    right -= 1
                    
                if left <= right:
                    A[left], A[right] = A[right], A[left]
                    left += 1
                    right -= 1
            left, right = 1, n-1
            while left < right:
                A[left], A[right] = A[right], A[left]
                left += 2
                right -= 2
                
        else:
            left, right = 0, n-1
            while left < right:
                while left < right and A[left] < 0:
                    left += 1
                while left < right and A[right] > 0:
                    right -= 1
                if left <= right:
                    A[left], A[right] = A[right], A[left]
                    left += 1
                    right -= 1
            if pos == neg:
                left, right = 1, n-2
            else:
                left, right = 1, n-1
            while left < right:
                A[left], A[right] = A[right], A[left]
                left += 2
                right -= 2
                
        return
    
                
