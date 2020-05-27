#!/usr/bin/python -t

class Stack:
    def __init__(self):
        self.l = []
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.l.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        if len(self.l) > 0:
            self.l.pop()
        
        return

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if len(self.l) > 0:
            return self.l[-1]
        return -1

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.l) == 0

