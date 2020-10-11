#!/usr/bin/python -t

class Solution:
    """
    @param s: the string
    @param k: the k
    @return: the answer
    """
    def wordSegmentation(self, s, k):
        # Write your code here
        n = len(s)
        if k>n:
            return [s]
        if k==0:
            return 
        result = []
        words = s.split(" ")
        unique = 0
        s = words[0]
        for i in range(1, len(words)):
            if len(words[i]) < k and len(s) <= k-len(words[i])-1:
                s += " "
                s += words[i]
                print s 
            else:
                result.append(s)
                s = words[i] 
        if result[-1] != s:
            result.append(s)
        return result
