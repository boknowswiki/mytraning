#!/usr/bin/python -t

# hash table

class HeartBeat:
    
    def __init__(self):
        # do intialization if necessary
        self.d = {}
        self.k = 0

    """
    @param: slaves_ip_list: a list of slaves'ip addresses
    @param: k: An integer
    @return: nothing
    """
    def initialize(self, slaves_ip_list, k):
        # write your code here
        self.k = 2*k
        for ip in slaves_ip_list:
            self.d[ip] = 0

    """
    @param: timestamp: current timestamp in seconds
    @param: slave_ip: the ip address of the slave server
    @return: nothing
    """
    def ping(self, timestamp, slave_ip):
        # write your code here
        if slave_ip in self.d:
            self.d[slave_ip] = timestamp

    """
    @param: timestamp: current timestamp in seconds
    @return: a list of slaves'ip addresses that died
    """
    def getDiedSlaves(self, timestamp):
        # write your code here
        ret = []
        for key in self.d:
            #print key, self.d[key]. self.k
            if timestamp - self.d[key] >= self.k:
                ret.append(key)
                
        return ret
        
