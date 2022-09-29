
# binary search
# time O(nlogn)
# space O(1)

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        def is_valid(val):
            l = 0
            r = len(arr2)-1
            
            while l + 1 < r:
                mid = l + (r-l)//2
                if abs(arr2[mid] - val) <= d:
                    return False
                elif arr2[mid] > val:
                    r = mid
                else:
                    l = mid
                    
            if abs(arr2[r] - val) <= d:
                return False
            if abs(arr2[l]-val) <= d:
                return False
            return True
            
        
        return sum(is_valid(x) for x in arr1)
