#!/usr/bin/python -t

class Solution:
    """
    @param str: The string
    @param k: The length of the substring
    @return: The answer
    """
    def findSubstring(self, str, k):
        # Write your code here
        ch_set = set()
        word_set = set()
        
        n = len(str)
        start, end = 0, 0
        # ch_set.add(str[0])
        
        count = 0
        while end < n:
            if str[end] not in ch_set:
                ch_set.add(str[end])
                end += 1
                
                if len(ch_set) == k:
                    word = str[start:end]
                    if word not in word_set:
                        word_set.add(word)
                        count += 1
                    ch_set.remove(str[start])
                    start += 1
            else:
                ch_set.remove(str[start])
                start += 1
                
        return count
