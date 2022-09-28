
# binary search
# time O(nlogn)
# space O(1)

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cnt = 0
        arr.sort()
        
        for a in arr:
            if a != 0:
                if self.find(2*a, arr):
                    return True
            else:
                cnt += 1
                
        return cnt >= 2
    
    def find(self, target, arr):
        l = 0
        r = len(arr)-1
        
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                r = mid-1
            else:
                l = mid+1
                
        return False
      
#hash map
# time O(n)
# space O(n)

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        a_set = set(arr)
        cnt = 0
        for i in arr:
            if i == 0:
                cnt += 1
                
        for i in a_set:
            if i*2 in a_set:
                if i == 0 and cnt > 1:
                    return True
                elif i == 0 and cnt <= 1:
                    continue
                return True
            
        return False
