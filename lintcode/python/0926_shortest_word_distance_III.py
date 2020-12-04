#!/usr/bin/python -t


# answer

class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestWordDistance(self, words, word1, word2):
        # Write your code here
        n = len(words)
        ans = n
        p1 = p2 = -n
        same = word1 == word2
        for i in xrange(n):
            if words[i] == word1:
                p1 = i
                ans = min(ans, i - p2)
                if same:
                    p2 = p1
            elif not same and words[i] == word2:
                p2 = i
                ans = min(ans, i - p1)
        return ans


# my solution

class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestWordDistance(self, words, word1, word2):
        # Write your code here
        #w1, w2 = False, False
        ret = len(words)
        
        if word2 == word1:
            l = -1
            for r in range(len(words)):
                if words[r] == word1:
                    if l == -1:
                        l = r
                    else:
                        ret = min(ret, r-l)
                        l = r
                        
            return ret
        else:                
                    
            w1_index, w2_index = -1, -1
        
        
            for index in range(len(words)):
                if words[index] == word1:
                    w1_index = index

                if word2 == words[index]:
                    w2_index = index

                if w1_index != -1 and w2_index != -1:            
                    ret = min(ret, abs(w2_index-w1_index))
            
            return ret
