#!/usr/bin/python -t

class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # Write your code here
        d = {}
        ret = sys.maxint
        
        for i in range(len(words)):
            if words[i] == word1:
                d[word1] = i
            if words[i] == word2:
                d[word2] = i
            if len(d) == 2:  
                ret = min(ret, abs(d[word1]-d[word2]))    
                    
        return ret
