#!/usr/bin/python -t

# two pointers
# 让我们从最直观的想法考虑：如果我们从左到右读字符串S，假设把一个字符'w'划入了当前的子串当中，那么S中所有'w'必须都在这个子串中。
#2. 这也就意味着子串的右边界不能低于最后一个'w'。然而，在这两个'w'中可能还有其他字符，这些字符也要满足上述条件，这可能会让子串变大。
#3. 比如S是"abccaddbeffe"，如果只看'a'，最小子串必须包含”abcca”，而其中又有'b'和'c'，所以最后一个'b'和'c'也要在子串中……重复上述步骤，最终得到“abccaddb”。
#4. 这样我们就有了算法思路：首先，为了能很快的找到任意字符的最右下标，需要提前遍历一边字符串，并用map记录最右下标。
#5. 再次遍历字符串S，用left和right表示当前子串的左边界和右边界，扩展当前的右边界right*=max(right，当前字符的最右下标）。如果已经遍历到了right位置，这时我们就可切出一个子串，这个子串的下标是从left到right（包括right），之后再设置left为下一个字符的下标。重复上述操作，直到遍历完S*。
#6. 复杂度分析：
#1. 时间复杂度：O(N)，N是字符串S的长度。两次遍历S，每一次访问都是固定时间。
#2. 空间复杂度：O(1)，这里容易被认为是O(N)，但实际上只需要固定空间就够了，因为只有26个字母，map最多只需要26个条目，字符串最多也只能切出26个部分，也即结果的List中不会超过26个数。所以，空间大小是固定的。

class Solution:
    """
    @param S: a string
    @return: a list of integers representing the size of these parts
    """
    def partitionLabels(self, S):
        # Write your code here
        n = len(S)
        l = [0] * 26
        
        for i in range(n):
            l[ord(S[i]) - ord('a')] = i
            
        left = 0
        right = 0
        ret = []
        
        for i in range(n):
            right = max(right, l[ord(S[i]) - ord('a')])
            if right == i:
                ret.append(right-left+1)
                left = i+1
                
        return ret
        
