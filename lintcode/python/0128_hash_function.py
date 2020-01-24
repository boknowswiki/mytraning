#!/usr/bin/python -t

# hash table

class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        ret = 0
        for k in key:
            ret = (ret*33 + ord(k))%HASH_SIZE
        
        return ret
        
