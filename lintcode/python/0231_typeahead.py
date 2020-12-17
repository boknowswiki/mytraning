#!/usr/bin/python -t

class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    def __init__(self, dict):
        # do intialization if necessary
        self.mp = {}
        
        for w in dict:
            l = len(w)
            for i in range(l):
                for j in range(i+1, l+1):
                    tmp = w[i:j]
                    if tmp not in self.mp:
                        self.mp[tmp] = [w]
                    elif self.mp[tmp][-1] != w:
                            self.mp[tmp].append(w)
                            
        return
                    

    """
    @param: str: a string
    @return: a list of words
    """
    def search(self, str):
        # write your code here
        if str not in self.mp:
            return []
        return self.mp[str]
