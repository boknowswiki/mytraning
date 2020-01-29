#!/usr/bin/python -t

# hash table


import re

class Solution:
    """
    @param paragraph: 
    @param banned: 
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        #
        list_words = re.findall(r'\w+', paragraph.lower())
        banned = set(banned)
        #print list_words
        d = {}
        max_cnt = 0
        ret = ""
        
        for word in list_words:
            if word not in banned:
                d[word] = d.get(word, 0) + 1
                if d[word] > max_cnt:
                    max_cnt = d[word]
                    ret = word
                
        return ret
        
