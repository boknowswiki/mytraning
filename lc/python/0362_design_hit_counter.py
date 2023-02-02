# queue

import collections

class HitCounter:

    def __init__(self):
        self.cap = 300
        self.queue = collections.deque([])
        

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0] <= timestamp-self.cap:
            self.queue.popleft()

        return len(self.queue)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
