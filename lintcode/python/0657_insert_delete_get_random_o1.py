#!/usr/bin/python -t


import random

class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.l = []
        self.d = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.d:
            return False
            
        if val not in self.d:
            self.l.append(val)
            self.d[val] = len(self.l) -1
            
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val in self.d:
            index = self.d[val]
            last = self.l[-1]
            self.d[index], self.d[last] = last, index
            self.l.pop()
            return True
        else:
            return False

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        return self.l[random.randint(0, len(self.l)-1)]
        
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
