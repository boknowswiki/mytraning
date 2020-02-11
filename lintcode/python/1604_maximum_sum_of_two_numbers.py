#!/usr/bin/python -t

# hash table
# 

class Solution:
    """
    @param A: An Integer array
    @return: returns the maximum sum of two numbers
    """
    def MaximumSum(self, A):
        # write your code here
        n = len(A)
        d = {}
        ret = -1
        
        for i in range(n):
            num_sum = self.getSum(A[i])
            if num_sum not in d:
                d[num_sum] = [A[i]]
            else:
                d[num_sum].append(A[i])
                
        #print d
        
        for k, v in d.items():
            if len(v) < 2:
                continue
            v = sorted(v)
            ret = max(ret, v[-1]+ v[-2])
            
        return ret
            
            
            
    def getSum(self, a):
        ret = 0
        while a != 0:
            ret += a%10
            a = a//10
            
        return ret
        
    
