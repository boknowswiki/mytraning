
# hash , binary search

from collections import defaultdict

class Solution:
    """
    @param str: The input string
    @param k: The repeated times
    @return: The answer
    """
    def longestRepeatingSubsequenceII(self, input_str, k):
        # Write your code here
        length = len(input_str)
        start, end = 0, length
        while start + 1 < end:
            mid = (start + end) // 2
            if self.count_longest(input_str, mid) >= k:
                start = mid
            else:
                end = mid
        
        # print(start)
        # print(end)
        # print(self.count_longest(input_str, end))
        if self.count_longest(input_str, end) >= k:
            return end
        else:
            return start
    
    
    def count_longest(self, input_str, sub_length):
        cnt = defaultdict(lambda: 0)
        max_cnt = 1
        for i in range(len(input_str) - sub_length + 1):
            cnt[input_str[i: i + sub_length]] += 1
            max_cnt = max(max_cnt, cnt[input_str[i: i + sub_length]])
        return max_cnt
