from typing import List

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
