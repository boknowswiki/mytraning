#!/usr/bin/python -t

# BFS



from collections import defaultdict, deque

class Solution:
    """
    @param routes:  a list of bus routes
    @param S: start
    @param T: destination
    @return: the least number of buses we must take to reach destination
    """
    def numBusesToDestination(self, routes, S, T):
        # Write your code here
        if S == T:
            return 0
        busToStop = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                busToStop[stop].append(i)
        front = {S, }
        vistedBus = set()
        visitedStop = {S, }
        distance = 1
        while front:
            newfront = set()
            for stop in front:
                for bus in busToStop[stop]:
                    if bus not in vistedBus:
                        vistedBus.add(bus)
                        for nextstop in routes[bus]:
                            if nextstop == T:
                                return distance
                            if nextstop not in visitedStop:
                                newfront.add(nextstop)
                                visitedStop.add(nextstop)
            distance += 1
            front = newfront
        return -1
        
        

# BFS, but MLE


from collections import defaultdict, deque

class Solution:
    """
    @param routes:  a list of bus routes
    @param S: start
    @param T: destination
    @return: the least number of buses we must take to reach destination
    """
    def numBusesToDestination(self, routes, S, T):
        # Write your code here
        stop_to_bus = defaultdict(set)
        
        for i in range(len(routes)):
            for  stop in routes[i]:
                stop_to_bus[stop].add(i)
        
        v_stop = set()
        v_bus = set()
        q = deque()
        q.append(S)
        v_stop.add(S)
        cnt = 0
        
        while len(q) > 0:
            l = len(q)
            
            for i in range(l):
                stop = q.popleft()
                if stop == T:
                    return cnt
                    
                buses = stop_to_bus[stop]
                for bus in buses:
                    if bus in v_bus:
                        continue
                    
                    v_bus.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop not in v_stop:
                            q.append(next_stop)
                            v_stop.add(next_stop)
                            
            cnt += 1
            
        return -1
        
