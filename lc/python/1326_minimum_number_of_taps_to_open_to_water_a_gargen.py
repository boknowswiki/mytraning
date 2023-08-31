# greedy
# time O(n)
# space O(n)

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Create a list to track the maximum reach for each position
        max_reach = [0] * (n + 1)

        # Calculate the maximum reach for each tap
        for i in range(len(ranges)):
            # Calculate the leftmost position the tap can reach
            start = max(0, i - ranges[i])
            # Calculate the rightmost position the tap can reach
            end = min(n, i + ranges[i])

            # Update the maximum reach for the leftmost position
            max_reach[start] = max(max_reach[start], end)
        
        # Number of taps used
        taps = 0
        # Current rightmost position reached
        curr_end = 0
        # Next rightmost position that can be reached
        next_end = 0

        # Iterate through the garden
        for i in range(n + 1):
            if i > next_end:
                # Current position cannot be reached
                return -1

            if i > curr_end:
                # Increment taps when moving to a new tap
                taps += 1
                # Move to the rightmost position that can be reached
                curr_end = next_end

            # Update the next rightmost position that can be reached
            next_end = max(next_end, max_reach[i])

        # Return the minimum number of taps used
        return taps

# dp
# time O(m*n)
# space O(n)

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # dp[i] is the min tap from 0 to ith position to get water
        # dp[tap_end] = min(dp[tap_end], dp[j]+1) for j in range(tap_start, tap_end)
        # dp[:n+1] = sys.maxsize dp[0] = 0
        # return dp[n]
        dp = [sys.maxsize] * (n+1)
        dp[0] = 0

        for i in range(n+1):
            tap_start = max(0, i-ranges[i])
            tap_end = min(n, i+ranges[i])

            for j in range(tap_start, tap_end+1):
                dp[tap_end] = min(dp[tap_end], dp[j]+1)

        return dp[n] if dp[n] != sys.maxsize else -1
