# hash map
# time O(mn)
# space O(n)

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            s = set()
            for j in range(n):
                s.add(matrix[i][j])
                
            for k in range(1, m+1):
                if k not in s:
                    return False
                
        for j in range(n):
            s = set()
            for i in range(m):
                s.add(matrix[i][j])
                
            for k in range(1, m+1):
                if k not in s:
                    return False
            
        return True
