#!/usr/bin/python -t

# hash table

    def __init__(self):
        self.server_ids = []
        self.id2index = {}

    # @param {int} server_id add a new server to the cluster 
    # @return nothing
    def add(self, server_id):
        if server_id in self.id2index:
            return
        self.server_ids.append(server_id)
        self.id2index[server_id] = len(self.server_ids) - 1

    # @param {int} server_id remove a bad server from the cluster
    # @return nothing
    def remove(self, server_id):
        if server_id not in self.id2index:
            return
        
        # remove the server_id
        index = self.id2index[server_id]
        del self.id2index[server_id]
        
        # overwrite the one to be removed
        last_server_id = self.server_ids[-1]
        self.id2index[last_server_id] = index
        self.server_ids[index] = last_server_id
        self.server_ids.pop()

    # @return {int} pick a server in the cluster randomly with equal probability
    def pick(self):
        import random
        index = random.randint(0, len(self.server_ids) - 1)
        return self.server_ids[index]



# mine solution, doesn't pass all, but I think it's correct.

import random

class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.d = {}
        self.l = []

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        if server_id not in self.d:
            n = len(self.l)
            self.d[server_id] = n
            self.l.append(server_id)
            
        return

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id in self.d:
            index = self.d[server_id]
            del self.l[index]
            del self.d[server_id]
        

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        n = len(self.l)
        return self.l[random.randint(0, n-1)]
        
