#!/usr/bin/python -t

# hash table

class Resource:
    
    def __init__(self, value, expired):
        self.value = value
        self.expired = expired

INT_MAX = 0x7fffffff

class Memcache:

    def __init__(self):
        # initialize your data structure here.
        self.client = dict()
    
    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return an integer
    def get(self, curtTime, key):
        # Write your code here
        if key not in self.client:
            return INT_MAX
        res = self.client.get(key)
        if res.expired >= curtTime or res.expired == -1:
            return res.value
        else:
            return INT_MAX

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} value an integer
    # @param {int} ttl an integer
    # @return nothing
    def set(self, curtTime, key, value, ttl):
        # Write your code here
        if ttl:
            res = Resource(value, curtTime + ttl - 1)
        else:
            res = Resource(value, -1)

        self.client[key] = res 
        
    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @return nothing
    def delete(self, curtTime, key):
        # Write your code here
        if key not in self.client:
            return

        del self.client[key]

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def incr(self, curtTime, key, delta):
        # Write your code here
        if self.get(curtTime, key) == INT_MAX:
            return INT_MAX
        self.client[key].value += delta

        return self.client[key].value

    # @param {int} curtTime an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def decr(self, curtTime, key, delta):
        # Write your code here
        if self.get(curtTime, key) == INT_MAX:
            return INT_MAX
        self.client[key].value -= delta

        return self.client[key].value
        

#my own doesn't pass, but i think it's working


class obj:
    def __init__(self, ttl, val):
        self.ttl = ttl
        self.val = val
        
    
INT_MAX = 0x7FFFFFFF

class Memcache:
    def __init__(self):
        # do intialization if necessary
        self.d = {}

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    def get(self, curtTime, key):
        # write your code here
        if key not in self.d:
            return INT_MAX
        else:
            print curtTime, self.d[key].ttl, key
            if self.d[key].ttl >= curtTime or self.d[key].ttl == -1:
                return self.d[key].val
            else:
                return INT_MAX
            

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    def set(self, curtTime, key, value, ttl):
        # write your code here
        if ttl:
            self.d[key] = obj(curtTime+ttl-1, value)
        else:
            self.d[key] = obj(-1, value)
            
        print self.d[key].val, self.d[key].ttl


    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    def delete(self, curtTime, key):
        # write your code here
        if key not in self.d:
            return INT_MAX
        else:
            del self.d[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def incr(self, curtTime, key, delta):
        # write your code here
        if key not in self.d:
            return INT_MAX
        else:
            self.d[key].val += delta
            return self.d[key].val

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def decr(self, curtTime, key, delta):
        # write your code here
        if key not in self.d:
            return INT_MAX
        else:
            self.d[key] -= delta
            return self.d[key]
            
        

