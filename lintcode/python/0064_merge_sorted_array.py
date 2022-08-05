#!/usr/bin/python3 -t

# list array or two pointer
# time O(m+n)
# space O(1)

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        if m == 0:
            A = B
            return
        if n == 0:
            return

        index = m+n-1
        i = m-1
        j = n-1

        while i >= 0 and j >= 0:
            if A[i] >= B[j]:
                A[index] = A[i]
                i -= 1
            else:
                A[index] = B[j]
                j -= 1

            index -= 1

        while j >= 0:
            A[index] = B[j]
            j -= 1
            index -= 1

        return


if __name__ == '__main__':
    s = Solution()
    a = [1,2,3]
    b = 3
    c = [4,5]
    d = 2
    print(s.mergeSortedArray(a, b, c, d))

# two pointers

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        index = m+n-1
        i = m-1
        j = n-1
        
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[index] = A[i]
                i -= 1
            else:
                A[index] = B[j]
                j -= 1
            
            index -= 1
            
        while i >= 0:
            A[index] = A[i]
            index -= 1
            i -= 1
        
        while j >= 0:
            A[index] = B[j]
            index -= 1
            j -= 1
            
        return
    
