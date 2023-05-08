# matrix, array

# time O(n)
# space O(1)

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 0:
            return 0
        if n == 1:
            return mat[0][0]

        ret = 0

        for i in range(n):
            if i != n-i-1:
                ret += mat[i][i]
                ret += mat[i][n-i-1]
            else:
                ret += mat[i][i]

        return ret



class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 0:
            return 0
        if n == 1:
            return mat[0][0]

        primary_idx = 0
        secondary_idx = n-1
        ret = 0

        for i in range(n):
            if primary_idx != secondary_idx:
                ret += mat[i][primary_idx]
                ret += mat[i][secondary_idx]
            else:
                ret += mat[i][primary_idx]
            
            primary_idx += 1
            secondary_idx -= 1

        return ret
