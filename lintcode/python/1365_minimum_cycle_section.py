#!/usr/bin/python -t

# two pointers
# 可以考虑使用双指针(L,R)，并开一个变量记录len当前的循环节，由于循环节肯定是从第一位开始，所以用L记录当前匹配到的位置，R一直往后移动，如果当前位不匹配，那么L就重置，len就加1,这里的操作和kmp算法求next一样，循环节就是 (i - 1) - ( next[i] - 1 ) = i - next[i]。整体复杂度O(n) 。

class Solution:
    """
    @param array: an integer array
    @return: the length of the minimum cycle section
    """
    def minimumCycleSection(self, array):
        # Write your code here
        n = len(array)
        next = [0] * (n+1)
        i = 0
        j = -1
        next[0] = -1
        
        while i < n:
            if j == -1 or array[i] == array[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
                
        return i - next[i]
        
        
