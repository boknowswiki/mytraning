#!/usr/bin/python -t


# from https://www.jiuzhang.com/problem/number-of-substrings-with-all-zeroes/

# sliding window， 每次多加一个0，就会多出r-l+1个符合条件的substring

class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def stringCount(self, str):
        # Write your code here.
        count = 0
        res = 0
        l = 0
        for r in range(len(str)):
            if str[r] == '1':
                count += 1
            while l <= r and count > 0:
                if str[l] == '1':
                    count -= 1
                l += 1
            res += r - l + 1
        return res
