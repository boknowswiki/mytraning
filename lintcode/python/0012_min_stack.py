#!/usr/bin/python -t

# time O(1)

class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.st = []
        self.min_st = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        if len(self.min_st) == 0:
            self.st.append(number)
            self.min_st.append(number)
        else:
            self.st.append(number)
            self.min_st.append(min(number, self.min_st[-1]))
            
        return

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if len(self.st) > 0:
            self.min_st.pop()
            return self.st.pop()
        else:
            return -1

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.min_st[-1]

