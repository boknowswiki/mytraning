# binary search
# Let n be the length of time, m be the upper limit of totalTrips and k be the maximum time taken by one trip.
# time O(n*log(m*k))
# space O(1)

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = max(time)*totalTrips

        def is_time_enough(given_time):
            total = 0
            for t in time:
                total += given_time//t
            return total >= totalTrips


        while left < right:
            mid = (left+right)//2
            if is_time_enough(mid):
                right = mid
            else:
                left = mid + 1

        return left
