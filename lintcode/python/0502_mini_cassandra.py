#!/usr/bin/python -t

# hash table

"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""

from collections import OrderedDict

class MiniCassandra:
    
    def __init__(self):
        # do intialization if necessary
        self.d = {}

    """
    @param: row_key: a string
    @param: column_key: An integer
    @param: value: a string
    @return: nothing
    """
    def insert(self, row_key, column_key, column_value):
        # write your code here
        if row_key not in self.d:
            self.d[row_key] = OrderedDict()
            
        self.d[row_key][column_key] = column_value


    """
    @param: row_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    def query(self, row_key, column_start, column_end):
        # write your code here
        ret = []
        if row_key not in self.d:
            return ret
            
        self.d[row_key] = OrderedDict(sorted(self.d[row_key].items()))
        for key, value in self.d[row_key].items():
            if key >= column_start and key <= column_end:
                ret.append(Column(key, value))
                
        return ret
        
