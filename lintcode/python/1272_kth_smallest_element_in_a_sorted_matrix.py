#!/usr/bin/python -t

# binary search solution
#采用二分答案的方式来解决问题。
#我们知道答案一定在[minNum,maxNum]这个区间内。
#对于某一个数res,我们将其与矩阵中的每一个数作对比，统计比他大的数字的个数，如果个数正好等于k且res在矩阵中则答案为res。

class Solution:
    """
    @param matrix: List[List[int]]
    @param k: a integer
    @return: return a integer
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        if not matrix:
            return 0
            
        l = matrix[0][0]
        r = matrix[-1][-1]
        
        while l < r:
            mid = l + (r-l)/2
            if self.getCnt(matrix, mid) < k:
                l = mid+1
            else:
                r = mid
                
        return l
        
    def getCnt(self, matrix, target):
        n = len(matrix)
        if n == 0:
            return 0
            
        i = 0
        j = n-1
        cnt = 0
        while i < n and j >= 0:
            if matrix[i][j] <= target:
                i += 1
                cnt += j+1
            else:
                j -= 1
                
        return cnt

