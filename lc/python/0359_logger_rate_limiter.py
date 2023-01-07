# hash map
# time O(1)
# space O(n)

class Logger:

    def __init__(self):
        self.rate = dict()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.rate:
            self.rate[message] = timestamp
            return True
        
        if timestamp >= self.rate[message]+10:
            self.rate[message] = timestamp
            return True

        return False
