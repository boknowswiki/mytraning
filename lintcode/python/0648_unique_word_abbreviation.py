#!/usr/bin/python -t

# hash table


class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    def __init__(self, dictionary):
        # do intialization if necessary
        self.d = {}
        for word in dictionary:
            abbr = self.getAbbr(word)
            if abbr not in self.d:
                self.d[abbr] = set()
            self.d[abbr].add(word)
            
    def getAbbr(self, word):
        if len(word) <= 1:
            return word
            
        return word[0] + str(len(word[1:-1])) + word[-1]

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        # write your code here
        abbr = self.getAbbr(word)
        if abbr not in self.d:
            return True
        
        for word_set in self.d[abbr]:
            if word != word_set:
                return False
                
        return True
        
