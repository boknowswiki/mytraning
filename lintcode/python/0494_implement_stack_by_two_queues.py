#!/usr/bin/python -t


# stack


import collections

class Stack:
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.q1.append(x)
        return

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        val = self.q1.popleft()

        self.q1, self.q2 = self.q2, self.q1

        return val
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        val = self.pop()
        self.push(val)

        return val

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return not self.q1


import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue.Queue()
        self.q2 = Queue.Queue()
        
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.q1.put(x)
        
        return

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        
        val = self.q1.get()
        
        # swap q1, q2, since q1 is empty now, and move all the remaining val back to q1
        self.q1, self.q2 = self.q2, self.q1

        return

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        
        val = self.q1.get()
        
        # swap q1, q2, since q1 is empty now, and move all the remaining val back to q1
        self.q1, self.q2 = self.q2, self.q1
        
        self.q1.put(val)
        
        return val
        

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return self.q1.qsize() == 0

