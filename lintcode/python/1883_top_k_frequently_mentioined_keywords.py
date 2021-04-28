#!/usr/bin/python -t

class Solution:
    """
    @param K: a integer
    @param keywords: a list of string
    @param reviews: a list of string
    @return: return the top k keywords list
    """
    def TopkKeywords(self, K, keywords, reviews):
        # write your code here
        keywords_count = {}

        for review in reviews:
            exist = set()
            for word in review.split():
                word = "".join([c for c in word.lower() if c.isalpha()])
                if word in keywords:
                    exist.add(word)
            for word in exist:
                keywords_count[word] = keywords_count.get(word, 0) + 1

        #print(keywords_count)
        return sorted(list(keywords_count.keys()), key=lambda k: (-keywords_count[k], k))[:K]

            
