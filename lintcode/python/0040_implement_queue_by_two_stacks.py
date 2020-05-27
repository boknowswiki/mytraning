#!/usr/bin/python -t

# time O(1) for long-term operations

class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.st1 = []
        self.st2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.st1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if len(self.st2) == 0:
            self.move()
        return self.st2.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if len(self.st2) == 0:
            self.move()
        return self.st2[-1]
        
    def move(self):
        while len(self.st1) > 0:
            self.st2.append(self.st1.pop())
            
        return

