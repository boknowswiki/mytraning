#!/usr/bin/python3 -t

# time O(mn)
# space O(m+n)

class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        n = len(source)
        m = len(target)

        if m == n == 0:
            return 0

        if m > n:
            return -1

        if m == n and source != target:
            return -1

        for i in range(n-m+1):
            j = 0
            while i+j < n and j < m and source[i+j] == target[j]:
                j += 1
            if j == m:
                return i
            else:
                continue

        return -1

        
if __name__ == '__main__':
    s = Solution()
    a = "source"
    b = "target"
    a = "abcdabcdefg"
    b = "bcd"
    print(s.str_str(a,b))