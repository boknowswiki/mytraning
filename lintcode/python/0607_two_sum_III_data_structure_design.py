#!/usr/bin/python -t

# hash table

class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.m = {}
        
    def add(self, number):
        # write your code here
        self.m[number] = self.m.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for val in self.m:
            needed = value - val
            if needed == val and self.m[needed] >= 2:
                return True
            elif needed != val and needed in self.m:
                return True
                
        return False
        
        
