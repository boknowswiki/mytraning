#!/usr/bin/python -t

# binary search solution
#采用的是二分法 + 双指针
#二分法确定一个位置，左侧是 < target，右侧是 >= target
#然后用两根指针从中间向两边走，依次找到最接近的 k 个数

class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        n = len(A)
        l = 0
        r = n-1
        target_index = -1
        
        while l < r:
            mid = (l+r)/2
            if A[mid] == target:
                target_index = mid
                break
            elif A[mid] < target:
                l = mid+1
            else:
                r = mid
        if target_index == -1:
            target_index = l
        ret = []
        l = target_index-1
        r = target_index
        
        for _ in range(k):
            if self.is_left_closer(A, target, l, r):
                ret.append(A[l])
                l -= 1
            else:
                ret.append(A[r])
                r += 1
                
        return ret
        
    def is_left_closer(self, A, target, l, r):
        if l < 0:
            return False
        if r >= len(A):
            return True
        return target-A[l] <= A[r] - target

