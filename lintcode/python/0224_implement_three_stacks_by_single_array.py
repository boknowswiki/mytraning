#!/usr/bin/python -t

# stack

class ThreeStacks:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.l = [0] * 3 * size
        self.index = [-1, -1, -1]

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """
    def push(self, stackNum, value):
        # Push value into stackNum stack
        self.index[stackNum] += 1
        self.l[stackNum*self.size+self.index[stackNum]] = value
        #print(self.l, self.index)
        return

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def pop(self, stackNum):
        # Pop and return the top element from stackNum stack
        val = self.l[stackNum*self.size+self.index[stackNum]]
        self.index[stackNum] -= 1
        return val

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def peek(self, stackNum):
        # Return the top element
        val = self.l[stackNum*self.size+self.index[stackNum]]
        return val

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """
    def isEmpty(self, stackNum):
        # write your code here
        return self.index[stackNum] == -1

