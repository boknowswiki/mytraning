#!/usr/bin/python -t

# two pointers
# similar to 0032


class Solution:
    """
    @param s: a string
    @param words: a list of words
    @return: all starting indices of substring(s)
    """
    def findSubstring(self, s, words):
        # write your code here
        n = len(s)
        m = len(words)
        w_size = len(words[0])
        
        d = {}
        ret = []
        
        for word in words:
            d[word] = d.get(word, 0) + 1
        
        #print d
        for start in range(w_size):
            sliding_window = {}
            words_cnt = 0
            for i in range(start, n, w_size):
                word = s[i:i+w_size]
                if word in d:
                    sliding_window[word] = sliding_window.get(word, 0) + 1
                    words_cnt += 1
                    while d[word] < sliding_window[word]:
                        pos = i - w_size*(words_cnt-1)
                        remove_word = s[pos:pos+w_size]
                        sliding_window[remove_word] -= 1
                        if sliding_window[remove_word] == 0:
                            del sliding_window[remove_word]
                        words_cnt -= 1
                else:
                    sliding_window.clear()
                    words_cnt = 0
                if words_cnt == m:
                    ret.append(i-w_size*(words_cnt-1))
                    
        return ret
        
        
