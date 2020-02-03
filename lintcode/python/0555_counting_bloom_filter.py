#!/usr/bin/python -t

# hash table

class CountingBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.d = {}

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        # write your code here
        self.d[word] = self.d.get(word, 0) + 1

    """
    @param: word: A string
    @return: nothing
    """
    def remove(self, word):
        # write your code here
        if word not in self.d:
            return
        else:
            self.d[word] -= 1
            if self.d[word] == 0:
                del self.d[word]
                
        return

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        # write your code here
        if word in self.d:
            return True
        else:
            return False
            

