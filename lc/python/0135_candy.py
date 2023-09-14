# array, greedy
# time O(n)
# space O(n)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0

        ret = 0
        left2right = [1] * n
        right2left = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1]+1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right2left[i] = right2left[i+1]+1

        for i in range(n):
            ret += max(left2right[i], right2left[i])

        return ret
        
