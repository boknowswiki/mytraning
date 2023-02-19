from typing import List

# vertical search

def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    m = len(mat)
    n = len(mat[0])

    # This code does the same as the animation above.
    indexes = []
    # For each cell, accessed in the order shown in the animation.
    for c, r in itertools.product(range(n), range(m)):
        if len(indexes) == k: break
        # If this is the first 0 in the current row.
        if mat[r][c] == 0 and (c == 0 or mat[r][c - 1] == 1):
            indexes.append(r)

    # If there aren't enough, it's because some of the first k weakest rows
    # are entirely 1's. We need to include the ones with the lowest indexes
    # until we have at least k.
    i = 0
    while len(indexes) < k:
        # If index i in the last column is 1, this was a full row and therefore
        # couldn't have been included in the output yet.
        if mat[i][-1] == 1:
            indexes.append(i)
        i += 1

    return indexes


# heapq

import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        if m == 0:
            return []
        n = len(mat[0])
        if n == 0:
            return []

        if k > m:
            return []

        ret = []
        min_hq = []
        
        for i in range(m):
            soldiers_cnt = self.get_cnt(mat[i])
            print(f"i {i}, cnt {soldiers_cnt}, nums {mat[i]}")
            heapq.heappush(min_hq, (soldiers_cnt, i))
            
        while k > 0:
            ret.append(heapq.heappop(min_hq)[1])
            k -= 1
            
        return ret
    
    def get_cnt(self, nums):
        l = 0
        r = len(nums)-1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[mid] == 1:
                l = mid
            else:
                r = mid
                
        if nums[r] == 1:
            return r
        if nums[l] == 1:
            return l
        return -1
            

if __name__ == "__main__":
    s = Solution()
    a =  [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
    b = 3
    a = [[1,0],[0,0],[1,0]]
    b = 2
    a = [[1,1,1,1,1],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,0],[1,1,1,1,1]]
    b = 3
    print(s.kWeakestRows(a, b))
