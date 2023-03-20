# array and greedy
# time O(n)
# space O(1)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if l == 1 and flowerbed[0] == 0:
            return True

        cnt = 0
        for i in range(l):
            if flowerbed[i] == 0:
                if i == 0 and i+1 < l and flowerbed[i+1] == 0:
                    cnt += 1
                    flowerbed[i] = 1
                elif i == l-1 and i-1 >= 0 and flowerbed[i-1] == 0:
                    cnt += 1
                elif 0 < i < l-1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    cnt += 1

        return cnt >= n
      
 class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
                    
        return count >= n
