
# binary search
# time O(mlogn)
# space O(1)

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        
        n = len(grid[0])
        if n == 0:
            return 0
        
        cnt = 0

        for i in range(m):
            if grid[i][0] >= 0:
                val= self.non_neg_cnt(grid[i])
                print(f"row {i}, val {val}")
            else:
                val = n
            cnt += val
            

        return cnt
    
    def non_neg_cnt(self, nums):
        n = len(nums)
        l = 0
        r = n-1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[mid] < 0:
                r = mid
            else:
                l = mid
                
        print(f"l {l}, r {r}, nums {nums}")
        if r == n-1 and nums[r] >= 0:
            return 0
        if nums[r] > 0:
            return n-r-1
        if nums[l] > 0:
            return n-l-1

        return

if __name__ == "__main__":
    s = Solution()
    a =  [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    #a = [[3,2],[1,0]]
    #a = [[-1]]
    #a = [[5,1,0],[-5,-5,-5]]
    #a = [[7,-3]]
    print(s.countNegatives(a))
