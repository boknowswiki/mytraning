# heapq

import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        #print(f"m {m}, n {n}")
        hq = []

        def get_cnt(l):
            cnt = 0
            for i in l:
                if i != 1:
                    break
                cnt += 1
            
            return cnt

        for i in range(m):
            soldiers_cnt = get_cnt(mat[i])
            put_num = (soldiers_cnt << m) | i
            #print(f"s {soldiers_cnt}, put_num {put_num}")
            heapq.heappush(hq, (soldiers_cnt << m) | i)

        ret = []

        for _ in range(k):
            cur = heapq.heappop(hq)
            get_num = cur&((1<<m)-1)
            #print(f"cur {cur}, get_num {get_num}, musk {1<<m-1}")
            ret.append(get_num)

        return ret

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
