#!/usr/bin/python -t

# time O(n) space O(n)

class Solution:
    """
    @param A: array A of non-negative integers.
    @return: Return the number of possible results.
    """
    def subarrayBitwiseORs(self, A):
        # write your code here
        n = len(A)
        
        ret = [set() for i in range(n)]
        retSet = set()
        ret[-1].add(A[-1])
        retSet.add(A[-1])
        
        for i in range(n-2, -1, -1):
            ret[i].add(A[i])
            retSet.add(A[i])
            
            for e in ret[i+1]:
                tmp = e | A[i]
                ret[i].add(tmp)
                retSet.add(tmp)
                
        return len(retSet)


'''
Java solution

    public int subarrayBitwiseORs(int[] A) {
        Set<Integer> set = new HashSet<>();
        
        int n = A.length;
        int[][] f = new int[n][n];
        
        for (int i = 0; i < n; i ++) {
            f[i][i] = A[i];
            set.add(A[i]);
        }
        
        for (int len = 2; len <= n; len ++) {
            for (int i = 0; i <= n - len; i ++) {
                int j = i + len - 1;
                f[i][j] = f[i][j - 1] | A[j];
                set.add(f[i][j]);
            }
        }
        
        return set.size();
    }
}
'''
